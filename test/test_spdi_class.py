import pytest
from src.spdi.spdi_class import SPDI

spdi_tests = [
    # Deletion Example: https://www.ncbi.nlm.nih.gov/clinvar/variation/2085710/
    ("NC_000001.11", "1014263", "2", "C"),
    # Insertion Example: https://www.ncbi.nlm.nih.gov/clinvar/variation/1344775/
    ("NC_000001.11", "113901365", "", "ATA"),
    # Substitution Example: https://www.ncbi.nlm.nih.gov/clinvar/variation/835613/
    ("NC_000002.12", "27453448", "C", "T"),
    # Insertion Deletion Example: https://www.ncbi.nlm.nih.gov/clinvar/variation/931239/
    ("NC_000002.12", "166043788", "CA", "GAT"),
    # Identity Example: https://www.ncbi.nlm.nih.gov/snp/rs1805044#hgvs_tab
    ("NC_000004.12", "88007815", "G", "G"),
    # Duplication Example: https://www.ncbi.nlm.nih.gov/clinvar/variation/1297092/
    ("NC_000001.11:5880117", "5880117", "TGAGCTTCCA", "TGAGCTTCCATGAGCTTCCA"),
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

