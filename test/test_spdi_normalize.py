# NOTE: Need to find examples to test voca normalization

# import pytest
# from src.spdi.spdi_class import SPDI
# from src.spdi.spdi_normalize import VocaNormalizeSpdi


# spdiExample = [
#     (
#         SPDI(
#             sequence="NC_000023.11",
#             position="32386322",
#             deletion="T",
#             insertion="GA"
#         ),
#         "NC_000023.11:32386322:T:GA",
#     ),
#     (
#         SPDI(sequence="NC_000019.10",
#              position="44908821",
#              deletion="C",
#              insertion="T"
#         ),
#         "NC_000019.10:44908821:C:T",
#     ),
#     (
#         SPDI(
#             sequence="NC_000013.11",
#             position="19993837",
#             deletion="GT",
#             insertion="GTGT",
#         ),

#         "NC_000013.11:19993837:GT:GTGT",
#     ),
# ]


# @pytest.fixture
# def vocanormspdi():
#     return VocaNormalizeSpdi()


# @pytest.mark.parametrize("variation,expected", spdiExample)
# def test_spdi_to_vrs(vocanormspdi, variation, expected):
#     resp = vocanormspdi.spdi_voca_normalize(variation)
#     assert resp == expected
