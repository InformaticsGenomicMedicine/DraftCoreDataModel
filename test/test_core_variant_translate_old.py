import pytest
from src.core_variant_translate import CVCTranslator
from src.core_variant import CoreVariantClass
from src.api.seqrepo_api import SeqRepoAPI

cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
dp = cn.dp
tlr = cn.tlr

# Creating Demo VRS object example.
vrs_dict = {
    "_id": "ga4gh:VA.CWDQtAfFv3QnUqN3up3J1bs32JVSKFPk",
    "type": "Allele",
    "location": {
        "_id": "ga4gh:VSL.ixj_LC0E_4GQvm7dtG4r5gjf88lWRxU1",
        "type": "SequenceLocation",
        "sequence_id": "ga4gh:SQ.S_KjnFVz-FE7M0W6yoaUDgYxLPc1jyWU",
        "interval": {
            "type": "SequenceInterval",
            "start": {"type": "Number", "value": 12345},
            "end": {"type": "Number", "value": 12346},
        },
    },
    "state": {"type": "LiteralSequenceExpression", "sequence": "A"},
}
vrs_object = tlr.translate_from(vrs_dict, "vrs")

# Creating Demo core variant class example.
cvc_example = CoreVariantClass(
    origCoordSystem="0-based interbase",
    seqType="DNA",
    refAllele="1",
    altAllele="A",
    start=12345,
    end=12346,
    allelicState=None,
    geneSymbol=None,
    hgncId=None,
    chrom=None,
    genomeBuild=None,
    sequenceId="NC_000001.10",
)

# Creating Demo core variant class example 2.
cvc_example2 = CoreVariantClass(
    origCoordSystem="0-based interbase",
    seqType="DNA",
    # NOTE for me to get the translation to be validated it i need to change the 1 to a C
    refAllele="C",
    altAllele="A",
    start=12345,
    end=12346,
    allelicState=None,
    geneSymbol=None,
    hgncId=None,
    chrom=None,
    genomeBuild=None,
    sequenceId="NC_000001.10",
)

# Created the framework of testing.
# More test need to be done.

# Simple test
cvc_to_spdi_tests = [(cvc_example, "NC_000001.10:12345:1:A")]
cvc_to_hgvs_tests = [(cvc_example, "NC_000001.10:g.12346C>A")]
cvc_to_vrs_tests = [
    (
        cvc_example,
        {
            "_id": "ga4gh:VA.CWDQtAfFv3QnUqN3up3J1bs32JVSKFPk",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.ixj_LC0E_4GQvm7dtG4r5gjf88lWRxU1",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.S_KjnFVz-FE7M0W6yoaUDgYxLPc1jyWU",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 12345},
                    "end": {"type": "Number", "value": 12346},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "A"},
        },
    )
]

spdi_to_cvc_tests = [("NC_000001.10:12345:1:A", cvc_example)]
hgvs_to_cvc_tests = [("NC_000001.10:g.12346C>A", cvc_example2)]
vrs_to_cvc_tests = [(vrs_object, cvc_example2)]


@pytest.fixture(scope="module")
def cvc_trans():
    return CVCTranslator()


# CVC to SPDI, HGVS, VRS


@pytest.mark.parametrize("cvc,expected", cvc_to_spdi_tests)
def test_cvc_to_spdi(cvc_trans, cvc, expected):
    resp = cvc_trans.cvc_to_spdi(cvc, format_output="string")
    assert resp == expected


@pytest.mark.parametrize("cvc,expected", cvc_to_hgvs_tests)
def test_cvc_to_hgvs(cvc_trans, cvc, expected):
    resp = cvc_trans.cvc_to_hgvs(cvc, format_output="string")
    assert resp == expected


@pytest.mark.parametrize("cvc,expected", cvc_to_vrs_tests)
def test_cvc_to_vrs(cvc_trans, cvc, expected):
    resp = cvc_trans.cvc_to_vrs(cvc, format_output="dict")
    assert resp == expected


# SPDI, HGVS, VRS to CVC


@pytest.mark.parametrize("spdi,expected", spdi_to_cvc_tests)
def test_spdi_to_cvc(cvc_trans, spdi, expected):
    resp = cvc_trans.spdi_to_cvc(spdi)
    assert str(resp) == str(expected)


@pytest.mark.parametrize("hgvs,expected", hgvs_to_cvc_tests)
def test_hgvs_to_cvc(cvc_trans, hgvs, expected):
    resp = cvc_trans.hgvs_to_cvc(hgvs)
    assert str(resp) == str(expected)


@pytest.mark.parametrize("vrs,expected", vrs_to_cvc_tests)
def test_vrs_to_cvc(cvc_trans, vrs, expected):
    resp = cvc_trans.vrs_to_cvc(vrs)
    assert str(resp) == str(expected)


# NOTE: This is the old test file for the translate class. Could possible use examples later on.
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
