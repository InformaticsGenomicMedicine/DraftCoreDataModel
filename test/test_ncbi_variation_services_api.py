import pytest
from src.api.ncbi_variation_services_api import VarServAPI

# Citation Link: 
    # Unchanged: https://www.ncbi.nlm.nih.gov/clinvar/variation/242687/?new_evidence=true
    # Substitution: https://www.ncbi.nlm.nih.gov/clinvar/variation/839655/?new_evidence=true
    # Deletion: https://www.ncbi.nlm.nih.gov/clinvar/variation/2025454/?new_evidence=true
    # Insertion: https://www.ncbi.nlm.nih.gov/clinvar/variation/2127271/?new_evidence=true
    # Duplication: https://www.ncbi.nlm.nih.gov/clinvar/variation/1370201/?new_evidence=true

spdi_hgvs_tests = (
    # Unchanged
    ('NC_000001.11:161629780:T:T','NC_000001.11:g.161629781='),

    # Substitution
    ('NC_000001.11:943042:C:T','NC_000001.11:g.943043C>T'),

    # Deletion
    ('NC_000001.11:930328:AA:','NC_000001.11:g.930329_930330del'),

    #Insertion
    ('NC_000001.11:941302::T','NC_000001.11:g.941302_941303insT'),

    #Duplication
    ('NC_000001.11:935845:GCCGC:GCCGCCGC','NC_000001.11:g.935848_935850dup')

    )

hgvs_spdi_tests = (
    # Unchanged
    ('NC_000001.11:g.161629781=','NC_000001.11:161629780:T:T'),

    # Substitution
    ('NC_000001.11:g.943043C>T','NC_000001.11:943042:C:T'),

    # Deletion
    ('NC_000001.11:g.930329_930330del','NC_000001.11:930328:AA:'),

    #Insertion
    ('NC_000001.11:g.941302_941303insT','NC_000001.11:941302::T'),

    #Duplication
    ('NC_000001.11:g.935848_935850dup','NC_000001.11:935845:GCCGC:GCCGCCGC')

    )

@pytest.fixture(scope="module")
def ncbi_variation_api():
    return VarServAPI()

@pytest.mark.parametrize("spdi,expected", spdi_hgvs_tests)
def test_spdi_to_hgvs(ncbi_variation_api,spdi,expected):
    resp = ncbi_variation_api.spdi_to_hgvs(spdi)
    assert resp == expected


@pytest.mark.parametrize("hgvs,expected", hgvs_spdi_tests)
def test_hgvs_to_spdi(ncbi_variation_api,hgvs,expected):
    resp = ncbi_variation_api.hgvs_to_spdi(hgvs)
    assert resp == expected





