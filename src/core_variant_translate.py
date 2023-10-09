from src.spdi.spdi_class import SPDI
from src.spdi.spdi_utils import SPDITranslate
from src.core_variant import CoreVariantClass
import hgvs.parser
import re
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy


class CVCTranslator:
    def __init__(self):
        self.trans_spdi = SPDITranslate()
        self.hp = hgvs.parser.Parser()
        self.dp = SeqRepoRESTDataProxy(base_url="https://services.genomicmedlab.org/seqrepo")

    def _detect_sequence_type_from_input(self,input_str):
        parts = input_str.split(":")
        sequence_prefix = parts[0][:2]

        if sequence_prefix == "NC":
            return "DNA"
        elif sequence_prefix == "NM":
            return "DNA"
        elif sequence_prefix == "NR":
            return "RNA"
        elif sequence_prefix == "NP":
            return "protein"
        else:
            raise ValueError("Unknown sequence type")
        
    def cvc_to_spdi(self, expression, format_output):
        if expression.origCoordSystem != "0-based interbase":
            raise ValueError('The origCoordsystem must equal 0-based interbase.')

        spdi_obj = SPDI(sequence=expression.sequenceId,
                        position=expression.start,
                        deletion=expression.refAllele,
                        insertion=expression.altAllele)

        if format_output == "object":
            return spdi_obj
        elif format_output == "string":
            return spdi_obj.to_string()
        elif format_output == 'dictionary':
            return spdi_obj.to_dict()
        else:
            raise ValueError("Invalid output_format. Use 'object', 'string', or 'dictionary'.")
        
    def cvc_to_hgvs(self, expression, format_output):
        spdi_expression = self.cvc_to_spdi(expression, format_output='string')
        hgvs_expression = self.trans_spdi.from_spdi_to_rightshift_hgvs(spdi_expression)
        #parse uses the hgvs parsing method
        if format_output == "parse":
            return self.hp.parse_hgvs_variant(hgvs_expression)
        elif format_output == "string":
            return hgvs_expression
        else:
            raise ValueError("Invalid output_format. Use 'parse' or 'string'.")

    def cvc_to_vrs(self, expression, format_output="obj"):
        spdi_expression = self.cvc_to_spdi(expression, format_output='string')

        if format_output == "object":
            return self.trans_spdi.from_spdi_to_vrs(spdi_expression, format_output="obj")
        elif format_output == "dict":
            return self.trans_spdi.from_spdi_to_vrs(spdi_expression, format_output="dict")
        elif format_output == "json":
            return self.trans_spdi.from_spdi_to_vrs(spdi_expression, format_output="json")
        else:
            raise ValueError("Invalid output_format. Use 'obj', 'dict', or 'json'.")

    def spdi_to_cvc(self, expression):
        spdi_re = re.compile(r"(?P<ac>[^:]+):(?P<pos>\d+):(?P<del_len_or_seq>\w*):(?P<ins_seq>\w*)")
        match_obj = spdi_re.match(expression)

        if not match_obj:
            raise ValueError(f"Invalid SPDI expression: {expression}")
        
        spdi_dict = match_obj.groupdict()

        try:
            deletion_length = int(spdi_dict["del_len_or_seq"])
        except ValueError:
            deletion_length = len(spdi_dict["del_len_or_seq"])

        start_position = int(spdi_dict["pos"])
        end_position = start_position + deletion_length

        cvc_instance = CoreVariantClass(
            origCoordSystem='0-based interbase',
            seqType=self._detect_sequence_type_from_input(expression),
            refAllele=spdi_dict["del_len_or_seq"],
            altAllele=spdi_dict["ins_seq"],
            start=start_position,
            end=end_position,
            sequenceId=spdi_dict['ac'],
            kwargs= expression
        )

        return cvc_instance

    def hgvs_to_cvc(self, expression):
        #parsing the hgvs expression to obtain specific felids needed
        parsed_variant = self.hp.parse_hgvs_variant(expression)

        # checks if the position is in the intronic region for both the start position and end position
        if isinstance(parsed_variant.posedit.pos, hgvs.location.BaseOffsetInterval):
            if parsed_variant.posedit.pos.start.is_intronic or parsed_variant.posedit.pos.end.is_intronic:
                raise ValueError(f"Intronic HGVS variants are not supported ({parsed_variant.posedit})")
        
        # modifying position form 1 base indexing to 0 base indexing
        if parsed_variant.posedit.edit.type == "ins":
            start_position = parsed_variant.posedit.pos.start.base
            end_position = parsed_variant.posedit.pos.start.base
        elif parsed_variant.posedit.edit.type in ("sub", "del", "delins"):
            start_position = parsed_variant.posedit.pos.start.base - 1
            end_position = parsed_variant.posedit.pos.end.base
        elif parsed_variant.posedit.edit.type == "dup":
            start_position = parsed_variant.posedit.pos.start.base - 1
            end_position = parsed_variant.posedit.pos.end.base
        else:
            raise ValueError(f"HGVS variant type {parsed_variant.posedit.edit.type} is unsupported")

        cvc_instance = CoreVariantClass(
            origCoordSystem='0-based interbase',
            seqType=self._detect_sequence_type_from_input(expression),
            refAllele=parsed_variant.posedit.edit.ref,
            altAllele=parsed_variant.posedit.edit.alt,
            start=start_position,
            end=end_position,
            sequenceId = parsed_variant.ac,
            kwargs=expression
        )

        return cvc_instance

    def vrs_to_cvc(self, expression):
        sequence_id = expression.location.sequence_id
        translated_sequence_ids = self.dp.translate_sequence_identifier(sequence_id, namespace="refseq")

        if not translated_sequence_ids:
            raise ValueError(f"Unable to translate sequence identifier: {sequence_id}")
        
        sequenceId = translated_sequence_ids[0].split(':')[1]
        reference_allele = str(self.dp.get_sequence(sequenceId, expression.location.interval.start.value, expression.location.interval.end.value))
        alternative_allele = str(expression.state.sequence) if expression.state.sequence else None
        start_val = int(expression.location.interval.start.value)
        end_val = int(expression.location.interval.end.value)

        cvc_instance = CoreVariantClass(
            origCoordSystem='0-based interbase',
            seqType=self._detect_sequence_type_from_input(sequenceId),
            refAllele=reference_allele,
            altAllele=alternative_allele,
            start=start_val,
            end=end_val,
            sequenceId=sequenceId,
            kwargs=expression
        )

        return cvc_instance


