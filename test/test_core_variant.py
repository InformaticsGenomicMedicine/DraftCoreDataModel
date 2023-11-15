import pytest
from src.core_variant import CoreVariantClass

# # #NOTE: These are all made up examples.

#TODO: USE THESE EXAMPLES TO EDIT THE FUNCTIONS CREATED BELOW!


# @pytest.mark.parametrize(
#     "origCoordSystem,seqType,refAllele,altAllele, start, end, allelicState,geneSymbol, hgncId, chrom, genomeBuild, sequenceId",
#     [
#         (
#             "0-based interbase",
#             "DNA",
#             "A",
#             "C",
#             1,
#             100,
#             "homozygous",
#             "BRCA1",
#             1234,
#             "MT",
#             "GRCh37",
#             None,
#         ),
#         (
#             "0-based counting",
#             "RNA",
#             "A",
#             "C",
#             200,
#             600,
#             "heterozygous",
#             "ABCA1",
#             1234,
#             None,
#             None,
#             "NC_000004.11",
#         ),
#         (
#             "1-based counting",
#             "protein",
#             "A",
#             "G",
#             500,
#             2324,
#             "homozygous",
#             "HOXB13",
#             1123,
#             "Y",
#             "GRCh28",
#             "NC_000004.11",
#         ),
#         (
#             "0-based interbase",
#             "DNA",
#             "A",
#             "C",
#             1,
#             100,
#             "homozygous",
#             "BRCA1",
#             1234,
#             "chr 1",
#             "GRCh37",
#             "NC_000004.11",
#         ),
#         (
#             "0-based counting",
#             "RNA",
#             "A",
#             "C",
#             200,
#             600,
#             "heterozygous",
#             "ABCA1",
#             1234,
#             "chr1",
#             "GRCh38",
#             "NC_000004.11",
#         ),
#         # The rest should fail because they are not valid
#         # Need to have either chrom and genomeBuild or sequenceId
#         (
#             "0-based interbase",
#             "DNA",
#             "A",
#             "C",
#             1,
#             100,
#             "homozygous",
#             "BRCA1",
#             1234,
#             "MT",
#             None,
#             None,
#         ),
#         # Need to use single string upper case 1 letter iupac syntax for reference and alternative allele
#         (
#             "1-based counting",
#             "protein",
#             "ATG",
#             "G",
#             500,
#             2324,
#             "homozygous",
#             "HOXB13",
#             1123,
#             "Y",
#             "GRCh28",
#             "NC_000004.11",
#         ),
#         (
#             "1-based counting",
#             "protein",
#             "A",
#             "ATG",
#             500,
#             2324,
#             "homozygous",
#             "HOXB13",
#             1123,
#             "Y",
#             "GRCh28",
#             "NC_000004.11",
#         ),
#         # Start must be greater than or equal to end
#         (
#             "0-based interbase",
#             "DNA",
#             "A",
#             "C",
#             10,
#             9,
#             "homozygous",
#             "BRCA1",
#             1234,
#             "MT",
#             "GRCh37",
#             None,
#         ),
#     ],
# )
# def test_cvc_initParams(
#     origCoordSystem,
#     seqType,
#     refAllele,
#     altAllele,
#     start,
#     end,
#     allelicState,
#     geneSymbol,
#     hgncId,
#     chrom,
#     genomeBuild,
#     sequenceId,
# ):

#     VariantClass = CoreVariantClass(
#         origCoordSystem,
#         seqType,
#         refAllele,
#         altAllele,
#         start,
#         end,
#         allelicState,
#         geneSymbol,
#         hgncId,
#         chrom,
#         genomeBuild,
#         sequenceId,
#     )

#     param_data = VariantClass.init_params()

#     assert param_data["origCoordSystem"] == origCoordSystem
#     assert param_data["seqType"] == seqType
#     assert param_data["allelicState"] == allelicState
#     assert param_data["geneSymbol"] == geneSymbol
#     assert param_data["hgncId"] == hgncId
#     assert param_data["refAllele"] == refAllele
#     assert param_data["altAllele"] == altAllele
#     assert param_data["chrom"] == chrom
#     assert param_data["genomeBuild"] == genomeBuild
#     assert param_data["start"] == start
#     assert param_data["end"] == end
#     assert param_data["sequenceId"] == sequenceId


# @pytest.mark.parametrize(
#     "origCoordSystem,seqType,refAllele,altAllele, start, end, allelicState,geneSymbol, hgncId, chrom, genomeBuild, sequenceId",
#     [
#         (
#             "0-based interbase",
#             "DNA",
#             "A",
#             "C",
#             1,
#             100,
#             "Homozygous",
#             "BRCA1",
#             1234,
#             "MT",
#             "GRCh37",
#             "NC_000004.11",
#         ),
#         (
#             "0-based interbase",
#             "RNA",
#             "A",
#             "C",
#             200,
#             600,
#             "Heterozygous",
#             "ABCA1",
#             1234,
#             "1",
#             "GRCh38",
#             "NC_000004.11",
#         ),
#         (
#             "0-based interbase",
#             "protein",
#             "A",
#             "G",
#             500,
#             2324,
#             "homozygous",
#             "HOXB13",
#             1123,
#             "Y",
#             "GRCh28",
#             "NC_000004.11",
#         ),
#         # The rest should fail because they are not valid
#         (
#             "0-based counting",
#             "RNA",
#             "A",
#             "C",
#             200,
#             600,
#             "heterozygous",
#             "ABCA1",
#             1234,
#             "1",
#             "GRCh38",
#             "NC_000004.11",
#         ),
#         (
#             "1-based counting",
#             "protein",
#             "A",
#             "G",
#             500,
#             2324,
#             "homozygous",
#             "HOXB13",
#             1123,
#             "Y",
#             "GRCh28",
#             "NC_000004.11",
#         ),
#     ],
# )
# def test_cvc_normalized_data(
#     origCoordSystem,
#     seqType,
#     refAllele,
#     altAllele,
#     start,
#     end,
#     allelicState,
#     geneSymbol,
#     hgncId,
#     chrom,
#     genomeBuild,
#     sequenceId,
# ):

#     VariantClass = CoreVariantClass(
#         origCoordSystem,
#         seqType,
#         refAllele,
#         altAllele,
#         start,
#         end,
#         allelicState,
#         geneSymbol,
#         hgncId,
#         chrom,
#         genomeBuild,
#         sequenceId,
#     )

#     normalized_data = VariantClass.normalized_data()

#     assert normalized_data["origCoordSystem"] == origCoordSystem
#     assert normalized_data["seqType"] == seqType.upper().strip()
#     assert normalized_data["allelicState"] == allelicState.lower().strip()
#     assert normalized_data["associatedGene"]["geneSymbol"] == geneSymbol
#     assert normalized_data["associatedGene"]["hgncId"] == hgncId
#     assert normalized_data["refAllele"] == refAllele
#     assert normalized_data["altAllele"] == altAllele
#     assert normalized_data["position"]["chrom"] == chrom
#     assert normalized_data["position"]["genomeBuild"] == genomeBuild
#     assert normalized_data["position"]["start"] == start
#     assert normalized_data["position"]["end"] == end
#     assert normalized_data["position"]["sequenceId"] == sequenceId
#(
#             "0-based interbase",
#             "DNA",
#             "A",
#             "C",
#             1,
#             100,
#             "homozygous",
#             "BRCA1",
#             1234,
#             "MT",
#             "GRCh37",
#             None,
#         ),
#         (
#             "0-based counting",
#             "RNA",
#             "A",
#             "C",
#             200,
#             600,
#             "heterozygous",
#             "ABCA1",
#             1234,
#             None,
#             None,
#             "NC_000004.11",
#         ),


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