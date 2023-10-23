#TODO: edit test provide just a bit more examples
#TODO: make sure that this is enough to test the core variant class
#TODO: many of the things have changed double check everything. 

import pytest
from src.core_variant import CoreVariantClass

#NOTE: These are all made up examples.

@pytest.mark.parametrize(
    "origCoordSystem,seqType,refAllele,altAllele, start, end, allelicState,geneSymbol, hgncId, chrom, genomeBuild, sequenceId",
    [
        ('0-based interbase', 'DNA', 'A', 'C', 1, 100, 'homozygous', 'BRCA1', 1234,'MT', 'GRCh37','NC_000004.11'),
        ('0-based counting', 'RNA', 'A', 'C', 200, 600,'heterozygous', 'ABCA1', 1234, '1', 'GRCh38','NC_000004.11'),
        ('1-based counting','protein','ATC','TCG',500,2324,'homozygous','HOXB13',1123,'Y','GRCh28','NC_000004.11')
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
        ('0-based interbase', 'DNA', 'A', 'C', 1, 100, 'Homozygous', 'BRCA1', 1234,'MT', 'GRCh37','NC_000004.11'),
        ('0-based interbase', 'RNA', 'A', 'C', 200, 600,'Heterozygous', 'ABCA1', 1234, '1', 'GRCh38','NC_000004.11'),
        ('0-based interbase','protein','ATC','TCG',500,2324,'homozygous','HOXB13',1123,'Y','GRCh28','NC_000004.11'),
        # These two below should fail because these are not normalized due to the origCoordSystem
        ('0-based counting', 'RNA', 'A', 'C', 200, 600,'heterozygous', 'ABCA1', 1234, '1', 'GRCh38','NC_000004.11'),
        ('1-based counting','protein','ATC','TCG',500,2324,'homozygous','HOXB13',1123,'Y','GRCh28','NC_000004.11')
    ]
)


def test_cvc_normalized_data(origCoordSystem,seqType,refAllele,
                  altAllele, start, end, allelicState,
                  geneSymbol, hgncId, chrom, genomeBuild, sequenceId):
    
    VariantClass = CoreVariantClass(origCoordSystem,seqType,refAllele,
                  altAllele, start, end, allelicState,
                  geneSymbol, hgncId, chrom, genomeBuild, sequenceId)
    
    normalized_data = VariantClass.normalizedData()

    assert normalized_data['origCoordSystem'] == origCoordSystem
    assert normalized_data['seqType'] == seqType.upper().strip()
    assert normalized_data['allelicState'] == allelicState.lower().strip()
    assert normalized_data['associatedGene']['geneSymbol'] == geneSymbol
    assert normalized_data['associatedGene']['hgncId'] == hgncId
    assert normalized_data['refAllele'] == refAllele
    assert normalized_data['altAllele'] == altAllele
    assert normalized_data['position']['chrom'] == chrom
    assert normalized_data['position']['genomeBuild'] == genomeBuild
    assert normalized_data['position']['start'] == start
    assert normalized_data['position']['end'] == end
    assert normalized_data['position']['sequenceId'] == sequenceId
    