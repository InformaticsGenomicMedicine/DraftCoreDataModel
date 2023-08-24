# Packages imported
import requests
import json


class var_norm_api:

    def __init__(self):
        """ Initialize class with the API URL """

        self.base_varnorm_url_api = 'https://normalize.cancervariants.org'

        self.headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

    def variation_to_vrs(self,q, untranslatable_returns_text='true'):
        """ Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh38 assembly
        to VRS variation. Performs fully-justified allele normalization.

        Args:
            q (_type_): _description_
            untranslatable_returns_text (str, optional): Defaults to 'true'. True returns VRS Text object when unable
            to translate or normalize query. False returns an empty list when unable to translate
            or normalize query. 

        Raises:
            requests.HTTPError: If the request fails with a non-200 status code.

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