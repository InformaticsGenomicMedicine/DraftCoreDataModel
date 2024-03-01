multiple_examples = [
    {
        "DeletionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/2085710/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "CC",
            "altAllele": "C",
            "start": 1014263,
            "end": 1014265,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000001.11",
        },
        "spdi": "NC_000001.11:1014263:CC:C",
        "hgvs": "NC_000001.11:g.1014265del",
        "vrs": {
            "_id": "ga4gh:VA.BmF3zr2l6XLpLaK8GInM6Q3Emc3JyPD3",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.i6Of9s2jVDuJ4vwU6sCeG-jT7ygmlfx6",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 1014263},
                    "end": {"type": "Number", "value": 1014265},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "C"},
        },
    },
    {
        "DeletionExample2": "https://www.ncbi.nlm.nih.gov/clinvar/variation/523496/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "GCATCG",
            "altAllele": "G",
            "start": 15445654,
            "end": 15445660,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000001.11",
        },
        "spdi": "NC_000001.11:15445654:GCATCG:G",
        "hgvs": "NC_000001.11:g.15445656_15445660del",
        "vrs": {
            "_id": "ga4gh:VA.5CfKpT5tErBj7PNtqdub7VOliwHEQLvs",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.z-j8mH9v1lJf-MsQosxg_8gtRA1zKhuE",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 15445654},
                    "end": {"type": "Number", "value": 15445660},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "G"},
        },
    },
    {
        "DeletionExample3": " https://www.ncbi.nlm.nih.gov/clinvar/variation/1062882/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "AG",
            "altAllele": "",
            "start": 1510945,
            "end": 1510947,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000016.10",
        },
        "spdi": "NC_000016.10:1510945:AG:",
        "hgvs": "NC_000016.10:g.1510946_1510947del",
        "vrs": {
            "_id": "ga4gh:VA.BAzdGf6SGQgUBZCADrRGSS61qYzhDWgy",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.CFA82oReGyKLEaLcmWDyzOkd3L8nhvDV",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.yC_0RBj3fgBlvgyAuycbzdubtLxq-rE0",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 1510945},
                    "end": {"type": "Number", "value": 1510947},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": ""},
        },
    },
    {
        "InsertionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/1344775/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "",
            "altAllele": "ATA",
            "start": 113901365,
            "end": 113901365,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000001.11",
        },
        "spdi": "NC_000001.11:113901365::ATA",
        "hgvs": "NC_000001.11:g.113901365_113901366insATA",
        "vrs": {
            "_id": "ga4gh:VA.J9BMdktHGGjE843oD0T_bwUV6WxojkCW",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.TMxdXtmi4ctcTRipHMD6py1Nv1kLMyJd",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 113901365},
                    "end": {"type": "Number", "value": 113901365},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "ATA"},
        },
    },
    {
        "InsertionExample2": " https://www.ncbi.nlm.nih.gov/clinvar/variation/930317/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "",
            "altAllele": "CGTTCTCTACCAGCTGC",
            "start": 134824705,
            "end": 134824705,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000009.12",
        },
        "spdi": "NC_000009.12:134824705::CGTTCTCTACCAGCTGC",
        "hgvs": "NC_000009.12:g.134824705_134824706insCGTTCTCTACCAGCTGC",
        "vrs": {
            "_id": "ga4gh:VA.kYmgdh3e7fpUwGCaxo2evZ3Jjvi_D8d6",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.2mzp0ihod6GjiSeFVdPRNWdGjX6NGhnZ",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.KEO-4XBcm1cxeo_DIQ8_ofqGUkp4iZhI",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 134824705},
                    "end": {"type": "Number", "value": 134824705},
                },
            },
            "state": {
                "type": "LiteralSequenceExpression",
                "sequence": "CGTTCTCTACCAGCTGC",
            },
        },
    },
    {
        "SubstitutionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/835613/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "C",
            "altAllele": "T",
            "start": 27453448,
            "end": 27453449,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000002.12",
        },
        "spdi": "NC_000002.12:27453448:C:T",
        "hgvs": "NC_000002.12:g.27453449C>T",
        "vrs": {
            "_id": "ga4gh:VA.fXvhngewkkyVwzEeSJRr5tro8Jcol6Q-",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.nLMbYalHO4OEI2axqkyTMCQxrH98UpDN",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.pnAqCRBrTsUoBghSD1yp_jXWSmlbdh4g",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 27453448},
                    "end": {"type": "Number", "value": 27453449},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    },
    {
        "SubstitutionExample2": " https://www.ncbi.nlm.nih.gov/clinvar/variation/217604/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "A",
            "altAllele": "T",
            "start": 15560606,
            "end": 15560607,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000004.12",
        },
        "spdi": "NC_000004.12:15560606:A:T",
        "hgvs": "NC_000004.12:g.15560607A>T",
        "vrs": {
            "_id": "ga4gh:VA.0yUR6mNfhWuFw3M72v1Mq3L_ab_crMUY",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.TVHFkYX90WBQK8YT_skSCg5VOscVFJLq",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.HxuclGHh0XCDuF8x6yQrpHUBL7ZntAHc",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 15560606},
                    "end": {"type": "Number", "value": 15560607},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "T"},
        },
    },
    {
        "InsertionDeletionExample1": "https://www.ncbi.nlm.nih.gov/clinvar/variation/931239/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "CA",
            "altAllele": "GAT",
            "start": 166043788,
            "end": 166043790,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000002.12",
        },
        "spdi": "NC_000002.12:166043788:CA:GAT",
        "hgvs": "NC_000002.12:g.166043789_166043790delinsGAT",
        "vrs": {
            "_id": "ga4gh:VA.I0biXWOvxxmy4jjxsMqQVgy0Q91CJY7x",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.E3BkYwqHo3ETPtXyM_oAzzcpbb07zJ3W",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.pnAqCRBrTsUoBghSD1yp_jXWSmlbdh4g",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 166043788},
                    "end": {"type": "Number", "value": 166043790},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "GAT"},
        },
    },
    {
        "InsertionDeletionExample2": "https://www.ncbi.nlm.nih.gov/clinvar/variation/931057/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "A",
            "altAllele": "CC",
            "start": 8058795,
            "end": 8058796,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000010.11",
        },
        "spdi": "NC_000010.11:8058795:A:CC",
        "hgvs": "NC_000010.11:g.8058796delinsCC",
        "vrs": {
            "_id": "ga4gh:VA.wL7Fbskfd2IVJwlboN3Rt_8C6_x4r8sy",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.SYp0Ombl1XpgwsKEQFYgKbE9KgoV9SUL",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.ss8r_wB0-b9r44TQTMmVTI92884QvBiB",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 8058795},
                    "end": {"type": "Number", "value": 8058796},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "CC"},
        },
    },
    {
        "IdentityExample": "https://www.ncbi.nlm.nih.gov/snp/rs1805044#hgvs_tab",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "G",
            "altAllele": "G",
            "start": 88007815,
            "end": 88007816,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000004.12",
        },
        "spdi": "NC_000004.12:88007815:G:G",
        "hgvs": "NC_000004.12:g.88007816=",
        "vrs": {
            "_id": "ga4gh:VA.eT7IpRxd5CiyJEq8sE6AgobdwgY62NxG",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.Iud8aOpjNALanhgWtq1sU6aQE5uK4ywU",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.HxuclGHh0XCDuF8x6yQrpHUBL7ZntAHc",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 88007815},
                    "end": {"type": "Number", "value": 88007816},
                },
            },
            "state": {"type": "LiteralSequenceExpression", "sequence": "G"},
        },
    },
    {
        "DuplicationExample": "https://www.ncbi.nlm.nih.gov/clinvar/variation/1297092/",
        "cvc": {
            "origCoordSystem": "0-based interbase",
            "seqType": "DNA",
            "refAllele": "TGAGCTTCCA",
            "altAllele": "TGAGCTTCCATGAGCTTCCA",
            "start": 5880117,
            "end": 5880127,
            "allelicState": None,
            "geneSymbol": None,
            "hgncId": None,
            "chrom": None,
            "genomeBuild": None,
            "sequenceId": "NC_000001.11",
        },
        "spdi": "NC_000001.11:5880117:TGAGCTTCCA:TGAGCTTCCATGAGCTTCCA",
        "hgvs": "NC_000001.11:g.5880118_5880127dup",
        "vrs": {
            "_id": "ga4gh:VA.OpO3jwlmnhvpmEs2v9orWvMIa7UPb1To",
            "type": "Allele",
            "location": {
                "_id": "ga4gh:VSL.veKlh4sQPAIr1HNoqjmsm7qZa0FNfjI9",
                "type": "SequenceLocation",
                "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
                "interval": {
                    "type": "SequenceInterval",
                    "start": {"type": "Number", "value": 5880117},
                    "end": {"type": "Number", "value": 5880127},
                },
            },
            "state": {
                "type": "LiteralSequenceExpression",
                "sequence": "TGAGCTTCCATGAGCTTCCA",
            },
        },
    }
    # Add more examples as needed
]
