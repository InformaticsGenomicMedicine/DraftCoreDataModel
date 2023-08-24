from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator
from src.old_scripts.api_class import translate_api


class translate_var_from_api:

    def __init__(self):
        """ Initialize class with the API URL """
        
        self.seqrepo_rest_service_url = "https://services.genomicmedlab.org/seqrepo"
        self.dp = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(data_proxy=self.dp,
                 translate_sequence_identifiers=True,  # default
                 normalize=True,                       # default
                 identify=True)                        # default
        self.vnorm = VariationNormalizerRESTDataProxy()
        self.api = translate_api()

    def from_spdi_to_rightshift_hgvs(self,expression):
        """ Translate SPDI expression to right-shift HGVS expression. (Using NCBI API)

        Args:
            expression (string): SPDI expression 

        Returns:
            str: Right shift normalized HGVS expressions
        """
        try: 
            return self.api.spdi_to_hgvs(expression)
        except Exception as e: 
            return '{}. Expression Error: {}'.format(e,expression)

    def from_hgvs_to_spdi(self,expression):
        """ Translate HGVS expression to SPDI expression. (Using NCBI API)

        Args:
            expression (str): HGVS expression

        Returns:
            str: The SPDI representation of the HGVS expression.
        """
        try: 
            return self.api.hgvs_to_spdi(expression)
        except Exception as e: 
            return '{}. Expression Error: {}'.format(e,expression)  

    def to_vrs_api(self,expression):
        """Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh 38 assembly
        to VRS variation. Performs fully-justified allele normalization. (Using the  Variation Normalization API)

        Args:
            expression (str): HGVS, gnomAD VCF or free text expression

        Returns:
            dict: The VRS object of the inputted variation.
        """

        try:
            return self.api.variation_to_vrs(expression)
        except Exception as e:
            return '{}. Expression Error: {}'.format(e,expression)  

    def from_vrs_to_normalize_hgvs(self,vrs_object):
        """ Convert a VRS object into a normalized HGVS expression. (Using the vrs translate.py module)

        Args:
            vrs_object (dict): VRS object

        Returns:
            str: Fully normalized HGVS expressions
        """
        
        pjo = self.tlr.translate_from(vrs_object,"vrs")
        try:
            return self.vnorm.to_hgvs(pjo)[0]
        except Exception as e:
            return '{} Expression Error: {}'.format(e,pjo)  

    def to_vrs_tranmod(self,expression):
        """Convert HGVS, SPDI, gnomad (vcf), beacon to VRS variation. (Using the vrs translate module)

        Args:
            expression (str): hgvs, spdi, gnomad (vcf) or beacon expression

        Raises:
            ValueError: If the provided input is not a string. 

        Returns:
            dict: VRS object
        """
        if not isinstance(expression, str):
            raise ValueError('Invalid {}: is not an integer.'.format(expression))
        try:
            expr = self.tlr.translate_from(expression)
            return expr.as_dict()
        except Exception as e: 
            return '{}. Expression Error: {}'.format(e, expression)