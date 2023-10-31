from ga4gh.vrs.extras.variation_normalizer_rest_dp import (
    VariationNormalizerRESTDataProxy,
)
import requests
import json


class VarNormRestApi(VariationNormalizerRESTDataProxy):
    """
    Extended Rest data proxy for Variation Normalizer API with additional method
    """

    def variation_to_vrs(self, q, untranslatable_returns_text="true"):
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
        endpoint = "/to_vrs"
        url = f"{self.api}{endpoint}"

        params = {"q": q, "untranslatable_returns_text": untranslatable_returns_text}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return json.loads(response.text)["variations"][0]
        else:
            raise requests.HTTPError(
                f"Request failed with status code: {response.status_code}"
            )


if __name__ == "__main__":
    from ga4gh.vrs import models

    proxy_with_vrs = VarNormRestApi()

    allele = models.Allele(
        location=models.SequenceLocation(
            sequence_id="ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT",
            interval=models.SequenceInterval(
                start=models.Number(value=32936731, type="Number"),
                end=models.Number(value=32936732, type="Number"),
                type="SequenceInterval",
            ),
            type="SequenceLocation",
        ),
        state=models.SequenceExpression(sequence="C", type="LiteralSequenceExpression"),
        type="Allele",
    )

    hgvs = "NM_000059.3:c.274G>A"
    vrs_result = proxy_with_vrs.variation_to_vrs(hgvs)
    print("translated hgvs to vrs", vrs_result)

    hgvs_result = proxy_with_vrs.to_hgvs(allele)
    print("translated vrs to hgvs", hgvs_result)
