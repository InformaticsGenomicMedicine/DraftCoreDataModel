import pytest
from src.core_variant import CoreVariantClass

@pytest.mark.parametrize(
    "origCoordSystem,seqType,refAllele,altAllele, start, end, allelicState,geneSymbol, hgncId, chrom, genomeBuild, sequenceId",
    [
        ('0-based interbase', 'DNA', 'A', 'C', 1, 100, 'homozygous', 'BRCA1', 1234,'MT', 'GRCh37','NC_000004.11'),
        ('0-based counting', 'DNA', 'A', 'C', 1, 100,'homozygous', 'BRCA1', 1234, 'MT', 'GRCh37','NC_000004.11')
    ]
)

def test_cvc_initParams(origCoordSystem,seqType,refAllele,
                  altAllele, start, end, allelicState,
                  geneSymbol, hgncId, chrom, genomeBuild, sequenceId):
    
    VariantClass = CoreVariantClass(origCoordSystem,seqType,refAllele,
                  altAllele, start, end, allelicState,
                  geneSymbol, hgncId, chrom, genomeBuild, sequenceId)
    
    param_data = VariantClass.initParams()

    assert param_data['origCoordSystem'] == origCoordSystem
    assert param_data['seqType'] == seqType
    assert param_data['allelicState'] == allelicState
    assert param_data['geneSymbol'] == geneSymbol
    assert param_data['hgncId'] == hgncId
    assert param_data['refAllele'] == refAllele
    assert param_data['altAllele'] == altAllele
    assert param_data['chrom'] == chrom
    assert param_data['genomeBuild'] == genomeBuild
    assert param_data['start'] == start
    assert param_data['end'] == end
    assert param_data['sequenceId'] == sequenceId
    

@pytest.mark.parametrize(
    "origCoordSystem,seqType,refAllele,altAllele, start, end, allelicState,geneSymbol, hgncId, chrom, genomeBuild, sequenceId",
    [
        ('0-based interbase', 'DNA', 'A', 'C', 1, 100, 'homozygous', 'BRCA1', 1234,'MT', 'GRCh37','NC_000004.11'),
        ('0-based interbase', 'DNA', 'A', 'C', 1, 100,'homozygous', 'BRCA1', 1234, 'MT', 'GRCh37','NC_000004.11')
    ]
)

def test_cvc_normalized_data(origCoordSystem,seqType,refAllele,
                  altAllele, start, end, allelicState,
                  geneSymbol, hgncId, chrom, genomeBuild, sequenceId):
    
    VariantClass = CoreVariantClass(origCoordSystem,seqType,refAllele,
                  altAllele, start, end, allelicState,
                  geneSymbol, hgncId, chrom, genomeBuild, sequenceId)
    
    normalized_data = VariantClass.normalized_data()

    assert normalized_data['origCoordSystem'] == origCoordSystem
    assert normalized_data['seqType'] == seqType
    assert normalized_data['allelicState'] == allelicState
    assert normalized_data['associatedGene']['geneSymbol'] == geneSymbol
    assert normalized_data['associatedGene']['hgncId'] == hgncId
    assert normalized_data['refAllele'] == refAllele
    assert normalized_data['altAllele'] == altAllele
    assert normalized_data['position']['chrom'] == chrom
    assert normalized_data['position']['genomeBuild'] == genomeBuild
    assert normalized_data['position']['start'] == start
    assert normalized_data['position']['end'] == end
    assert normalized_data['position']['sequenceId'] == sequenceId
    