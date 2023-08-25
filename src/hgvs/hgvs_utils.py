from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator

import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator
import hgvs.normalizer
from hgvs.exceptions import HGVSError

from src.api.vicc_api import VarNormAPI
from src.api.ncbi_variation_services_api import VarServAPI


class HGVSTranslate:

    def __init__(self):
        """ Initialize class with the API URL """
        
        self.seqrepo_rest_service_url = "https://services.genomicmedlab.org/seqrepo"
        self.dp = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(data_proxy=self.dp,
                 translate_sequence_identifiers=True,  # default
                 normalize=True,                       # default
                 identify=True)                        # default
        self.vnorm = VariationNormalizerRESTDataProxy()
        self.var_norm_api = VarNormAPI()
        self.var_serv_api = VarServAPI()

        self.hp = hgvs.parser.Parser()
        self.hdp = hgvs.dataproviders.uta.connect()
        self.hn = hgvs.normalizer.Normalizer(self.hdp)
        self.vr = hgvs.validator.Validator(hdp=self.hdp)


    def _validate_hgvs_variants(self,expression):
        try:
            parsed_variant = self.hp.parse_hgvs_variant(expression)
            self.vr.validate(parsed_variant)
            return expression
        except HGVSError as e:
            return e
        

    def from_hgvs_to_vrs(self,expression):
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
        except Exception as e:
            return '{}. Expression Error: {}'.format(e,hgvs_expression)


    def from_hgvs_to_spdi(self,expression):
        """ Translate HGVS expression to SPDI expression. (Using NCBI API)

        Args:
            expression (str): HGVS expression

        Returns:
            str: The SPDI representation of the HGVS expression.
        """
        hgvs_expression = self._validate_hgvs_variants(expression)
        try: 
            return self.var_serv_api.hgvs_to_spdi(hgvs_expression)
        except Exception as e: 
            return '{}. Expression Error: {}'.format(e,hgvs_expression) 
        

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