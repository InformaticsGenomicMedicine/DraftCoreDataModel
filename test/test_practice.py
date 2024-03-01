import pytest
from src.core_variant import CoreVariantClass

# Exaxmple: "https://www.ncbi.nlm.nih.gov/clinvar/variation/835613/"

data = [
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "T",
        "start": -27453448,  # Negative start position which is invalid
        "end": 27453449,
        "allelicState": None,
        "geneSymbol": "IFT172",
        "hgncId": None,
        "chrom": "chr 2",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000002.12",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "T",
        "start": 27453448,
        "end": -27453449,  # Negative end position which is invalid
        "allelicState": None,
        "geneSymbol": "IFT172",
        "hgncId": None,
        "chrom": "chr 2",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000002.12",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "T",
        "start": 27453449,  # Start position is greater than end position which is invalid
        "end": 27453448,
        "allelicState": None,
        "geneSymbol": "IFT172",
        "hgncId": None,
        "chrom": "chr 2",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000002.12",
    },
    {
        "origCoordSystem": "interbase",  # Invalid origCoordSystem
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "T",
        "start": 27453448,
        "end": 27453448,
        "allelicState": None,
        "geneSymbol": "IFT172",
        "hgncId": None,
        "chrom": "chr 2",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000002.12",
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "C",
        "altAllele": "T",
        "start": 27453448,
        "end": 27453449,
        "allelicState": None,
        "geneSymbol": "IFT172",
        "hgncId": None,
        "chrom": "chr 2",
        "genomeBuild": None,  # Need to have genomeBuild with chrom or sequenceId
        "sequenceId": None,
    },
    {
        "origCoordSystem": "0-based interbase",
        "seqType": "DNA",
        "refAllele": "U",  # Invalid refAllele because seqType is DNA and should be RNA.
        "altAllele": "T",
        "start": 27453448,
        "end": 27453449,
        "allelicState": None,
        "geneSymbol": "IFT172",
        "hgncId": None,
        "chrom": "chr 2",
        "genomeBuild": "GRCh38",
        "sequenceId": "NC_000002.12",
    },
]

@pytest.mark.parametrize("input_data", data)
def test_validation_with_input_data(input_data):
    with pytest.raises(ValueError):
        CoreVariantClass(**input_data)


# norm_data = [
#     (
#         {
#             "origCoordSystem": "0-based interbase",
#             "seqType": "DNA",
#             "refAllele": "C",
#             "altAllele": "T",
#             "start": 27453448,
#             "end": 27453449,
#             "allelicState": None,
#             "geneSymbol": "IFT172",
#             "hgncId": None,
#             "chrom": "chr 2",
#             "genomeBuild": "GRCh38",
#             "sequenceId": "NC_000002.12",
#         },
#         { 
#             "origCoordSystem": "0-based interbase",
#             "seqType": "DNA",
#             "allelicState": None,
#             "associatedGene": {"geneSymbol": "IFT172", "hgncId": None},
#             "refAllele": "C",
#             "altAllele": "T",
#             "position": {
#                 "chrom": "chr 2",
#                 "genomeBuild": "GRCh38",
#                 "start": 27453448,
#                 "end": 27453449,
#                 "sequenceId": "NC_000002.12",
#             }
#         }
#     )
# ]


# @pytest.mark.parametrize("input_data, expected_output", norm_data)
# def test_normalized_data(input_data, expected_output):
#     instance = CoreVariantClass(**input_data)
#     output = instance.normalized_data()
#     assert output == expected_output
