// Literal Expression

// HGVS expression: NC_000001.11:g.943043C>T

//VRS
{
	"_id": "ga4gh:VA.s8vzlmFv83fcoJnNovFkp4pnE48weUh4",
	"type": "Allele",
	"location": {
		"_id": "ga4gh:VSL.2tX8CXXY1z3HcbrXdGGTbmuqmYgNks6G",
		"type": "SequenceLocation",
		"sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
		"interval": {
			"type": "SequenceInterval",
			"start": {
				"type": "Number",
				"value": 943042
			},
			"end": {
				"type": "Number",
				"value": 943043
			}
		}
	},
	"state": {
		"type": "LiteralSequenceExpression",
		"sequence": "T"
	}
}

//FHIR
{
	"resourceType": "MolecularSequence",
	"id": "VRS_example_literal_1",
	"identifier": {
		"value": "ga4gh:VA.s8vzlmFv83fcoJnNovFkp4pnE48weUh4" //VRS ID
	},
	"type": "dna", //VRS does not convey the Type (loss in translation): This was pulled from the reference sequence of hgvs.
	"literal": [
		{
			"sequenceValue": "T" //VRS literal sequence expression 
		}
	]
}