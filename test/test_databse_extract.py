import pytest
from src.database_extract import request_local_api


row_example_1 = [
    (1, {'id': 1, 'origcoordsystem': '0-based interbase', 'seqtype': 'DNA', 'refallele': 'C', 'altallele': 'A', 'startcoord': 12345, 'endcoord': 12346, 
         'chrom': '3', 'genomebuild': 'GRCh38', 'sequenceid': 'NC_000001.10', 'allelicstate': 'heterozygous', 'genesymbol': 'GENE1', 'hgncid': 123, 
         'originalvalue': 'NC_000001.10:12345:C:A', 'originaltype': 'spdi_str', 'normspdi': 'NC_000001.10:12345:C:A', 'normhgvs': 'NC_000001.10:g.12346C>A',
         'normvrs': {'_id': 'ga4gh:VA.CWDQtAfFv3QnUqN3up3J1bs32JVSKFPk', 'type': 'Allele', 'state': {'type': 'LiteralSequenceExpression', 'sequence': 'A'},
                     'location': {'_id': 'ga4gh:VSL.ixj_LC0E_4GQvm7dtG4r5gjf88lWRxU1', 'type': 'SequenceLocation',
                                  'interval': {'end': {'type': 'Number', 'value': 12346},
                                               'type': 'SequenceInterval',
                                               'start': {'type': 'Number', 'value': 12345}},
                                  'sequence_id': 'ga4gh:SQ.S_KjnFVz-FE7M0W6yoaUDgYxLPc1jyWU'}}})
]


db_to_cvc_example = [
    (1,{'origCoordSystem': '0-based interbase','seqType': 'DNA','allelicState': 'heterozygous','geneSymbol': 'GENE1',
        'hgncId': 123, 'refAllele': 'C', 'altAllele': 'A','chrom': '3', 'genomeBuild': 'GRCh38','start': 12345,'end': 12346,'sequenceId': 'NC_000001.10'})
]

@pytest.fixture(scope="module")
def database_example():
    return request_local_api()

@pytest.mark.parametrize("rowId, expected", row_example_1)
def test_getExample(database_example,rowId,expected):
    resp = database_example.getExample(rowId)
    assert resp == expected

@pytest.mark.parametrize("rowId, expected", db_to_cvc_example)
def test_db_to_cvc(database_example,rowId,expected):
    resp = database_example.db_to_cvc(rowId)
    assert resp == expected