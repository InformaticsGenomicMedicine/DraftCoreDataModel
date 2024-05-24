import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator
import hgvs.normalizer
from hgvs.exceptions import HGVSError

from src.api.variation_norm_api import VarNormRestApi
from src.api.ncbi_variation_services_api import VarServAPI
from src.api.seqrepo_api import SeqRepoAPI

from src.exceptions import HGVSTranslationError

class HGVSTranslate:
    def __init__(self) -> None:
        """Initialize class with the API URL"""
        self.var_norm_api = VarNormRestApi()
        self.var_serv_api = VarServAPI()

        self.hp = hgvs.parser.Parser()
        self.hdp = hgvs.dataproviders.uta.connect()
        # self.hn = hgvs.normalizer.Normalizer(self.hdp)
        self.vr = hgvs.validator.Validator(hdp=self.hdp)
        self.seqrepo_api = SeqRepoAPI()
        self.dp = self.seqrepo_api.seqrepo_dataproxy 
        self.tlr = self.seqrepo_api.tlr

    def _validate_hgvs_variants(self, expression: str) -> str:
        """Validates the given HGVS expression.

        Args:
            expression (str): The HGVS expression to validate.

        Raises:
            HGVSError: If the validation fails.

        Returns:
            str: The validated HGVS expression.
        """
        try:
            parsed_variant = self.hp.parse_hgvs_variant(expression)
            self.vr.validate(parsed_variant)
            return expression
        except HGVSError as e:
            raise HGVSError(
                f"Validation failed for HGVS expression '{expression}': {e}"
            )
    #NOTE: 
    # from_hgvs_to_vrs uses variation normalization API.
    # VarNorm API has been updated and it seems like it is converting to vrs 2.0.
    # instead of sequence_id they have change to sequenceReference
    # also the ID does not match what translate module in vrs 1.3. 
    # for now we will not be using this process of translations.
    def from_hgvs_to_vrs(self, expression: str,validate: bool = True ) -> dict:
        """Translates a given HGVS expression to a VRS expression. On GRCh37 or GRCh 38 assembly and performs fully-justified allele normalization. 
        (Using the Variation Normalization API)

        Args:
            expression (str): The HGVS expression to be translated.

        Raises:
            ValueError: If an error occurs while translating the HGVS expression to a VRS expression.

        Returns:
            dict: The VRS expression obtained from the translation of the HGVS expression.
        """
        try:
            if validate:
                expression = self._validate_hgvs_variants(expression)
            return self.var_norm_api.variation_to_vrs(expression)
        except Exception:
            raise HGVSTranslationError(
                f"An error occurred while translating the HGVS expression '{expression}' to a VRS expression."
            )

    def from_hgvs_to_spdi(self, expression: str, validate: bool = True) -> str:
        """Translates a HGVS expression to a SPDI expression. (Using NCBI API)

        Args:
            expression (str): The HGVS expression to translate.

        Raises:
            ValueError: If an error occurs while translating the HGVS expression to a SPDI expression.

        Returns:
            str: The SPDI expression obtained from the translation of the HGVS expression.
        """
        try: 
            if validate:
                expression = self._validate_hgvs_variants(expression)
            return self.var_serv_api.hgvs_to_spdi(expression)
        except Exception:
            raise HGVSTranslationError(
                f"An error occurred while translating the HGVS expression '{expression}' to a SPDI expression."
            ) 

    # NOTE: this uses the translate module-- possible remove later.
    #changed the name of this method from to_vrs_tranmod to hgvs_to_vrs_trans
    def hgvs_to_vrs_trans(self,expression: str, validate: bool = True) -> object:
        """Convert HGVS, SPDI, gnomad (vcf), beacon to VRS variation. (Using the vrs translate module)

        Args:
            expression (str): hgvs, spdi, gnomad (vcf) or beacon expression

        Raises:
            ValueError: If the provided input is not a string.

        Returns:
            dict: VRS object
        """
        try:
            if validate:
                expression = self._validate_hgvs_variants(expression)
            return self.tlr.translate_from(str(expression),'hgvs')
        except Exception:
            raise HGVSTranslationError(
                f"An error occurred while translating the HGVS expression '{expression}' to a VRS expression."
            )
