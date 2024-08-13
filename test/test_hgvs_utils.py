import pytest
from src.hgvsExtra.hgvs_utils import HGVSTranslate
from database.db_operation import DbOperation

data = DbOperation('../database/gsdb_v3.db').get_testdata_df()

@pytest.fixture(scope="module")
def hgvs_translate():
    return HGVSTranslate()


@pytest.mark.parametrize("example_data", data)
def test_from_hgvs_to_vrs(hgvs_translate, example_data):
    resp = hgvs_translate.hgvs_to_vrs_trans(example_data["hgvs"],validate=True)
    assert resp.as_dict() == example_data["vrs"]


@pytest.mark.parametrize("example_data", data)
def test_from_hgvs_to_spdi(hgvs_translate, example_data):
    resp = hgvs_translate.from_hgvs_to_spdi(example_data["hgvs"],validate=True)
    assert resp == example_data["spdi"]
