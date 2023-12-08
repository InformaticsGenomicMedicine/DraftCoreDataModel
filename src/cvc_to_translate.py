from src.api.seqrepo_api import SeqRepoAPI
from ga4gh.vrs.utils.hgvs_tools import HgvsTools
from src.core_variant import CoreVariantClass
from src.spdi import SPDI
from ga4gh.core import ga4gh_identify
from ga4gh.vrs import models, normalize as do_normalize
# import hgvs.parser
# import hgvs.location
# import hgvs.posedit
# import hgvs.edit
# import hgvs.sequencevariant
import hgvs.dataproviders.uta

#NOTE: this was seperated from core_variant_translate.py to help debug. 
#TODO: use a better name for this class

class ToTranslate:
    def __init__(self):
        self.cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp = self.cn.dp    
        self.hgvs_tools = None

    def _get_hgvs_tools(self):
        if self.hgvs_tools is None:
            uta_conn = hgvs.dataproviders.uta.connect()
            self.hgvs_tools = HgvsTools(uta_conn)
        return self.hgvs_tools

    def _get_letter_prefix(self, refseq):
        letter_prefix = {
            'NM_': 'n',
            'NP_': 'p',
            'NG_': 'g',
            'NC_': 'g',
        }
        sequence_prefix = refseq.split(":")[0][:3]
        letter = letter_prefix.get(sequence_prefix)

        if letter is None:
            raise ValueError("Unknown reference sequence type.")
        return letter
    
    #TODO: allow format features
    #Double check: https://github.com/ga4gh/vrs-python/blob/e09e09c33e0fd310277d048083812bf5b47b3c74/src/ga4gh/vrs/extras/translator.py#L355C2-L450
    def cvc_to_hgvs(self, expression):
        if expression.origCoordSystem != "0-based interbase":
            raise ValueError("The origCoordsystem must equal 0-based interbase.")

        sequence_id = str(expression.sequenceId)
        aliases = self.dp.translate_sequence_identifier(sequence_id, 'refseq')
        refseq = aliases[0].split(":")[1]
        letter = self._get_letter_prefix(refseq)

        if letter == "p":
            raise ValueError("Only nucleic acid variation is currently supported")
        else:
            start, end = expression.start, expression.end

            if start == end:
                ref = None
                end += 1
            else:
                ref = self.dp.get_sequence(sequence_id, start, end)
                start += 1

            ival = hgvs.location.Interval(
                start=hgvs.location.SimplePosition(base=start),
                end=hgvs.location.SimplePosition(base=end))

            alt = str(expression.altAllele) or None
            edit = hgvs.edit.NARefAlt(ref=ref, alt=alt)

        posedit = hgvs.posedit.PosEdit(pos=ival, edit=edit)
        var = hgvs.sequencevariant.SequenceVariant(
            ac=refseq,
            type=letter,
            posedit=posedit)

        self.hgvs_tools = self._get_hgvs_tools()
        parsed = self.hgvs_tools.parse(str(var))
        var = self.hgvs_tools.normalize(parsed)
        return str(var)
    
    def cvc_to_spdi(self, expression, output_format='string'):
        """Converts a CoreVariantClass object into an SPDI expression. 

        Args:
            expression (object): An object representing a core variant class.
            output_format (str): Desired format for the output. Can be "object","string", or "dict".

        Raises:
            ValueError: If the origCoordSystem of the expression is not "0-based interbase".
            ValueError: If an invalid output format is provided.

        Returns:
            (object or str or dict): Spdi Expression
        """

        if not isinstance(expression, CoreVariantClass):
            raise ValueError("Invalid input format. Expected CoreVariantClass object.")

        if output_format not in ("obj", "string", "dict"):
            raise ValueError("Invalid output format. Use 'obj', 'string', or 'dict'.")

        if expression.origCoordSystem != "0-based interbase":
            raise ValueError("The origCoordsystem must equal 0-based interbase.")

        spdi_obj = SPDI(
            sequence=expression.sequenceId,
            #TODO: double check this this should probably be the end position
            position=str(expression.start),
            deletion=expression.refAllele,
            insertion=expression.altAllele,
        )

        if output_format == "obj":
            return spdi_obj
        elif output_format == "string":
            return spdi_obj.to_string()
        elif output_format == "dict":
            return spdi_obj.to_dict()
        
    # NOTE: Method that normalizes the vrs allele.
    # TODO: Make this a parameter in in the cvc_to_vrs: normalize = true
    def _post_normalize_allele(self, allele):
        seq_id = self.dp.translate_sequence_identifier(allele.location.sequence_id._value, "ga4gh")[0]
        allele.location.sequence_id = seq_id
        allele = do_normalize(allele, self.dp)
        allele._id = ga4gh_identify(allele)
        allele.location._id = ga4gh_identify(allele.location)
        return allele
    
    #TODO: allow format features
    def cvc_to_vrs(self, expression, normalize=True): 
        if expression.origCoordSystem != "0-based interbase":
            raise ValueError("The origCoordsystem must equal 0-based interbase.")

        interval = models.SequenceInterval(start=models.Number(value=expression.start),
                                            end=models.Number(value=expression.end))
        # NOTE: sequence id need to have this particular format: refseq:sequenceId
        location = models.SequenceLocation(sequence_id=f"refseq:{expression.sequenceId}", interval=interval)
        #NOTE: State in the translator.py in vrs-python is always literal. 
        state = models.LiteralSequenceExpression(sequence=expression.altAllele)
        allele = models.Allele(location=location, state=state)
        if normalize:
            allele = self._post_normalize_allele(allele)
            return allele
        else: 
            return allele
    
#NOTE: THIS IS OLD KEEP TILL WE FORSURE DONT WANT TO USE API TO GO FROM CVC -> SPDI -> VRS
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
        

        
#NOTE: THIS IS OLD KEEP TILL WE FORSURE DONT WANT TO USE API TO GO FROM CVC -> SPDI -> HGVS
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

