import pytest
from src.api.ncbi_variation_services_api import VarServAPI


data = [
    {
        "DelitionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/2085710/",
        "spdi": "NC_000001.11:1014263:CC:C",
        "hgvs": "NC_000001.11:g.1014265del",
    },
    {
        "InsertionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/1344775/",
        "spdi": "NC_000001.11:113901365::ATA",
        "hgvs": "NC_000001.11:g.113901365_113901366insATA",
    },
    {
        "SubstitutionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/835613/",
        "spdi": "NC_000002.12:27453448:C:T",
        "hgvs": "NC_000002.12:g.27453449C>T",
    },
    {
        "InsertionDeletionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/931239/",
        "spdi": "NC_000002.12:166043788:CA:GAT",
        "hgvs": "NC_000002.12:g.166043789_166043790delinsGAT",
    },
    {
        "IdentityExample": "https://www.ncbi.nlm.nih.gov/snp/rs1805044#hgvs_tab",
        "spdi": "NC_000004.12:88007815:G:G",
        "hgvs": "NC_000004.12:g.88007816=",
    },
    {
        "DuplicationExample": "https://www.ncbi.nlm.nih.gov/clinvar/variation/1297092/",
        "spdi": "NC_000001.11:5880117:TGAGCTTCCA:TGAGCTTCCATGAGCTTCCA",
        "hgvs": "NC_000001.11:g.5880118_5880127dup",
    },
]


@pytest.fixture(scope="module")
def ncbi_variation_api():
    return VarServAPI()


@pytest.mark.parametrize("exaple_data", data)
def test_spdi_to_hgvs(ncbi_variation_api, exaple_data):
    resp = ncbi_variation_api.spdi_to_hgvs(exaple_data["spdi"])
    assert resp == exaple_data["hgvs"]


@pytest.mark.parametrize("exaple_data", data)
def test_hgvs_to_spdi(ncbi_variation_api, exaple_data):
    resp = ncbi_variation_api.hgvs_to_spdi(exaple_data["hgvs"])
    assert resp == exaple_data["spdi"]
