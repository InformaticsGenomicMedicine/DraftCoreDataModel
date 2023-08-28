from src.api.ncbi_variation_services_api import VarServAPI
from ga4gh.vrs.extras.translator import Translator
from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy

import hgvs.parser

#TODO: Class names should follow a camelCase 
class SPDITranslate:

    def __init__(self):

        self.seqrepo_rest_service_url = "https://services.genomicmedlab.org/seqrepo"
        self.dp = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(data_proxy=self.dp,
                 translate_sequence_identifiers=True,  # default
                 normalize=True,                       # default
                 identify=True)                        # default
        self.var_serv_api = VarServAPI()
        self.hp = hgvs.parser.Parser()

#TODO: reWrite documentation 
    def from_spdi_to_rightshift_hgvs(self,expression,validate= True,format_output= True):
        """ Translate SPDI expression to right-shift HGVS expression. (Using NCBI API)

        Args:
            expression (string): SPDI expression 

        Returns:
            str: Right shift normalized HGVS expressions
        """
        if validate:
            spdi_expression = self.var_serv_api.validate_spdi(expression)
        else:
            spdi_expression = expression

        try: 
            if format_output:
                return self.var_serv_api.spdi_to_hgvs(spdi_expression)
            else:
                hgvs_expression = self.var_serv_api.spdi_to_hgvs(spdi_expression)
                return self.hp.parse_hgvs_variant(hgvs_expression)
        except Exception as e: 
            return '{}. Expression Error: {}'.format(e,spdi_expression)

#TODO: reWrite documentation
    def from_spdi_to_vrs(self,expression,validate= True):
        """SPDI --> VRS

        Args:
            expression (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        if validate:
            spdi_expression = self.var_serv_api.validate_spdi(expression)
        else:
            spdi_expression = expression

        try:
            vrs_expression = self.tlr.translate_from(spdi_expression,"spdi")
            return vrs_expression.as_dict()
        except Exception as e:
            return '{}. Expression Error: {}'.format(e,expression) 
