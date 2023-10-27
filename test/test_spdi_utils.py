import pytest
from src.spdi.spdi_utils import SPDITranslate



spdi_to_vrs_example = (
    ('NC_000001.11:161629780:T:T',{'_id': 'ga4gh:VA.g0DrpsYsVp9QTURGJj9FWqGc_yMUeimD', 'type': 'Allele', 'location': {'_id': 'ga4gh:VSL.VFv5ccgTy-vP0N0EyCi8lSr1ktZUvtqJ',
  'type': 'SequenceLocation',  'sequence_id': 'ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO',  'interval': {'type': 'SequenceInterval',
  'start': {'type': 'Number', 'value': 161629780},'end': {'type': 'Number', 'value': 161629781}}},'state': {'type': 'LiteralSequenceExpression', 'sequence': 'T'}}),
    ('NC_000001.11:943042:C:T',{'_id': 'ga4gh:VA.s8vzlmFv83fcoJnNovFkp4pnE48weUh4','type': 'Allele', 'location': {'_id': 'ga4gh:VSL.2tX8CXXY1z3HcbrXdGGTbmuqmYgNks6G',
  'type': 'SequenceLocation', 'sequence_id': 'ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO','interval': {'type': 'SequenceInterval',
   'start': {'type': 'Number', 'value': 943042},'end': {'type': 'Number', 'value': 943043}}},
 'state': {'type': 'LiteralSequenceExpression', 'sequence': 'T'}})
)
spdi_to_rightshfit_hgvs_example = (
    ('NC_000001.11:161629780:T:T','NC_000001.11:g.161629781='),
    ('NC_000001.11:943042:C:T','NC_000001.11:g.943043C>T')
)



@pytest.fixture(scope="module")
def spdi_translate():
    return SPDITranslate()

@pytest.mark.parametrize("variation,expected",spdi_to_vrs_example)
def test_spdi_to_vrs(spdi_translate,variation,expected):
    resp = spdi_translate.from_spdi_to_vrs(variation,format_output='dict')
    assert resp == expected

@pytest.mark.parametrize("variation,expected",spdi_to_rightshfit_hgvs_example)
def test_spdi_to_rightshift_hgvs(spdi_translate,variation,expected):
    resp = spdi_translate.from_spdi_to_rightshift_hgvs(variation)
    assert resp == expected

