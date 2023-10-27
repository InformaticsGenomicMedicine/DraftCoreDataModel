#TODO: All of this needs to be redone.
# This should correlate with core_variant_translate.py







# NOTE: This is the old test file for the translate class.
# import pytest
# from src.old_scripts.translate_class import translate_var_from_api

# # Citation Link: 
#     # Unchanged: https://www.ncbi.nlm.nih.gov/clinvar/variation/242687/?new_evidence=true
#     # Substitution: https://www.ncbi.nlm.nih.gov/clinvar/variation/839655/?new_evidence=true
#     # Deletion: https://www.ncbi.nlm.nih.gov/clinvar/variation/2025454/?new_evidence=true
#     # Insertion: https://www.ncbi.nlm.nih.gov/clinvar/variation/2127271/?new_evidence=true
#     # Duplication: https://www.ncbi.nlm.nih.gov/clinvar/variation/1370201/?new_evidence=true

# # NOTE: Should id a try statement to this function in order to catch errors that variation normalize doesn't catch ? 
# variation_vrs_test = (

#     ('NC_000001.11:g.161629781',{'_id': 'ga4gh:VT.RYjuKX6Cv-N522jb4BZoaljKTrpXNgUN', 'definition': 'NC_000001.11:g.161629781', 'type': 'Text'}),
#     ('NC_000001.11:.943043C>T',{"_id": "ga4gh:VT.RQKniMcZGR4vgBPeFoXTZmY35EoZHs7O","type": "Text","definition": "NC_000001.11:.943043C>T"})
#     # https://www.ncbi.nlm.nih.gov/clinvar/variation/31915/
    
#     )

# spdi_hgvs_tests = (
#     # Unchanged
#     ('NC_000001.11:161629780:TT','Request failed with status code: 400. Expression Error: NC_000001.11:161629780:TT'),

#     # Substitution
#     ('NC_000001:943042:C:T','Request failed with status code: 500. Expression Error: NC_000001:943042:C:T'),

#     #Duplication
#     ('NC_000001.11:935845:GCCGC:GCCGCCGC','NC_000001.11:g.935848_935850dup')

#     )

# hgvs_spdi_tests = (
#     # Unchanged
#     ('NC_000001.11:g.161629781','Request failed with status code: 400. Expression Error: NC_000001.11:g.161629781'),

#     # Substitution
#     ('NC_000001.11:.943043C>T','Request failed with status code: 400. Expression Error: NC_000001.11:.943043C>T'),

#     #Duplication
#     ('NC_000001.11:g.935848_935850dup','NC_000001.11:935845:GCCGC:GCCGCCGC')

#     )

# @pytest.fixture(scope="module")
# def translate():
#     return translate_var_from_api()


# @pytest.mark.parametrize("variation,expected",variation_vrs_test)
# def test_to_vrs_api(translate,variation,expected):
#     resp = translate.to_vrs_api(variation)
#     assert resp == expected


# @pytest.mark.parametrize("spdi,expected", spdi_hgvs_tests)
# def test_from_spdi_to_rightshift_hgvs(translate,spdi,expected):
#     resp = translate.from_spdi_to_rightshift_hgvs(spdi)
#     assert resp == expected


# @pytest.mark.parametrize("hgvs,expected", hgvs_spdi_tests)
# def test_from_hgvs_to_spdi(translate,hgvs,expected):
#     resp = translate.from_hgvs_to_spdi(hgvs)
#     assert resp == expected





