#TODO: I dont know if we really need this class im trying to think on how we can make it work.

from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator

from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator

class VrsTranslate:

    def __init__(self):
        """ Initialize class with the API URL """
        self.seqrepo_rest_service_url = "https://services.genomicmedlab.org/seqrepo"
        self.dp = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(data_proxy=self.dp,
                 translate_sequence_identifiers=True,  
                 normalize=True,                       
                 identify=True)                        
        self.vnorm = VariationNormalizerRESTDataProxy()

    def from_vrs_to_spdi(self, expression):
        """ Convert a VRS object into a SPDI expression. (Using the vrs translate.py module)

        Args:
            vrs_object (dict): VRS object

        Returns:
            str: SPDI expression
        """
        try:
            if isinstance(expression, dict):
                vrs_obj = self.tlr.translate_from(expression, "vrs")
                return self.tlr.translate_to(vrs_obj, "spdi")[0]
            elif isinstance(expression, object):
                return self.tlr.translate_to(expression, "spdi")[0]
        except Exception as e:
            return '{}: Expression Error: {}'.format(e, expression)

    def from_vrs_to_normalize_hgvs(self,expression):
        """ Convert a VRS object into a normalized HGVS expression. (Using the vrs translate.py module)

        Args:
            vrs_object (dict): VRS object

        Returns:
            str: Fully normalized HGVS expressions
        """
        try:
            if isinstance(expression, dict):
                vrs_obj = self.tlr.translate_from(expression, "vrs")
                return self.vnorm.to_hgvs(vrs_obj, "spdi")[0]
            elif isinstance(expression, object):
                return self.tlr.translate_to(expression, "spdi")[0]
        except Exception as e:
            return '{}: Expression Error: {}'.format(e, expression)

