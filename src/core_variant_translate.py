# Citation: https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/extras/translator.py
# Citation: https://github.com/biocommons/hgvs


import re

from src.spdi.spdi_utils import SPDITranslate
from src.core_variant import CoreVariantClass
from src.api.seqrepo_api import SeqRepoAPI
from src.spdi.spdi_class import SPDI

import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator


class CVCTranslator:
    def __init__(self):
        self.trans_spdi = SPDITranslate()
        self.hp = hgvs.parser.Parser()
        self.cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp = self.cn.dp
        self.hdp = hgvs.dataproviders.uta.connect()
        self.vr = hgvs.validator.Validator(hdp=self.hdp)
        # self.spdi = SPDI()

    def _detect_sequence_type(self, input_str):
        """ Detects that sequence type based on the reference sequence provided.
        Formatted reference sequence: 
            * NC_, NM_, NG_, NR_, NP_

        Args:
            input_str (str): A string representing the reference sequence.

        Raises:
            ValueError: If the input reference sequence is not one of the following format: NC_, NM_, NG_, NR_, NP_

        Returns:
            str: The sequence type which can be "DNA", "RNA", or "protein".
        """
        sequence_prefix_map = {
            "NC_": "DNA",
            "NM_": "DNA",
            "NG_": "DNA",
            "NR_": "RNA",
            "NP_": "protein",
        }
        sequence_prefix = input_str.split(":")[0][:3]

        sequence_type = sequence_prefix_map.get(sequence_prefix)

        if sequence_type is None:
            raise ValueError("Unknown sequence type")

        return sequence_type
    
# NOTE: These were moved to cvc_to_translate.py in order to debug better.

    # def cvc_to_spdi(self, expression, output_format='string'):
    #     """Converts a CoreVariantClass object into an SPDI expression. 

    #     Args:
    #         expression (object): An object representing a core variant class.
    #         output_format (str): Desired format for the output. Can be "object","string", or "dict".

    #     Raises:
    #         ValueError: If the origCoordSystem of the expression is not "0-based interbase".
    #         ValueError: If an invalid output format is provided.

    #     Returns:
    #         (object or str or dict): Spdi Expression
    #     """

    #     if not isinstance(expression, CoreVariantClass):
    #         raise ValueError("Invalid input format. Expected CoreVariantClass object.")

    #     if output_format not in ("obj", "string", "dict"):
    #         raise ValueError("Invalid output format. Use 'obj', 'string', or 'dict'.")

    #     if expression.origCoordSystem != "0-based interbase":
    #         raise ValueError("The origCoordsystem must equal 0-based interbase.")

    #     spdi_obj = SPDI(
    #         sequence=expression.sequenceId,
    #         #TODO: double check this this should probably be the end position
    #         position=str(expression.start),
    #         deletion=expression.refAllele,
    #         insertion=expression.altAllele,
    #     )

    #     if output_format == "obj":
    #         return spdi_obj
    #     elif output_format == "string":
    #         return spdi_obj.to_string()
    #     elif output_format == "dict":
    #         return spdi_obj.to_dict()

    # def cvc_to_hgvs(self, expression, output_format):
    #     """Converts a CoreVariantClass object into an HGVS expression. 

    #     Args:
    #         expression (object): An object representing a core variant class.
    #         output_format (str): Desired format for the output. Can be "parse" or "string".

    #     Raises:
    #         ValueError: If an invalid output format is provided.

    #     Returns:
    #         (parse or string): HGVS expression 
    #     """

    #     if not isinstance(expression, CoreVariantClass):
    #         raise ValueError("Invalid input format. Expected CoreVariantClass object.")

    #     if output_format not in ("parse", "string"):
    #         raise ValueError("Invalid output format. Use 'parse' or 'string'.")

    #     spdi_expression = self.cvc_to_spdi(expression, output_format="string")

    #     if output_format == "parse":
    #         return self.trans_spdi.from_spdi_to_rightshift_hgvs(
    #             spdi_expression, output_format="parse"
    #         )
    #     elif output_format == "string":
    #         return self.trans_spdi.from_spdi_to_rightshift_hgvs(
    #             spdi_expression, output_format="string"
    #         )

    # def cvc_to_vrs(self, expression, output_format="obj"):
    #     """Converts a CoreVariantClass object into an VRS expression.

    #     Args:
    #         expression (object): An object representing a CoreVariantClass.
    #         output_format (str): Desired format for the output. Can be "obj" or "dict", or "json".

    #     Raises:
    #         ValueError: If an invalid output format is provided.

    #     Returns:
    #         (obj,dict,json): VRS expression
    #     """

    #     if not isinstance(expression, CoreVariantClass):
    #         raise ValueError("Invalid input format. Expected CoreVariantClass object.")

    #     if output_format not in ("obj", "dict", "json"):
    #         raise ValueError("Invalid output format. Use 'obj', 'dict', or 'json'.")

    #     spdi_expression = self.cvc_to_spdi(expression, output_format="string")
    #     try:

    #         if output_format == "obj":
    #             return self.trans_spdi.from_spdi_to_vrs(
    #                 spdi_expression, output_format="obj"
    #             )
    #         elif output_format == "dict":
    #             return self.trans_spdi.from_spdi_to_vrs(
    #                 spdi_expression, output_format="dict"
    #             )
    #         elif output_format == "json":
    #             return self.trans_spdi.from_spdi_to_vrs(
    #                 spdi_expression, output_format="json"
    #             )
    #     except ValueError as e:
    #         raise ValueError(f"{e}. Expression Error: {spdi_expression}")

    def spdi_to_cvc(self, expression):
        """Converts an SPDI expression to a CoreVariantClass object.

        Args:
            expression (str): An SPDI expression. 

        Raises:
            ValueError: If the provided SPDI expression is invalid.

        Returns:
            object: An object representing the CoreVariantClass format.
        """
        # TODO: I think i should use the the spdi validation step here then if its valid then extract the values.
        # spdi_re = re.compile(
        #     r"(?P<sequenceId>[^:]+):(?P<pos>\d+):(?P<del_len_or_seq>\w*):(?P<ins_seq>\w*)"
        # )
        # match_obj = spdi_re.match(expression)
        # if not match_obj:
        #     raise ValueError(f"Invalid SPDI expression: {expression}")
        # spdi_dict = match_obj.groupdict()
        # TODO: if we use the validation step then we need to make sure that we modify this part.
        # try:
        #     deletion_length = int(spdi_dict["del_len_or_seq"])
        # except ValueError:
        #     deletion_length = len(spdi_dict["del_len_or_seq"])
        # start_pos = int(spdi_dict["pos"])
        # end_pos = start_pos + deletion_length
        # TODO: test out new method of converting SPDI to CVC
        s, p, d, i = expression.split(":")
        spdi = SPDI(s, p, d, i)

        if isinstance(spdi.deletion, int):
            del_len = spdi.deletion
        else:
            del_len = len(str(spdi.deletion)) 

        start_pos = int(spdi.position)
        end_pos = start_pos + del_len

        try:
            return CoreVariantClass(
                origCoordSystem="0-based interbase",
                seqType=self._detect_sequence_type(expression),
                refAllele=spdi.deletion,  # spdi_dict["del_len_or_seq"],
                altAllele=spdi.insertion,  # spdi_dict["ins_seq"],
                start=start_pos,
                end=end_pos,
                sequenceId=spdi.sequence  # spdi_dict["sequenceId"],
                # NOTE:
                # kwargs= expression
            )
        except Exception as e:
            raise ValueError(
                f"Error creating CoreVariantClass from SPDI: {e}. SPDI Expression: {expression}"
            )


    def hgvs_to_cvc(self, expression):
        """Converts an HGVS expression to a CoreVariantClass object.
            Only supports (ins,sub,del,delins,or dup) HGVS expressions.

        Args:
            expression (str): An HGVS expression. 

        Raises:
            ValueError: If the HGVS expression is in the intronic region
            ValueError: if the HGVS expression is not a supported type. 

        Returns:
            object: An object representing the CoreVariantClass format.
        """
        # validate hgvs input
        parsed_variant = self.hp.parse_hgvs_variant(expression)
        if not self.vr.validate(parsed_variant):
            raise(ValueError(f"Invalid HGVS expression: {expression}"))

        # checks if posedit.pos is an intronic region
        if isinstance(parsed_variant.posedit.pos, hgvs.location.BaseOffsetInterval):
            # checks if the start or end position is intronic
            if (parsed_variant.posedit.pos.start.is_intronic or parsed_variant.posedit.pos.end.is_intronic):
                raise ValueError(f"Intronic HGVS variants are not supported ({parsed_variant.posedit})")
            
        if parsed_variant.posedit.edit.type == "ins":
            start_pos = parsed_variant.posedit.pos.start.base
            end_pos = parsed_variant.posedit.pos.end.base

            ref_seq = parsed_variant.posedit.edit.ref or ""
            alt_seq = parsed_variant.posedit.edit.alt

        elif parsed_variant.posedit.edit.type in ("sub","del","delins","identity","dup"):
            # The starting position is changed to account for 0-interbase indexing
            start_pos = parsed_variant.posedit.pos.start.base - 1 
            end_pos = parsed_variant.posedit.pos.end.base

            if parsed_variant.posedit.edit.type == "sub":
                ref_seq = parsed_variant.posedit.edit.ref
                alt_seq = parsed_variant.posedit.edit.alt

            elif parsed_variant.posedit.edit.type == "del":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = parsed_variant.posedit.edit.alt or ""
                
            elif parsed_variant.posedit.edit.type == "delins":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = parsed_variant.posedit.edit.alt
            
            elif parsed_variant.posedit.edit.type == "identity":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = ref_seq

            elif parsed_variant.posedit.edit.type == "dup":
                ref_seq = self.dp.get_sequence(parsed_variant.ac,start_pos,end_pos)
                alt_seq = ref_seq + ref_seq
        else:
            raise ValueError(
                f"HGVS variant type {parsed_variant.posedit.edit.type} is unsupported"
            )

        cvc_instance = CoreVariantClass(
            origCoordSystem="0-based interbase",
            seqType=self._detect_sequence_type(expression),
            refAllele= ref_seq, #parsed_variant.posedit.edit.ref,
            altAllele= alt_seq, #parsed_variant.posedit.edit.alt,
            start=start_pos,
            end=end_pos,
            sequenceId=parsed_variant.ac,
            # kwargs=expression
        )

        return cvc_instance
    
# NOTE: THIS IS THE OLD WAY I DID IT AND RELEASED THERE WAS ERROR:
# TODO: delelte this after making sure the new method works

        # # modifying position form 1 base indexing to 0 base indexing
        # # Based on the vrs-python translate.py module
        # if parsed_variant.posedit.edit.type == "ins":
        #     start_pos = parsed_variant.posedit.pos.start.base
        #     end_pos = parsed_variant.posedit.pos.start.base
            
        #     alt_allele = parsed_variant.posedit.edit.alt
        #     ref_allele = parsed_variant.posedit.edit.ref

        # elif parsed_variant.posedit.edit.type in ("sub", "del", "delins", "identity"):

        #     start_pos = parsed_variant.posedit.pos.start.base - 1
        #     end_pos = parsed_variant.posedit.pos.end.base


        #     if parsed_variant.posedit.edit.type == "identity":
        #         alt_allele = self.data_proxy.get_sequence(parsed_variant.ac,
        #                                              start_pos,
        #                                              end_pos)
        #     else:
        #         alt_allele = parsed_variant.posedit.edit.alt or ""

        # elif parsed_variant.posedit.edit.type == "dup":
        #     start_pos = parsed_variant.posedit.pos.start.base - 1
        #     end_pos = parsed_variant.posedit.pos.end.base

        #     ref_allele = self.data_proxy.get_sequence(parsed_variant.ac,
        #                                              start_pos,
        #                                              end_pos)
        #     alt_allele = ref_allele + ref_allele

        # else:
        #     raise ValueError(
        #         f"HGVS variant type {parsed_variant.posedit.edit.type} is unsupported"
        #     )

    def vrs_to_cvc(self, expression):
        """Converts an VRS expression to a CoreVariantClass object.

        Args:
            expression (str): An VRS expression.

        Raises:
            ValueError: If there is an issue translating the sequence id using the SeqRepoRESTDataProxy.

        Returns:
            object: An object representing the CoreVariantClass format.
        """
        # sequence_id = expression.location.sequence_id

        translated_sequence_ids = self.dp.translate_sequence_identifier(
            # we are specifying we only want the reference sequence id. 
            expression.location.sequence_id, namespace="refseq"
        )
        if not translated_sequence_ids:
            raise ValueError(f"Unable to translate VRS Sequence ID: {expression.location.sequence_id}")
        
        # try:
            # Based on the vrs-python translate.py module
            #translated_sequence_id returns example = 'refseq:NC_000019.10'
            # so we need to remove the refseq
        ref_sequence_id_parts = translated_sequence_ids[0].split(":")
        if len(ref_sequence_id_parts) < 2:
            raise ValueError(f"Invalid translated sequence identifier format: {translated_sequence_ids[0]}")
        
        ref_sequence_id = ref_sequence_id_parts[1]

        ref_seq = str(
            self.dp.get_sequence(
                ref_sequence_id, 
                expression.location.interval.start.value, 
                expression.location.interval.end.value,
                )
            )

            # TODO: look into this: https://github.com/ga4gh/vrs-python/blob/593508c6e8229336ca1f53a06f69966020cd68f7/src/ga4gh/vrs/extras/translator.py#L412
            # alternative_allele = (
            #     str(expression.state.sequence) if expression.state.sequence else None
            # )

        if expression.state.sequence_type:
            alt_seq = str(expression.state.sequence_type)
        else:
            alt_seq = None

        start_pos = int(expression.location.interval.start.value)
        end_pos = int(expression.location.interval.end.value)

        return CoreVariantClass(
            origCoordSystem="0-based interbase",
            seqType=self._detect_sequence_type(ref_sequence_id),
            refAllele=ref_seq,
            altAllele=alt_seq,
            start=start_pos,
            end=end_pos,
            sequenceId=ref_sequence_id,
            # kwargs=expression
        )
        # except Exception as e:
        #     raise ValueError(
        #         f"Error while creating CoreVariantClass from VRS expression: {e}"
        #     )


