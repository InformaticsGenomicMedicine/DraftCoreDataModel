import pytest
from src.spdi.spdi_utils import SPDITranslate
from database.db_operation import DbOperation

data = DbOperation('../database/test_gsdb.db').get_testdata_df()


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
