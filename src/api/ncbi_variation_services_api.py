# Citation: NHI Variation Services: https://api.ncbi.nlm.nih.gov/variation/v0/

# Packages imported
import requests
import json

class VarServAPI:

    def __init__(self):
        """ Initialize class with the API URL """
        
        self.base_ncbi_url_api = 'https://api.ncbi.nlm.nih.gov/variation/v0/'

        self.headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

    def spdi_attribute_concat(self,r):
        """ Extract SPDI attributes, and concatenating the attributes to create a SPDI expressions.

        Args:
            r (request.Response): The response containing SPDI data

        Returns:
            list: A list of SPDI expressions 
        """
        response_json = json.loads(r.text)
        spdi_dict = response_json['data']['spdis'][0] # first spdi expression.
        return ':'.join( (spdi_dict['seq_id'],str(spdi_dict['position']), spdi_dict['deleted_sequence'],spdi_dict['inserted_sequence']) )

#TODO: Write documentation
#NOTE: added validation from NCBI API
    def validate_spdi(self,spdi_id):
        """_summary_

        Args:
            spdi_id (_type_): _description_

        Raises:
            requests.HTTPError: _description_
            requests.HTTPError: _description_

        Returns:
            _type_: _description_
        """
        endpoint = '/spdi/{}/'.format(spdi_id)
        url = f'{self.base_ncbi_url_api}{endpoint}'
        response = requests.get(url,headers=self.headers)

        if response.status_code == 200:

            response_json = json.loads(response.text)
            spdi_dict = response_json['data']
            return ':'.join( (spdi_dict['seq_id'],str(spdi_dict['position']), spdi_dict['deleted_sequence'],spdi_dict['inserted_sequence']) )
        else:
            try:
                # TODO: delete once tested/ check message 
                # error_json = response.json()
                # error_message = error_json['error']['message']
                raise requests.HTTPError(f'Failed to validate SPDI expression: {spdi_id}.') # Error Message: {error_message}
            except json.JSONDecodeError:
                raise requests.HTTPError(f'Failed to parse error response as JSON: {response.text}')

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
            try:
                # TODO: delete once tested/ check message 
                # error_json = response.json()
                # error_message = error_json['error']['message']
                raise requests.HTTPError(f'Failed to validate SPDI expression: {spdi_id}.') #Error Message: {error_message}
            except json.JSONDecodeError:
                raise requests.HTTPError(f'Failed to parse error response as JSON: {response.text}')
        # else:
        #     raise requests.HTTPError(f'Request failed with status code: {response.status_code}')
            
    def hgvs_to_spdi(self,hgvs_id, assembly ='GCF_000001405.38'):
        """Translate HGVS expression to SPDI expression.
        End point used from variation service api: /hgvs/{hgvs}/contextuals

        Args:
            hgvs_id (str): HGVS expression
            assembly (str, optional): Assembly version. Defaults assemlby version to 'GCF_000001405.38'.

        Raises:
            requests.HTTPError: If the request fails with a non-200 status code.

        Returns:
            str: The SPDI representation of the HGVS expression. 
        """

        endpoint = '/hgvs/{}/contextuals{}'.format(hgvs_id,assembly)
        
        url = f'{self.base_ncbi_url_api}{endpoint}' 

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return self.spdi_attribute_concat(response)
        else:
            try:
                #TODO: delete once tested/ check message 
                # error_json = response.json()
                # error_message = error_json['error']['message']
                raise requests.HTTPError(f'Failed to validate SPDI expression: {hgvs_id}.') # Error Message: {error_message}
            except json.JSONDecodeError:
                raise requests.HTTPError(f'Failed to parse error response as JSON: {response.text}')
        # else:
        #     raise requests.HTTPError(f'Request failed with status code: {response.status_code}')