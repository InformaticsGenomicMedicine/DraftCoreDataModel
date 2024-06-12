#TODO: add data to database

# NO URL
snv = {
    "hgvs": "NC_000019.10:g.44908822C>T",
    "spdi": "NC_000019.10:44908821:1:T",
}

# URL: https://www.ncbi.nlm.nih.gov/clinvar/variation/1373966/?new_evidence=true
deletion_inputs = {
    "hgvs": "NC_000013.11:g.20003097del",
    "spdi": ["NC_000013.11:20003096:C:", "NC_000013.11:20003096:1:"]
}
# URL: # https://www.ncbi.nlm.nih.gov/clinvar/variation/1687427/?new_evidence=true
insertion_inputs = {
    "hgvs": "NC_000013.11:g.20003010_20003011insG",
    "spdi": ["NC_000013.11:20003010::G", "NC_000013.11:20003010:0:G"]
}
# https://www.ncbi.nlm.nih.gov/clinvar/variation/1264314/?new_evidence=true
duplication_inputs = {
    "hgvs": "NC_000013.11:g.19993838_19993839dup",
    "spdi": "NC_000013.11:19993837:GT:GTGT"
}
# NO URL
hgvs_examples = (
    "NC_000013.11:g.32936732=",
    "NC_000007.14:g.55181320A>T",
    "NC_000007.14:g.55181220del",
    "NC_000007.14:g.55181230_55181231insGGCT",
    "NC_000013.11:g.32331093_32331094dup",
    "NC_000013.11:g.32316467dup",
    "NM_001331029.1:n.872A>G",
    "NM_181798.1:n.1263G>T"
)