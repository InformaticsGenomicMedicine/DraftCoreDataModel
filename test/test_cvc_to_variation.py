import pytest
from src.cvc_to_variant_translate import CVCTranslatorFrom
from src.core_variant import CoreVariantClass
from ga4gh.vrs import models
from database.db_operation import DbOperation

data = DbOperation('../database/gsdb_v2.db').get_testdata_df()

@pytest.fixture(scope="module")
def cvc_trans():
    return CVCTranslatorFrom()

@pytest.mark.parametrize("example_data", data)
def test_spdi_to_cvc(cvc_trans, example_data):
    spdi = example_data['spdi']
    cvc_expected = CoreVariantClass(**example_data['cvc'])
    resp = cvc_trans.cvc_to_spdi(cvc_expected, output_format="string")
    assert str(resp) == str(spdi)

@pytest.mark.parametrize("example_data", data)
def test_hgvs_to_cvc(cvc_trans, example_data):
    hgvs = example_data['hgvs']
    cvc_expected = CoreVariantClass(**example_data['cvc'])
    resp = cvc_trans.cvc_to_hgvs(cvc_expected, output_format="string")
    assert str(resp) == str(hgvs)

@pytest.mark.parametrize("example_data", data)
def test_vrs_to_cvc(cvc_trans, example_data):
    vrs = models.Allele(**example_data['vrs'])
    cvc_expected = CoreVariantClass(**example_data['cvc'])
    resp = cvc_trans.cvc_to_vrs(cvc_expected, output_format="obj")
    assert str(resp) == str(vrs)

