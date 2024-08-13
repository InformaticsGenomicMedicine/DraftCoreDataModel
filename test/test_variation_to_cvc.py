import pytest
from src.variant_to_cvc_translate import CVCTranslatorTo
from src.core_variant import CoreVariantClass
from ga4gh.vrs import models
from database.db_operation import DbOperation

data = DbOperation('../database/gsdb_v3.db').get_testdata_df()

@pytest.fixture(scope="module")
def cvc_trans():
    return CVCTranslatorTo()

@pytest.mark.parametrize("example_data", data)
def test_spdi_to_cvc(cvc_trans, example_data):
    spdi = example_data['spdi']
    cvc_expected = CoreVariantClass(**example_data['cvc'])
    resp = cvc_trans.spdi_to_cvc(spdi)
    assert str(resp) == str(cvc_expected)

@pytest.mark.parametrize("example_data", data)
def test_hgvs_to_cvc(cvc_trans, example_data):
    hgvs = example_data['hgvs']
    cvc_expected = CoreVariantClass(**example_data['cvc'])
    resp = cvc_trans.hgvs_to_cvc(hgvs)
    assert str(resp) == str(cvc_expected)

@pytest.mark.parametrize("example_data", data)
def test_vrs_to_cvc(cvc_trans, example_data):
    vrs = models.Allele(**example_data['vrs'])
    cvc_expected = CoreVariantClass(**example_data['cvc'])
    resp = cvc_trans.vrs_to_cvc(vrs)
    assert str(resp) == str(cvc_expected)