import pytest
from src.api.variation_norm_api import VarNormRestApi

# Citation Link:
#     Unchanged: https://www.ncbi.nlm.nih.gov/clinvar/variation/242687/?new_evidence=true
#     Substitution: https://www.ncbi.nlm.nih.gov/clinvar/variation/839655/?new_evidence=true

#NOTE: Variation Normalization API changed from sequence_id to sequenceReference.
# Currently stop using VarNorm to translate hgvs to VRS, and will only be using vrs-python translator.py module.

variation_vrs_test = (
    (
        "NC_000001.11:g.161629781=",
        {
            "id": "ga4gh:VA.E1EjA8j8JDkOc0r6mQpsYfHtEBwZboyY",
            "type": "Allele",
            "location": {
                "id": "ga4gh:SL.Xr3nHkM9o9FavUonnFqpDMVaeUHGcyH6",
                "type": "SequenceLocation",
                "sequenceReference": {
                    "type": "SequenceReference",
                    "refgetAccession": "SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                },
                "start": 161629780,
                "end": 161629781,
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    ),
    (
        "NC_000001.11:g.943043C>T",
        {
            "id": "ga4gh:VA.KaNXdfINNTK0jyd4m6XRdhPLbzFQZQDV",
            "type": "Allele",
            "location": {
                "id": "ga4gh:SL.vb5Khxuw3jCvdu_SZx1kWn8IuuO8DHc1",
                "type": "SequenceLocation",
                "sequenceReference": {
                    "type": "SequenceReference",
                    "refgetAccession": "SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                },
                "start": 943042,
                "end": 943043,
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    ),
)


@pytest.fixture(scope="module")
def variation_normalize_api():
    return VarNormRestApi()


@pytest.mark.parametrize("variation,expected", variation_vrs_test)
def test_variation_to_vrs(variation_normalize_api, variation, expected):
    resp = variation_normalize_api.variation_to_vrs(variation)
    assert resp[0] == expected
