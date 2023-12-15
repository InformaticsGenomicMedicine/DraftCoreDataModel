import pytest
from src.hgvsExtra.hgvs_utils import HGVSTranslate


hgvs_to_vrs_example = (
    (  # Insertion Example
        "NC_000007.14:g.55181230_55181231insGGCT",
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
    ),
    (  # Substitution Example
        "NC_000019.10:g.44908822C>T",
        {
            "_id": "ga4gh:VA.CxiA_hvYbkD8Vqwjhx5AYuyul4mtlkpD",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.QrRSuBj-VScAGV_gEdxNgsnh41jYH1Kg",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 44908821},
                    "end": {"type": "Number", "value": 44908822},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    ),
    (  # Deletion Example
        "NC_000007.14:g.55181220del",
        {
            "_id": "ga4gh:VA.h6WuolTwZJYZh86qP2a8YVA1WXpHuY_X",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.kB_ok6Eka0225QwwbOKtvcYZBz7Z0mSR",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 55181219},
                    "end": {"type": "Number", "value": 55181220},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": ""},
        },
    ),
    (  # Deletion Insertion Example
        "NC_000023.11:g.32386323delinsGA",
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
    (  # Identity Example
        "NC_000013.11:g.32936732=",
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
    (  # Duplication Example
        "NC_000013.11:g.19993838_19993839dup",
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
)

hgvs_to_spdi_example = (
    # Insertion Example
    ("NC_000007.14:g.55181230_55181231insGGCT", "NC_000007.14:55181230::GGCT"),
    # Substitution Example
    ("NC_000019.10:g.44908822C>T", "NC_000019.10:44908821:C:T"),
    # Deletion Example
    ("NC_000007.14:g.55181220del", "NC_000007.14:55181219:T:"),
    # Deletion Insertion Example
    ("NC_000023.11:g.32386323delinsGA", "NC_000023.11:32386322:T:GA"),
    # Identity Example
    ("NC_000013.11:g.32936732=", "NC_000013.11:32936731:C:C"),
    # Duplication Example
    ("NC_000013.11:g.19993838_19993839dup", "NC_000013.11:19993837:GT:GTGT"),
)


@pytest.fixture(scope="module")
def hgvs_translate():
    return HGVSTranslate()


@pytest.mark.parametrize("variation,expected", hgvs_to_vrs_example)
def test_from_hgvs_to_vrs(hgvs_translate, variation, expected):
    resp = hgvs_translate.from_hgvs_to_vrs(variation)
    assert resp[0] == expected


@pytest.mark.parametrize("variation,expected", hgvs_to_spdi_example)
def test_from_hgvs_to_spdi(hgvs_translate, variation, expected):
    resp = hgvs_translate.from_hgvs_to_spdi(variation)
    assert resp == expected
