import pytest
from src.spdi.spdi_utils import SPDITranslate

data = [
    {
        "DelitionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/2085710/",
        "spdi": "NC_000001.11:1014263:CC:C",
        "hgvs": "NC_000001.11:g.1014265del",
        "vrs": {
            "_id": "ga4gh:VA.BmF3zr2l6XLpLaK8GInM6Q3Emc3JyPD3",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.i6Of9s2jVDuJ4vwU6sCeG-jT7ygmlfx6",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 1014263},
                    "end": {"type": "Number", "value": 1014265},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "C"},
        },
    },
    {
        "InsertionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/1344775/",
        "spdi": "NC_000001.11:113901365::ATA",
        "hgvs": "NC_000001.11:g.113901365_113901366insATA",
        "vrs": {
            "_id": "ga4gh:VA.J9BMdktHGGjE843oD0T_bwUV6WxojkCW",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.TMxdXtmi4ctcTRipHMD6py1Nv1kLMyJd",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 113901365},
                    "end": {"type": "Number", "value": 113901365},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "ATA"},
        },
    },
    {
        "SubstitutionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/835613/",
        "spdi": "NC_000002.12:27453448:C:T",
        "hgvs": "NC_000002.12:g.27453449C>T",
        "vrs": {
            "_id": "ga4gh:VA.fXvhngewkkyVwzEeSJRr5tro8Jcol6Q-",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.nLMbYalHO4OEI2axqkyTMCQxrH98UpDN",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.pnAqCRBrTsUoBghSD1yp_jXWSmlbdh4g",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 27453448},
                    "end": {"type": "Number", "value": 27453449},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    },
    {
        "InsertionDeletionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/931239/",
        "spdi": "NC_000002.12:166043788:CA:GAT",
        "hgvs": "NC_000002.12:g.166043789_166043790delinsGAT",
        "vrs": {
            "_id": "ga4gh:VA.I0biXWOvxxmy4jjxsMqQVgy0Q91CJY7x",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.E3BkYwqHo3ETPtXyM_oAzzcpbb07zJ3W",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.pnAqCRBrTsUoBghSD1yp_jXWSmlbdh4g",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 166043788},
                    "end": {"type": "Number", "value": 166043790},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "GAT"},
        },
    },
    {
        "IdentityExample": "https://www.ncbi.nlm.nih.gov/snp/rs1805044#hgvs_tab",
        "spdi": "NC_000004.12:88007815:G:G",
        "hgvs": "NC_000004.12:g.88007816=",
        "vrs": {
            "_id": "ga4gh:VA.eT7IpRxd5CiyJEq8sE6AgobdwgY62NxG",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.Iud8aOpjNALanhgWtq1sU6aQE5uK4ywU",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.HxuclGHh0XCDuF8x6yQrpHUBL7ZntAHc",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 88007815},
                    "end": {"type": "Number", "value": 88007816},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "G"},
        },
    },
    {
        "DuplicationExample": "https://www.ncbi.nlm.nih.gov/clinvar/variation/1297092/",
        "spdi": "NC_000001.11:5880117:TGAGCTTCCA:TGAGCTTCCATGAGCTTCCA",
        "hgvs": "NC_000001.11:g.5880118_5880127dup",
        "vrs": {
            "_id": "ga4gh:VA.OpO3jwlmnhvpmEs2v9orWvMIa7UPb1To",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.veKlh4sQPAIr1HNoqjmsm7qZa0FNfjI9",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 5880117},
                    "end": {"type": "Number", "value": 5880127},
                },
            },
            "state": {
                "type": "LiteralSequenceExpression",
                "sequence": "TGAGCTTCCATGAGCTTCCA",
            },
        },
    },
]


@pytest.fixture(scope="module")
def spdi_translate():
    return SPDITranslate()


@pytest.mark.parametrize("example_data", data)
def test_spdi_to_rightshift_hgvs(spdi_translate, example_data):
    resp = spdi_translate.from_spdi_to_rightshift_hgvs(example_data["spdi"])
    assert resp == example_data["hgvs"]


@pytest.mark.parametrize("example_data", data)
def test_spdi_to_vrs(spdi_translate, example_data):
    resp = spdi_translate.from_spdi_to_vrs(example_data["spdi"], output_format="dict")
    assert resp == example_data["vrs"]
