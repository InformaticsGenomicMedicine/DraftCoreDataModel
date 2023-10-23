from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
from src.api.seqrepo_api import SeqRepoAPI

class VrsTranslate:

    def __init__(self):
        """Initialize class with the API URL """

        self.cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp = self.cn.dp
        self.tlr = self.cn.tlr
        self.vnorm = VariationNormalizerRESTDataProxy()

    def from_vrs_to_spdi(self, expression):
        """Convert a VRS dict or object into a SPDI expression.

        Args:
            expression (dict or object): A VRS dict or object to be converted.

        Returns:
            str: The SPDI expression.
        """
        try:
            if isinstance(expression, dict):
                vrs_dict = self.tlr.translate_from(expression, "vrs")
                return self.tlr.translate_to(vrs_dict, "spdi")[0]
            elif isinstance(expression, object):
                return self.tlr.translate_to(expression, "spdi")[0]
        except Exception as e:
            return f"{e}. Expression Error: {expression}"
        
    def from_vrs_to_normalize_hgvs(self,expression):
        """Convert a VRS dictionary or object into a normalized HGVS expression.

        Args:
            expression (dict or object): A VRS dict or object to be converted.

        Returns:
            str: The fully normalized HGVS expression.
        """
        try:
            if isinstance(expression, dict):
                vrs_dict = self.tlr.translate_from(expression, "vrs")
                return self.vnorm.to_hgvs(vrs_dict, "spdi")[0]
            elif isinstance(expression, object):
                return self.tlr.translate_to(expression, "spdi")[0]
        except Exception as e:
            return f"{e}. Expression Error: {expression}"
