import pytest
from src.vrs.vrs_utils import VrsTranslate
from src.api.seqrepo_api import SeqRepoAPI

cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
dp = cn.dp
tlr = cn.tlr

# vrs_utils is able to handle vrs dictionary or vrs objects. Need to create an example of a vrs object.
# Vrs object was created using vr-python library using the following code:
vrsObject = tlr.translate_from(
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
    "vrs",
)

vrs_to_spdi_test_example = (
    (vrsObject, "NC_000001.11:161629780:1:T"),
    (
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
        "NC_000001.11:943042:1:T",
    ),
)

vrs_to_hgvs_test_example = (
    # Testing vrs object
    (vrsObject, "NC_000001.11:g.161629781="),
    # Testing vrs dictionary
    (
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
        "NC_000001.11:g.943043C>T",
    ),
)


@pytest.fixture(scope="module")
def vrs_translate():
    return VrsTranslate()


@pytest.mark.parametrize("variation,expected", vrs_to_spdi_test_example)
def test_from_vrs_to_spdi(vrs_translate, variation, expected):
    resp = vrs_translate.from_vrs_to_spdi(variation)
    assert resp == expected


@pytest.mark.parametrize("variation,expected", vrs_to_hgvs_test_example)
def test_from_vrs_to_normalize_hgvs(vrs_translate, variation, expected):
    resp = vrs_translate.from_vrs_to_normalize_hgvs(variation)
    assert resp == expected
