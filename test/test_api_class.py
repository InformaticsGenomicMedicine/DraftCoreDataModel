import pytest
from src.api_class import translate_api

# Citation Link: 
    # Unchanged: https://www.ncbi.nlm.nih.gov/clinvar/variation/242687/?new_evidence=true
    # Substitution: https://www.ncbi.nlm.nih.gov/clinvar/variation/839655/?new_evidence=true
    # Deletion: https://www.ncbi.nlm.nih.gov/clinvar/variation/2025454/?new_evidence=true
    # Insertion: https://www.ncbi.nlm.nih.gov/clinvar/variation/2127271/?new_evidence=true
    # Duplication: https://www.ncbi.nlm.nih.gov/clinvar/variation/1370201/?new_evidence=true

variation_vrs_test = (
    ('NC_000001.11:g.161629781=',
     {"_id": "ga4gh:VA.g0DrpsYsVp9QTURGJj9FWqGc_yMUeimD",
      "type": "Allele","location": {"_id": "ga4gh:VSL.VFv5ccgTy-vP0N0EyCi8lSr1ktZUvtqJ",
                                    "type": "SequenceLocation","sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                                    "interval": {"type": "SequenceInterval","start": {"type": "Number","value": 161629780},
                                                 "end": {"type": "Number","value": 161629781}}},"state": {"type": "LiteralSequenceExpression","sequence": "T"}}
        ),
      ('NC_000001.11:g.943043C>T',
       {"_id": "ga4gh:VA.s8vzlmFv83fcoJnNovFkp4pnE48weUh4",
        "type": "Allele","location": {"_id": "ga4gh:VSL.2tX8CXXY1z3HcbrXdGGTbmuqmYgNks6G",
                                      "type": "SequenceLocation","sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                                      "interval": {"type": "SequenceInterval","start": {"type": "Number","value": 943042},
                                                   "end": {"type": "Number","value": 943043}}},"state": {"type": "LiteralSequenceExpression","sequence": "T"}}
        )
    )

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
def variation_api():
    return translate_api()


@pytest.mark.parametrize("variation,expected",variation_vrs_test)
def test_variation_to_vrs(variation_api,variation,expected):
    resp = variation_api.variation_to_vrs(variation)
    assert resp == expected


@pytest.mark.parametrize("spdi,expected", spdi_hgvs_tests)
def test_spdi_to_hgvs(variation_api,spdi,expected):
    resp = variation_api.spdi_to_hgvs(spdi)
    assert resp == expected


@pytest.mark.parametrize("hgvs,expected", hgvs_spdi_tests)
def test_hgvs_to_spdi(variation_api,hgvs,expected):
    resp = variation_api.hgvs_to_spdi(hgvs)
    assert resp == expected





