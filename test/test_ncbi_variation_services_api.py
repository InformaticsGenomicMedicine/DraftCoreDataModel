import pytest
from src.api.ncbi_variation_services_api import VarServAPI
from database.db_operation import DbOperation

data = DbOperation('../database/test_gsdb.db').get_testdata_df()

@pytest.fixture(scope="module")
def ncbi_variation_api():
    return VarServAPI()


@pytest.mark.parametrize("exaple_data", data)
def test_spdi_to_hgvs(ncbi_variation_api, exaple_data):
    resp = ncbi_variation_api.spdi_to_hgvs(exaple_data["spdi"])
    assert resp == exaple_data["hgvs"]


@pytest.mark.parametrize("exaple_data", data)
def test_hgvs_to_spdi(ncbi_variation_api, exaple_data):
    resp = ncbi_variation_api.hgvs_to_spdi(exaple_data["hgvs"])
    assert resp == exaple_data["spdi"]
