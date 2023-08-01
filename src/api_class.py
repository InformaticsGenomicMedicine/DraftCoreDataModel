# Citation: 
    # https://ngdc.cncb.ac.cn/gwh/assembly/history
    # https://api.ncbi.nlm.nih.gov/variation/v0/
    # https://github.com/ncbi/dbsnp
    # https://github.com/ncbi/dbsnp/blob/master/tutorials/Variation%20Services/Jupyter_Notebook/spdi_batch.ipynb
    # https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/extras/variation_normalizer_rest_dp.py
    # https://normalize.cancervariants.org/variation#/

# Packages imported
import requests
import json

class translate_api:

    def __init__(self):
        """ Initialize class with the API URL """
        
        self.base_ncbi_url_api = 'https://api.ncbi.nlm.nih.gov/variation/v0/'
        self.base_varnorm_url_api = 'https://normalize.cancervariants.org'

        self.headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

    # TODO: I think i should implement this in the code. if the hgvs expression does work then use this. 
    def variation_to_vrs(self,q, untranslatable_returns_text='true'):
        
        """ Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh 38 assembly
        to VRS variation. Performs fully-justified allele normalization.

        Args:
            q (string): HGVS, gnomAD VCF or free text expression
            untranslatable_returns_text (str, optional): True returns VRS Text object when unable
            to translate or normalize query. False returns an empty list when unable to translate
            or normalize query.

        Returns:
            dict: The VRS representation of the variation.
        """
        
        endpoint = '/variation/to_vrs'

        url = f'{self.base_varnorm_url_api}{endpoint}'
        
        params = {
            'q': q,
            'untranslatable_returns_text': untranslatable_returns_text
        }
        
        response = requests.get(url, params=params, headers=self.headers)
        
        if response.status_code == 200:
            return json.loads(response.text)['variations'][0]
        else:
            raise requests.HTTPError(f'Request failed with status code: {response.status_code}')
        
    def spdi_attribute_concat(self,r):
        """Extract SPDI attributes, and concatenating the attributes to create a SPDI expressions.

        Args:
            r (request.Response): The response containing SPDI data

        Returns:
            list: A list of SPDI expressions 
        """
        reqjson = json.loads(r.text)
        spdiobjs = reqjson['data']['spdis'] #[0] Index at first position for the first spdi object. 
        expr_list = []
        for spdiobj in spdiobjs:
            spdi = ':'.join([
                spdiobj['seq_id'],
                str(spdiobj['position']),
                spdiobj['deleted_sequence'],
                spdiobj['inserted_sequence']])
            expr_list.append(spdi)
        return expr_list

    def spdi_to_hgvs(self,spdi_id):
        """ Translate SPDI expression to right-shift hgvs notation.
         End point used from variation service api: /spdi/{spdi}/hgvs

        Args:
            spdi_id (str): SPDI expression 

        Raises:
            requests.HTTPError: If the request fails with a non-200 status code.

        Returns:
            str: Right shift normalized HGVS representation of the SPDI expression.
        """
        endpoint = '/spdi/{}/hgvs'.format(spdi_id)
        
        url = f'{self.base_ncbi_url_api}{endpoint}'

        
        response = requests.get(url,headers=self.headers)

        if response.status_code == 200:
            return json.loads(response.text)['data']['hgvs']
        else:
            raise requests.HTTPError(f'Request failed with status code: {response.status_code}')
    
    def hgvs_to_spdi(self,hgvs_id, assembly ='GCF_000001405.38'):
        """Translate HGVS expression to SPDI expression. 

        Args:
            hgvs_id (str): HGVS expression
            assembly (str, optional): Default assembly version. Defaults to 'GCF_000001405.38'.

        Raises:
            requests.HTTPError: If the request fails with a non-200 status code.

        Returns:
            str: The SPDI representation of the HGVS expression. 
        """

        endpoint = '/hgvs/{}/contextuals{}'.format(hgvs_id,assembly)
        
        url = f'{self.base_ncbi_url_api}{endpoint}' 

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return self.spdi_attribute_concat(response)[0] # if I only want back one spdi expression [0]
        else:
            raise requests.HTTPError(f'Request failed with status code: {response.status_code}')