import pytest
from src.vrs.vrs_utils import VrsTranslate
from ga4gh.vrs import models
from database.db_operation import DbOperation

data = DbOperation('../database/new_test_db.db').get_testdata_df()


@pytest.fixture(scope="module")
def vrs_translate():
    return VrsTranslate()


@pytest.mark.parametrize("example_data", data)
def test_from_vrs_to_normalize_hgvs(vrs_translate, example_data):
    resp = vrs_translate.from_vrs_to_hgvs(models.Allele(**example_data["vrs"]))
    assert resp == example_data["hgvs"]


@pytest.mark.parametrize("example_data", data)
def test_from_vrs_to_spdi(vrs_translate, example_data):
    resp = vrs_translate.from_vrs_to_spdi(models.Allele(**example_data["vrs"]),validate=True)
    assert resp == example_data["spdi"]

#TODO: look into these examples test_from_vrs_to_spdi : NM_001331029.1:871:A:G, NM_181798.1:1262:G:T