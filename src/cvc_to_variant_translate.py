from src.api.seqrepo_api import SeqRepoAPI

# from ga4gh.vrs.utils.hgvs_tools import HgvsTools
from src.core_variant import CoreVariantClass
from src.spdi import SPDI
from ga4gh.core import ga4gh_identify
from ga4gh.vrs import models, normalize as vrs_normalize
import hgvs.validator
import hgvs.parser
import hgvs.validator
import hgvs.dataproviders.uta
import json


# TODO: This was seperated from core_variant_translate.py to help debug and code review. Will be merged back once code is reviewed.

class ToTranslate:
    """Preforming translations from CVC to SPDI, HGVS, and VRS."""
    def __init__(self):
        self.seqrepo_api = SeqRepoAPI()
        # self.dp = self.seqrepo_api.seqrepo_data_proxy 
        self.dp = self.seqrepo_api.seqrepo_dataproxy
        self.hp = hgvs.parser.Parser()
        self.hdp = hgvs.dataproviders.uta.connect()
        self.hn = hgvs.normalizer.Normalizer(self.hdp)

    def _get_letter_prefix(self, refseq):
        letter_prefix = {
            "NM_": "n",
            "NP_": "p",
            "NG_": "g",
            "NC_": "g",
        }
        sequence_prefix = refseq.split(":")[0][:3]
        letter = letter_prefix.get(sequence_prefix)

        if letter is None:
            raise ValueError("Unknown reference sequence type.")
        return letter

    def cvc_to_spdi(self, expression, output_format="string"):
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
        
        # SPDI object has built in validation for the sequence, position, deletion and insertion
        spdi_obj = SPDI(
            sequence=expression.sequenceId,
            # Position represents the starting position.
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

    # reference: Double check: https://github.com/ga4gh/vrs-python/blob/e09e09c33e0fd310277d048083812bf5b47b3c74/src/ga4gh/vrs/extras/translator.py#L355C2-L450
    def cvc_to_hgvs(self, expression, output_format="string"):

        # Checking coordSystem
        if expression.origCoordSystem != "0-based interbase":
            raise ValueError("The origCoordsystem must equal 0-based interbase.")

        # Capturing the sequence id and the letter prefix
        sequence_id = str(expression.sequenceId)
        letter = self._get_letter_prefix(sequence_id)

        # Letter prefix p is not supported
        if letter == "p":
            raise ValueError("Only nucleic acid variation is currently supported")
        else:
            start_pos, end_pos = expression.start, expression.end
            # Converting from 1-based counting to 0-based interbase and capturing the reference sequence
            if start_pos == end_pos:
                ref_seq = None
                end_pos += 1
            else:
                ref_seq = self.dp.get_sequence(sequence_id, start_pos, end_pos)
                start_pos += 1

            # Creating interval for hgvs expression
            interval = hgvs.location.Interval(
                start=hgvs.location.SimplePosition(base=start_pos),
                end=hgvs.location.SimplePosition(base=end_pos),
            )

            # Capturing the alternate sequence
            alt_seq = str(expression.altAllele) or None

            # Creating edit object for hgvs expression that includes Reference and Alternate sequence
            edit = hgvs.edit.NARefAlt(ref=ref_seq, alt=alt_seq)
        # Creating poseedit object for hgvs expression including the position and edit
        posedit = hgvs.posedit.PosEdit(pos=interval, edit=edit)
        # Creating hgvs expression
        hgvs_var = hgvs.sequencevariant.SequenceVariant(
            ac=sequence_id, type=letter, posedit=posedit
        )

        # Normalizing the hgvs expression
        parsed_variant = self.hp.parse_hgvs_variant(str(hgvs_var))
        hgvs_var = self.hn.normalize(parsed_variant)

        # Formating the hgvs expression
        if output_format == "string":
            return str(hgvs_var)
        elif output_format == "parse":
            return self.hp.parse_hgvs_variant(str(hgvs_var))
        else:
            raise ValueError("Invalid output format. Use 'string' or 'parse'.")

    # Internal function to normalize the vrs allele
    def _post_normalize_allele(self, allele):
        # Translating the sequence id to ga4gh format
        seq_id = self.dp.translate_sequence_identifier(
            allele.location.sequence_id._value, "ga4gh")[0]
        allele.location.sequence_id = seq_id
        # Using the ga4gh normalize function to normalize the allele. (Coming form biocommons.normalize())
        allele = vrs_normalize(allele, self.dp)
        # Setting the allele id to a  GA4GH digest-based id for the object, as a CURIE
        allele._id = ga4gh_identify(allele)
        # Setting the location id to a GA4GH digest-based id for the object, as a CURIE
        allele.location._id = ga4gh_identify(allele.location)
        return allele

    def cvc_to_vrs(self, expression, normalize=True,output_format="obj"):

        # Checking coordSystem
        if expression.origCoordSystem != "0-based interbase":
            raise ValueError("The origCoordsystem must equal 0-based interbase.")

        # Creating a VRS interval object
        interval = models.SequenceInterval(
            start=models.Number(value=expression.start),
            end=models.Number(value=expression.end),
        )

        # Sequence id need to have this particular format: refseq:sequenceId
        location = models.SequenceLocation(
            sequence_id=f"refseq:{expression.sequenceId}", interval=interval
        )
        # Creating a VRS state object
        state = models.LiteralSequenceExpression(sequence=expression.altAllele)
        # Creating a VRS allele object with the location and state
        allele = models.Allele(location=location, state=state)

        # Normalizing the allele
        if normalize:
            allele = self._post_normalize_allele(allele)

        if output_format == "obj":
            return allele
        elif output_format == "dict":
            return allele.as_dict()
        elif output_format == "json":
            return json.dumps(allele.as_dict())
        else:
            raise ValueError("Invalid output format. Use 'obj', 'dict', or 'json'.")