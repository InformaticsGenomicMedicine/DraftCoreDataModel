import pytest
from src.spdi.spdi_class import SPDI

spdi_tests = [
    # Insertion Example
    ("NC_000007.14", "55181230", "", "GGCT"),
    # Substitution Example
    ("NC_000019.10", "44908821", "C", "T"),
    # Deletion Example
    ("NC_000007.14", "55181219", "T", ""),
    # Deletion Insertion Example
    ("NC_000023.11", "32386322", "T", "GA"),
    # Identity Example
    ("NC_000013.11", "32936731", "C", "C"),
    # Duplication Example
    ("NC_000013.11", "19993837", "GT", "GTGT"),
]


@pytest.mark.parametrize("sequence, position, deletion, insertion", spdi_tests)
def test_spdi_init(sequence, position, deletion, insertion):
    spdi_expression = SPDI(sequence, position, deletion, insertion)

    assert spdi_expression.sequence == sequence
    assert spdi_expression.position == position
    assert spdi_expression.deletion == deletion
    assert spdi_expression.insertion == insertion


@pytest.mark.parametrize("sequence, position, deletion, insertion", spdi_tests)
def test_spdi_to_string(sequence, position, deletion, insertion):
    spdi_expression = SPDI(sequence, position, deletion, insertion)
    str_format = spdi_expression.to_string()

    assert isinstance(str_format, str)
    assert str_format == f"{sequence}:{position}:{deletion}:{insertion}"


@pytest.mark.parametrize("sequence, position, deletion, insertion", spdi_tests)
def test_spdi_to_dictionary(sequence, position, deletion, insertion):
    spdi_expression = SPDI(sequence, position, deletion, insertion)
    dict_format = spdi_expression.to_dict()
    expected_dict = {
        "sequence": sequence,
        "position": position,
        "deletion": deletion,
        "insertion": insertion,
    }
    assert isinstance(dict_format, dict)
    assert dict_format == expected_dict
