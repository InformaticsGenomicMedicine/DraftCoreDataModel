from ga4gh.vrs.extras.variation_normalizer_rest_dp import VariationNormalizerRESTDataProxy
import requests
import json

class VariationNormalizerWithVRS(VariationNormalizerRESTDataProxy):
    """
    Extended Rest data proxy for Variation Normalizer API with additional method
    """
    def variation_to_vrs(self, q, untranslatable_returns_text='true'):
        """Convert HGVS, gnomAD VCF or free text variation on GRCh37 or GRCh38 assembly 
        to VRS Variation. 
            * Fully-justified allele normalization: (https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/normalize.py). 

        Args:
            q (str): Variation query in HGVS, gnomAD VCF, or free text format.
            untranslatable_returns_text (str, optional): True returns VRS Text object when unable to translate or normalize query. 
            False returns an empty list when unable to translate or normalize query. Defaults to 'true'.

        Raises:
            requests.HTTPError: If the request fails with a non-200 status code.

        Returns:
            dict: The VRS representation of the variation.
        """
        endpoint = '/to_vrs'
        url = f'{self.api}{endpoint}'

        params = {
            'q': q,
            'untranslatable_returns_text': untranslatable_returns_text
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return json.loads(response.text)['variations'][0]
        else:
            raise requests.HTTPError(f'Request failed with status code: {response.status_code}')

if __name__ == "__main__":
    # Create an instance of VariationNormalizerWithVRS
    proxy_with_vrs = VariationNormalizerWithVRS()
    # Query the API
    variation_query = "NM_000059.3:c.274G>A"
    vrs_result = proxy_with_vrs.variation_to_vrs(variation_query)
    print("Result from variation_to_vrs method:", vrs_result)