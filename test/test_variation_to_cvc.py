import pytest
from src.core_variant_translate import CVCTranslator
from src.core_variant import CoreVariantClass
from ga4gh.vrs import models

from test.data import multiple_examples

@pytest.fixture(scope="module")
def cvc_trans():
    return CVCTranslator()

@pytest.mark.parametrize("example", multiple_examples)
def test_spdi_to_cvc(cvc_trans, example):
    spdi = example['spdi']
    cvc_expected = CoreVariantClass(**example['cvc'])
    resp = cvc_trans.spdi_to_cvc(spdi)
    assert str(resp) == str(cvc_expected)

@pytest.mark.parametrize("example", multiple_examples)
def test_hgvs_to_cvc(cvc_trans, example):
    hgvs = example['hgvs']
    cvc_expected = CoreVariantClass(**example['cvc'])
    resp = cvc_trans.hgvs_to_cvc(hgvs)
    assert str(resp) == str(cvc_expected)

@pytest.mark.parametrize("example", multiple_examples)
def test_vrs_to_cvc(cvc_trans, example):
    vrs = models.Allele(**example['vrs'])
    cvc_expected = CoreVariantClass(**example['cvc'])
    resp = cvc_trans.vrs_to_cvc(vrs)
    assert str(resp) == str(cvc_expected)
