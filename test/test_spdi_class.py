# import pytest
# from src.spdi.spdi_class import SPDI

# spdi_string_examples = (
#     (SPDI('NC_000001.11', 161629780, 'T', 'T'), 'NC_000001.11:161629780:T:T'),
# )

# spdi_dict_examples = (
#     (SPDI('NC_000001.11', 161629780, 'T', 'T'), {'sequence': 'NC_000001.11', 'position': 161629780, 'deletion': 'T', 'insertion': 'T'}),
# )

# @pytest.mark.parametrize("spdi,expected", spdi_string_examples)
# def test_spdi_to_string(spdi, expected):
#     resp = spdi.to_string()
#     assert resp == expected

# @pytest.mark.parametrize("spdi,expected", spdi_dict_examples)
# def test_spdi_to_dict(spdi, expected):
#     resp = spdi.to_dict()
#     assert resp == expected


import pytest
from src.spdi.spdi_class import SPDI


class TestSPDIClass:
    
    def test_spdi_init(self):
        spdi = SPDI('NC_000001.11', 161629780, 'T', 'T')
        assert spdi.sequence == 'NC_000001.11'
        assert spdi.position == 161629780
        assert spdi.deletion == 'T'
        assert spdi.insertion == 'T'
    
    def test_spdi_to_string(self):
        spdi = SPDI('NC_000001.11', 161629780, 'T', 'T')
        assert spdi.to_string() == 'NC_000001.11:100:A:C'
    
    def test_spdi_to_dict(self):
        spdi = SPDI('NC_000001.11', 161629780, 'T', 'T')
        assert spdi.to_dict() == {'sequence': 'NC_000001.11', 'position': 161629780, 'deletion': 'T', 'insertion': 'T'}