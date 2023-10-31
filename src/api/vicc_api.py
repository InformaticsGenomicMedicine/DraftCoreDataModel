# #Citation: Variant Interpretation for Cancer Consortium (VICC) - https://normalize.cancervariants.org/
# #Citation: Variant Interpretation for Cancer Consortium (VICC)- https://normalize.cancervariants.org/variation

# # Packages imported
# import requests
# import json


# class VarNormAPI:
#     """A class for interacting with the Variant Interpretation for Cancer Consortium (VICC) API. """

#     def __init__(self):       
#         """ Initialize class with the API URL"""
#         self.base_varnorm_url_api = 'https://normalize.cancervariants.org'

#         self.headers = {
#             'Content-Type': 'application/json; charset=utf-8'
#         }

#     def variation_to_vrs(self,q, untranslatable_returns_text='true'):
#         """Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh38 assembly 
#         to VRS Variation. 
#             * Fully-justified allele normalization: (https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/normalize.py). 

#         Args:
#             q (str): Variation query in HGVS, gnomAD VCF, or free text format.
#             untranslatable_returns_text (str, optional): True returns VRS Text object when unable to translate or normalize query. 
#             False returns an empty list when unable to translate or normalize query. Defaults to 'true'.

#         Raises:
#             requests.HTTPError: If the request fails with a non-200 status code.

#         Returns:
#             dict: The VRS representation of the variation.
#         """
#         endpoint = '/variation/to_vrs'

#         url = f'{self.base_varnorm_url_api}{endpoint}'
        
#         params = {
#             'q': q,
#             'untranslatable_returns_text': untranslatable_returns_text
#         }
        
#         response = requests.get(url, params=params, headers=self.headers)
        
#         if response.status_code == 200:
#             return json.loads(response.text)['variations'][0]
#         else:
#             raise requests.HTTPError(f'Request failed with status code: {response.status_code}')
