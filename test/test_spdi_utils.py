import pytest
from src.spdi.spdi_utils import SPDITranslate


spdi_to_vrs_example = (
    (
        "NC_000001.11:161629780:T:T",
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
        "NC_000001.11:943042:C:T",
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
    (
        "NC_000023.11:32386322:T:GA",
        {
            "_id": "ga4gh:VA.HH3RHjZymrie-09X8aR2SMf1ULMlee6u",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.tS45HvJapFexhxmbHe6SBn7dGuC46sni",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.w0WZEvgJF0zf_P4yyTzjjv9oW1z61HHP",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 32386322},
                    "end": {"type": "Number", "value": 32386323},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "GA"},
        },
    ),
    (
        "NC_000013.11:32936731:C:C",
        {
            "_id": "ga4gh:VA.DkZLLMnwoH6zIncSRh2c05nzCNLdTqHl",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.iSZclbNW8T95cXDuNvLMvm6xJd2g4pTn",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 32936731},
                    "end": {"type": "Number", "value": 32936732},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "C"},
        },
    ),
    (
        "NC_000013.11:19993837:GT:GTGT",
        {
            "_id": "ga4gh:VA.S3eUS2hlp6q4pSv4u2CbN0OPMusMUnHZ",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.nW80UuWsc9bgMncP24FLII6qx8aouNki",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ._0wi-qoDrvram155UmcSC-zA5ZK4fpLT",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 19993837},
                    "end": {"type": "Number", "value": 19993839},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "GTGT"},
        },
    ),
    (
        "NC_000017.11:83129587:TTGWCACATGATTG:TTG",
        {
            "_id": "ga4gh:VA.uMh32FdgdocWldFZL5Pi7RxOwvXJX_Md",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.8eHx9-4dIsZIUD6Od9WU-a06qNJKi8ra",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.dLZ15tNO1Ur0IcGjwc3Sdi_0A6Yf4zm7",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 83129587},
                    "end": {"type": "Number", "value": 83129601},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "TTG"},
        },
    ),
    (
        "NC_000003.12:16894810:W:",
        {
            "_id": "ga4gh:VA.LDwtaWm1yS--3mHT84AsBM2g3c9zElNN",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.-gPFR8xJpy5aWeQS6BzfMQOUe2LsJeb-",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Zu7h9AggXxhTaGVsy7h_EZSChSZGcmgX",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 16894810},
                    "end": {"type": "Number", "value": 16894811},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": ""},
        },
    ),
)

spdi_to_rightshfit_hgvs_example = (
    ("NC_000001.11:161629780:T:T", "NC_000001.11:g.161629781="),
    ("NC_000001.11:943042:C:T", "NC_000001.11:g.943043C>T"),
    # Special Case
    ("NC_000017.11:83129587:TTGWCACATGATTG:TTG", "NC_000017.11:g.83129591_83129601del"),
    # Special Case
    ("NC_000003.12:16894810:W:", "NC_000003.12:g.16894811del"),
    ("NC_000013.11:32936731:C:C", "NC_000013.11:g.32936732="),
    ("NC_000013.11:19993837:GT:GTGT", "NC_000013.11:g.19993838_19993839dup"),
    ("NC_000023.11:32386322:T:GA", "NC_000023.11:g.32386323delinsGA"),
)


@pytest.fixture(scope="module")
def spdi_translate():
    return SPDITranslate()


@pytest.mark.parametrize("variation,expected", spdi_to_vrs_example)
def test_spdi_to_vrs(spdi_translate, variation, expected):
    resp = spdi_translate.from_spdi_to_vrs(variation, output_format="dict")
    assert resp == expected


@pytest.mark.parametrize("variation,expected", spdi_to_rightshfit_hgvs_example)
def test_spdi_to_rightshift_hgvs(spdi_translate, variation, expected):
    resp = spdi_translate.from_spdi_to_rightshift_hgvs(variation)
    assert resp == expected
