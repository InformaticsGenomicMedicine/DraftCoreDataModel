import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator
import hgvs.normalizer
from hgvs.exceptions import HGVSError

from src.api.variation_norm_api import VarNormRestApi
from src.api.ncbi_variation_services_api import VarServAPI


class HGVSTranslate:
    def __init__(self) -> None:
        """Initialize class with the API URL """
        self.var_norm_api: VarNormRestApi = VarNormRestApi()
        self.var_serv_api: VarServAPI = VarServAPI()

        self.hp: hgvs.parser.Parser = hgvs.parser.Parser()
        self.hdp: hgvs.dataproviders.uta.AssemblyDataProvider = hgvs.dataproviders.uta.connect()
        self.hn: hgvs.normalizer.Normalizer = hgvs.normalizer.Normalizer(self.hdp)
        self.vr: hgvs.validator.Validator = hgvs.validator.Validator(hdp=self.hdp)

    def _validate_hgvs_variants(self, expression: str) -> str:
        """Validate an HGVS expression.

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
            raise HGVSError(f"Validation failed for HGVS expression '{expression}': {e}")

    def from_hgvs_to_vrs(self, expression: str) -> dict:
        """Convert HGVS on GRCh37 or GRCh 38 assembly to VRS variation. 
        Performs fully-justified allele normalization. (Using the  Variation Normalization API)

        Args:
            expression (str): HGVS, gnomAD VCF or free text expression

        Returns:
            dict: The VRS object of the inputted variation.
        """

        hgvs_expression = self._validate_hgvs_variants(expression)
        try:
            return self.var_norm_api.variation_to_vrs(hgvs_expression)
        except Exception:
            raise ValueError(f"An error occurred while translating the HGVS expression '{hgvs_expression}' to a VRS expression.")

    def from_hgvs_to_spdi(self, expression: str) -> str:
        """ Translate HGVS expression to SPDI expression. (Using NCBI API)

        Args:
            expression (str): HGVS expression

        Returns:
            str: The SPDI representation of the HGVS expression.
        """
        hgvs_expression = self._validate_hgvs_variants(expression)
        try:
            return self.var_serv_api.hgvs_to_spdi(hgvs_expression)
        except Exception:
            raise ValueError(f"An error occurred while translating the HGVS expression '{hgvs_expression}' to a SPDI expression.")


# NOTE: this uses the translate module-- possible remove later.
# def to_vrs_tranmod(self,expression):
#     """Convert HGVS, SPDI, gnomad (vcf), beacon to VRS variation. (Using the vrs translate module)

#     Args:
#         expression (str): hgvs, spdi, gnomad (vcf) or beacon expression

#     Raises:
#         ValueError: If the provided input is not a string.

#     Returns:
#         dict: VRS object
#     """
#     if not isinstance(expression, str):
#         raise ValueError('Invalid {}: is not an integer.'.format(expression))
#     try:
#         expr = self.tlr.translate_from(expression)
#         return expr.as_dict()
#     except Exception as e:
#         return '{}. Expression Error: {}'.format(e, expression)
