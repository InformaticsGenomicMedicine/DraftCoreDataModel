#TODO: I dont know if we really need this class im trying to think on how we can make it work.

from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator

class vrs_translate:

    def __init__(self):
        """ Initialize class with the API URL """
        
        self.seqrepo_rest_service_url = "https://services.genomicmedlab.org/seqrepo"
        self.dp = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(data_proxy=self.dp,
                 translate_sequence_identifiers=True,  
                 normalize=True,                       
                 identify=True)                        
        self.vnorm = VariationNormalizerRESTDataProxy()


    def from_vrs_to_spdi(self,expression):
        """ Convert a VRS object into a SPDI expression. (Using the vrs translate.py module)

        Args:
            vrs_object (dict): VRS object

        Returns:
            str: SPDI expression
        """
        vrs = None
        try:
            vrs = self.tlr.translate_from(expression,"vrs")
            return self.tlr.translate_to(vrs,"spdi")[0]
        except Exception as e:
            if vrs is None:
                return '{}: Expression Error: {}'.format(e, expression)
        
    def from_vrs_to_normalize_hgvs(self,expression):
        """ Convert a VRS object into a normalized HGVS expression. (Using the vrs translate.py module)

        Args:
            vrs_object (dict): VRS object

        Returns:
            str: Fully normalized HGVS expressions
        """
        vrs = None
        try:
            vrs = self.tlr.translate_from(expression,"vrs")
            return self.vnorm.to_hgvs(vrs)[0]
        except Exception as e:
            if vrs is None:
                return '{}: Expression Error: {}'.format(e, expression)


# TODO: double check you dont need this code bellow.


    # def from_hgvs_to_vrs(self,expression):
    #     """Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh 38 assembly
    #     to VRS variation. Performs fully-justified allele normalization. (Using the  Variation Normalization API)

    #     Args:
    #         expression (str): HGVS, gnomAD VCF or free text expression

    #     Returns:
    #         dict: The VRS object of the inputted variation.
    #     """

    #     try:
    #         return self.var_norm_api.variation_to_vrs(expression)
    #     except Exception as e:
    #         return '{}. Expression Error: {}'.format(e,expression)
    
    # def from_normalized_hgvs_to_vrs(self,expression):
    #     """Convert HGVS, SPDI, gnomad (vcf), beacon to VRS variation. (Using the vrs vicc_api module)

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
        
    # def from_vrs_to_normalize_hgvs(self,vrs_object):
    #     """ Convert a VRS object into a normalized HGVS expression. (Using the vrs translate.py module)

    #     Args:
    #         vrs_object (dict): VRS object

    #     Returns:
    #         str: Fully normalized HGVS expressions
    #     """
        
    #     vrs = self.tlr.translate_from(vrs_object,"vrs")
    #     try:
    #         return self.vnorm.to_hgvs(vrs)[0]
    #     except Exception as e:
    #         return '{} Expression Error: {}'.format(e,vrs)  

    # def to_vrs_api(self,expression):
    #     """Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh 38 assembly
    #     to VRS variation. Performs fully-justified allele normalization. (Using the  Variation Normalization API)

    #     Args:
    #         expression (str): HGVS, gnomAD VCF or free text expression

    #     Returns:
    #         dict: The VRS object of the inputted variation.
    #     """

    #     try:
    #         return self.var_norm_api.variation_to_vrs(expression)
    #     except Exception as e:
    #         return '{}. Expression Error: {}'.format(e,expression)