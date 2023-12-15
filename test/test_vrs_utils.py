import pytest
from src.vrs.vrs_utils import VrsTranslate
from ga4gh.vrs import models

vrs_list = [
    {
        "_id": "ga4gh:VA.JKGCs07cFu2wlDydCAe2ea06jMFXyK56",
        "type": "Allele",
        "location": {
            "_id": "ga4gh:VSL.SdvAZCNKh5kf6ClsiOOmw_88fbkFPTqG",
            "type": "SequenceLocation",
            "sequence_id": "ga4gh:SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul",
            "interval": {
                "type": "SequenceInterval",
                "start": {"type": "Number", "value": 55181230},
                "end": {"type": "Number", "value": 55181230},
            },
        },
        "state": {"type": "LiteralSequenceExpression", "sequence": "GGCT"},
    },
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
]

vrs_obj = []
for vrs in vrs_list:
    vrs_obj.append(models.Allele(**vrs))

vrs_to_hgvs_test_example = (
    (vrs_obj[0], "NC_000007.14:g.55181230_55181231insGGCT"),
    (vrs_obj[1], "NC_000001.11:g.943043C>T"),
    (vrs_obj[2], "NC_000001.11:g.161629781="),
)


vrs_to_spdi_test_example = (
    (vrs_obj[0], "NC_000007.14:55181230:0:GGCT"),
    (vrs_obj[1], "NC_000001.11:943042:1:T"),
    (vrs_obj[2], "NC_000001.11:161629780:1:T"),
)


@pytest.fixture(scope="module")
def vrs_translate():
    return VrsTranslate()


@pytest.mark.parametrize("variation,expected", vrs_to_hgvs_test_example)
def test_from_vrs_to_normalize_hgvs(vrs_translate, variation, expected):
    resp = vrs_translate.from_vrs_to_normalize_hgvs(variation)
    assert resp == expected


@pytest.mark.parametrize("variation,expected", vrs_to_spdi_test_example)
def test_from_vrs_to_spdi(vrs_translate, variation, expected):
    resp = vrs_translate.from_vrs_to_spdi(variation)
    assert resp == expected
