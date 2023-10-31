import pytest
from src.api.variation_norm_api import VarNormRestApi

# Citation Link:
#     Unchanged: https://www.ncbi.nlm.nih.gov/clinvar/variation/242687/?new_evidence=true
#     Substitution: https://www.ncbi.nlm.nih.gov/clinvar/variation/839655/?new_evidence=true

variation_vrs_test = (
    (
        "NC_000001.11:g.161629781=",
        {
            "_id": "ga4gh:VA.g0DrpsYsVp9QTURGJj9FWqGc_yMUeimD",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.VFv5ccgTy-vP0N0EyCi8lSr1ktZUvtqJ",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 161629780},
                    "end": {"type": "Number", "value": 161629781},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    ),
    (
        "NC_000001.11:g.943043C>T",
        {
            "_id": "ga4gh:VA.s8vzlmFv83fcoJnNovFkp4pnE48weUh4",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.2tX8CXXY1z3HcbrXdGGTbmuqmYgNks6G",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 943042},
                    "end": {"type": "Number", "value": 943043},
                },
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
    assert resp == expected
