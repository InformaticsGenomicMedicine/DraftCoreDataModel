multiple_examples = [
    {
        'InsertionExample':'https://www.ncbi.nlm.nih.gov/clinvar/variation/1344775/',
        'cvc': {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "",
            "altAllele": "ATA",
            "start": 113901365,
            "end": 113901365,
            "allelicState": None,
            "geneSymbol": 'AP4B1',
            "hgncId": None,
            "chrom": 'chr 1',
            "genomeBuild": 'GRCh38',
            "sequenceId": "NC_000001.11",
        },
        'spdi': 'NC_000001.11:113901365::ATA',
        'hgvs': 'NC_000001.11:g.113901365_113901365insATA',
        'vrs': {
            "_id": "ga4gh:VA.J9BMdktHGGjE843oD0T_bwUV6WxojkCW",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.TMxdXtmi4ctcTRipHMD6py1Nv1kLMyJd",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 113901365},
                    "end": {"type": "Number", "value": 113901365}
                }
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "ATA"}
        }
    },
    {
        'SubstitutionExample': 'https://www.ncbi.nlm.nih.gov/clinvar/variation/835613/',
        'cvc': {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "C",
            "altAllele": "T",
            "start": 27453448,
            "end": 27453449,
            "allelicState": None,
            "geneSymbol": 'IFT172',
            "hgncId": None,
            "chrom": 'chr 2',
            "genomeBuild": 'GRCh38',
            "sequenceId": "NC_000002.12",
        },
        'spdi': 'NC_000002.12:27453449:C:T',
        'hgvs': 'NC_000002.12:g.27453449C>T',
        'vrs': {
            '_id': 'ga4gh:VA.fXvhngewkkyVwzEeSJRr5tro8Jcol6Q-',
            'type': 'Allele',
            'location': {
                '_id': 'ga4gh:VSL.nLMbYalHO4OEI2axqkyTMCQxrH98UpDN',
                'type': 'SequenceLocation',
                'sequence_id': 'ga4gh:SQ.pnAqCRBrTsUoBghSD1yp_jXWSmlbdh4g',
                'interval': {
                    'type': 'SequenceInterval',
                    'start': {'type': 'Number', 'value': 27453448},
                    'end': {'type': 'Number', 'value': 27453449}
                }
            },
            'state': {'type': 'LiteralSequenceExpression', 'sequence': 'T'}
        }
    }
    # Add more examples as needed
]
