import pytest
from src.cvc_to_translate import ToTranslate
from src.core_variant import CoreVariantClass
from ga4gh.vrs import models

from test.data import multiple_examples

@pytest.fixture(scope="module")
def cvc_trans():
    return ToTranslate()

@pytest.mark.parametrize("example", multiple_examples)
def test_spdi_to_cvc(cvc_trans, example):
    spdi = example['spdi']
    cvc_expected = CoreVariantClass(**example['cvc'])
    resp = cvc_trans.cvc_to_spdi(cvc_expected, output_format="string")
    assert str(resp) == str(spdi)

@pytest.mark.parametrize("example", multiple_examples)
def test_hgvs_to_cvc(cvc_trans, example):
    hgvs = example['hgvs']
    cvc_expected = CoreVariantClass(**example['cvc'])
    resp = cvc_trans.cvc_to_hgvs(cvc_expected, output_format="string")
    assert str(resp) == str(hgvs)

@pytest.mark.parametrize("example", multiple_examples)
def test_vrs_to_cvc(cvc_trans, example):
    vrs = models.Allele(**example['vrs'])
    cvc_expected = CoreVariantClass(**example['cvc'])
    resp = cvc_trans.cvc_to_vrs(cvc_expected, output_format="obj")
    assert str(resp) == str(vrs)
