import pytest
from src.hgvsExtra.hgvs_utils import HGVSTranslate
from database.db_operation import DbOperation

data = DbOperation('/Users/M278428/Documents/rf_lab_projects/DraftCoreDataModel/database/test_gsdb.db').get_testdata_df()

@pytest.fixture(scope="module")
def hgvs_translate():
    return HGVSTranslate()


@pytest.mark.parametrize("example_data", data)
def test_from_hgvs_to_vrs(hgvs_translate, example_data):
    resp = hgvs_translate.hgvs_to_vrs_trans(example_data["hgvs"])
    assert resp.as_dict() == example_data["vrs"]


@pytest.mark.parametrize("example_data", data)
def test_from_hgvs_to_spdi(hgvs_translate, example_data):
    resp = hgvs_translate.from_hgvs_to_spdi(example_data["hgvs"])
    assert resp == example_data["spdi"]
