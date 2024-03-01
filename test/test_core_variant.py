import pytest
from src.core_variant import CoreVariantClass


# DONT change this is good
@pytest.mark.parametrize("input_data, expected_output", [
    # Test case with different input and output
    ({
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "G",
        "altAllele": "T",
        "start": 50,
        "end": 75,
        "allelicState": "Heterozygous",
        "geneSymbol": "TP53",
        "hgncId": 5678,
        "chrom": "X",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000023.11",
        'kwargs': {}
    }, {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "G",
        "altAllele": "T",
        "start": 50,
        "end": 75,
        "allelicState": "Heterozygous",
        "geneSymbol": "TP53",
        "hgncId": 5678,
        "chrom": "X",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000023.11",
        'kwargs': {'kwargs': {}}
    }),

    ({
        "origCoordSystem": "0-based interbase",
        "seqType": "RNA",
        "refAllele": "A",
        "altAllele": "C",
        "start": 200,
        "end": 600,
        "allelicState": "heterozygous",
        "geneSymbol": "ABCA1",
        "hgncId": 1234,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000004.11",
        'kwargs': {}
    }, {
        "origCoordSystem": "0-based interbase",
        "seqType": "RNA",
        "refAllele": "A",
        "altAllele": "C",
        "start": 200,
        "end": 600,
        "allelicState": "heterozygous",
        "geneSymbol": "ABCA1",
        "hgncId": 1234,
        "chrom": None,
        "genomeBuild": None,
        "sequenceId": "NC_000004.11",
        'kwargs': {'kwargs': {}}
    }),

])
def test_init_params_functionality(input_data, expected_output):
    instance = CoreVariantClass(**input_data)
    output = instance.init_params()
    assert output == expected_output

# DONT change this is good
@pytest.mark.parametrize("input_data, expected_output", [
    ({
        "origCoordSystem": "1-based counting",
        "seqType": "DNA",
        "refAllele": "A",
        "altAllele": "C",
        "start": 50,
        "end": 100,
        "allelicState": "Homozygous",
        "geneSymbol": "BRCA1",
        "hgncId": 1234,
        "chrom": "MT",
        "genomeBuild": "GRCh37",
        "sequenceId": "NC_000004.11",
    }, {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "allelicState": "homozygous",
        "associatedGene":{"geneSymbol": "BRCA1","hgncId": 1234},
        "refAllele": "A",
        "altAllele": "C",
        "position":{
            "chrom": "MT",
            "genomeBuild": "GRCh37",
            "start": 49,
            "end": 100,
             "sequenceId": "NC_000004.11",
        }
    }),
    ({
        "origCoordSystem": "0-based counting",
        "seqType": "DNA",
        "refAllele": "A",
        "altAllele": "C",
        "start": 50,
        "end": 100,
        "allelicState": "Homozygous",
        "geneSymbol": "BRCA1",
        "hgncId": 1234,
        "chrom": "MT",
        "genomeBuild": "GRCh37",
        "sequenceId": "NC_000004.11",
    }, {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "allelicState": "homozygous",
        "associatedGene":{"geneSymbol": "BRCA1","hgncId": 1234},
        "refAllele": "A",
        "altAllele": "C",
        "position":{
            "chrom": "MT",
            "genomeBuild": "GRCh37",
            "start": 51,
            "end": 100,
             "sequenceId": "NC_000004.11",
        }
    })
])
def test_normalized_data(input_data, expected_output):
    instance = CoreVariantClass(**input_data)
    output = instance.normalized_data()
    assert output == expected_output