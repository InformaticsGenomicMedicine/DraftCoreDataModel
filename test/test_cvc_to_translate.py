import pytest
from src.cvc_to_translate import ToTranslate
from src.core_variant import CoreVariantClass
from ga4gh.vrs import models


cvc_list = [
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "",
        "altAllele": "GGCT",
        "start": 55181230,
        "end": 55181230,
        "allelicState": None,
        "geneSymbol": None,
        "hgncId": None,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000007.14",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "T",
        "start": 44908821,
        "end": 44908822,
        "allelicState": None,
        "geneSymbol": None,
        "hgncId": None,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000019.10",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "T",
        "altAllele": "",
        "start": 55181219,
        "end": 55181220,
        "allelicState": None,
        "geneSymbol": None,
        "hgncId": None,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000007.14",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "T",
        "altAllele": "GA",
        "start": 32386322,
        "end": 32386323,
        "allelicState": None,
        "geneSymbol": None,
        "hgncId": None,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000023.11",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "C",
        "start": 32936731,
        "end": 32936732,
        "allelicState": None,
        "geneSymbol": None,
        "hgncId": None,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000013.11",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "GT",
        "altAllele": "GTGT",
        "start": 19993837,
        "end": 19993839,
        "allelicState": None,
        "geneSymbol": None,
        "hgncId": None,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000013.11",
    },
]
cvc_example = []
for cvc in cvc_list:
    cvc_example.append(CoreVariantClass(**cvc))

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
]
vrs_example = []
for vrs in vrs_list:
    vrs_example.append(models.Allele(**vrs))


cvc_to_spdi_tests = [
    (cvc_example[0], "NC_000007.14:55181230::GGCT"),
    (cvc_example[1], "NC_000019.10:44908821:C:T"),
    (cvc_example[2], "NC_000007.14:55181219:T:"),
    (cvc_example[3], "NC_000023.11:32386322:T:GA"),
    (cvc_example[4], "NC_000013.11:32936731:C:C"),
    (cvc_example[5], "NC_000013.11:19993837:GT:GTGT"),
]

cvc_to_hgvs_tests = [
    (cvc_example[0], "NC_000007.14:g.55181230_55181231insGGCT"),
    (cvc_example[1], "NC_000019.10:g.44908822C>T"),
    (cvc_example[2], "NC_000007.14:g.55181220del"),
    (cvc_example[3], "NC_000023.11:g.32386323delinsGA"),
    (cvc_example[4], "NC_000013.11:g.32936732="),
    (cvc_example[5], "NC_000013.11:g.19993838_19993839dup"),
]


cvc_to_vrs_tests = [
    (cvc_example[0], vrs_example[0]),
    (cvc_example[1], vrs_example[1]),
    (cvc_example[2], vrs_example[2]),
    (cvc_example[3], vrs_example[3]),
    (cvc_example[4], vrs_example[4]),
    (cvc_example[5], vrs_example[5]),
]


@pytest.fixture(scope="module")
def cvc_trans():
    return ToTranslate()


@pytest.mark.parametrize("cvc,expected", cvc_to_spdi_tests)
def test_cvc_to_spdi(cvc_trans, cvc, expected):
    resp = cvc_trans.cvc_to_spdi(cvc, output_format="string")
    assert resp == expected


@pytest.mark.parametrize("cvc,expected", cvc_to_hgvs_tests)
def test_cvc_to_hgvs(cvc_trans, cvc, expected):
    resp = cvc_trans.cvc_to_hgvs(cvc, output_format="string")
    assert resp == expected


@pytest.mark.parametrize("cvc,expected", cvc_to_vrs_tests)
def test_cvc_to_vrs(cvc_trans, cvc, expected):
    resp = cvc_trans.cvc_to_vrs(cvc, output_format="obj")
    assert resp == expected
