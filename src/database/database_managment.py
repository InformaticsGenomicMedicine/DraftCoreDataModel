import sqlite3
import json


class DatabaseManager:
    def __init__(self, db_file="data.db"):
        self.db_file = db_file

    def create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            create_table = """
            CREATE TABLE IF NOT EXISTS Variations (
              id INTEGER PRIMARY KEY,
              example_name TEXT,
              variant_url TEXT,
              spdi TEXT,
              hgvs TEXT,
              vrs TEXT,
              cvc TEXT
            )
            """
            cur.execute(create_table)

    def insert_row(self, example):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            name = example["example_name"]
            url = example["variant_url"]
            spdi = example["spdi"]
            hgvs = example["hgvs"]
            vrs = json.dumps(example["vrs"])
            cvc = json.dumps(example["cvc"])

            try:
                cur.execute(
                    "INSERT INTO Variations (example_name, variant_url, spdi, hgvs, vrs, cvc) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, url, spdi, hgvs, vrs, cvc),
                )
            except sqlite3.Error as e:
                print(f"An error occurred: {str(e)}")

    def insert_data(self, data):
        for example in data:
            self.insert_row(example)

    def delete_row(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            try:
                cur.execute("DELETE FROM Variations WHERE id = ?", (id,))
                if cur.rowcount == 0:
                    print(f"No row with ID {id} found.")
            except sqlite3.Error as e:
                print(f"An error occurred: {str(e)}")

    def get_row(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            try:
                cur.execute("SELECT * FROM Variations WHERE id = ?", (id,))
                return cur.fetchone()
            except sqlite3.Error as e:
                print(f"An error occurred: {str(e)}")

    def update_row(self, id, example):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            name = example["example_name"]
            url = example["variant_url"]
            spdi = example["spdi"]
            hgvs = example["hgvs"]
            vrs = json.dumps(example["vrs"])
            cvc = json.dumps(example["cvc"])

            try:
                cur.execute(
                    "UPDATE Variations SET example_name = ?, variant_url = ?, spdi = ?, hgvs = ?, vrs = ?, cvc = ? WHERE id = ?",
                    (name, url, spdi, hgvs, vrs, cvc, id),
                )
            except sqlite3.Error as e:
                print(f"An error occurred: {str(e)}")

    def get_all_rows(self):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            try:
                cur.execute("SELECT * FROM VARIATIONS")
                return cur.fetchall()
            except sqlite3.Error as e:
                print(f"An error occurred: {str(e)}")

    def get_specific_columns(self, id, columns):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            try:
                cur.execute(
                    f"SELECT {', '.join(columns)} FROM Variations WHERE id = ?", (id,)
                )
                return cur.fetchone()
            except sqlite3.Error as e:
                print(f"An error occurred: {str(e)}")


# Example usage:
if __name__ == "__main__":
    from data import multiple_examples  # Assuming you have your data in rawdata.py

    db_manager = DatabaseManager(db_file="test.db")
    # db_manager.create_table()  # Ensure table is created before any other operations
    # db_manager.insert_data(multiple_examples)  # Insert multiple rows

    # # Insert a single row
    # single_example = {
    #     "example_name": "Deletion",
    #     "variant_url": "https://example.com/variants/1",
    #     "spdi": "test1",
    #     "hgvs": "test2",
    #     "vrs": {"ref": "G", "alt": ""},
    #     "cvc": {"start": 1000000, "length": 1, "type": "DEL"},
    # }
    # db_manager.insert_row(single_example)

    # db_manager.delete_row(12)  # Delete the row with id 1
    a = db_manager.get_specific_columns(5, ["cvc"])
    print(a)
    # print(json.loads(a[0]))


# {
#     "metadata": {
#         "description": "This is a collection of examples of variants in different formats",
#         "technique": "This is a test data for the database",
#     }, # optional, can be used to store metadata
#     "example_data": [
#         {
#             "example_name": "Deletion", # required, name of the example
#             "source_url": "https://www.ncbi.nlm.nih.gov/clinvar/variation/2085710/", # optional, URL to the variant
#             "spdi": {
#                 "version": "1.0", # Key represents the version and the key represent the string of the variant
#                 "expression": "NC_000001.11:1014263:CC:C"
#             },
#             "hgvs": {
#                 "version": "1.0", # Key represents the version and the key represent the string of the variant
#                 "expression": "NC_000001.11:g.1014265del"
#             },
#             "vrs": {
#                 "version": "1.3", # Key represents the version and the key represent the string of the variant,
#                 "expression": {
#             "_id": "ga4gh:VA.BmF3zr2l6XLpLaK8GInM6Q3Emc3JyPD3",
#             "type": "Allele",
#             "location": {
#                 "_id": "ga4gh:VSL.i6Of9s2jVDuJ4vwU6sCeG-jT7ygmlfx6",
#                 "type": "SequenceLocation",
#                 "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
#                 "interval": {
#                     "type": "SequenceInterval",
#                     "start": {"type": "Number", "value": 1014263},
#                     "end": {"type": "Number", "value": 1014265},
#                 },
#             },
#             "state": {"type": "LiteralSequenceExpression", "sequence": "C"},
#         }
#             },
#             "cvc": {
#                 "version": "1.0", # Key represents the version and the key represent the string of the variant
#                 "expression": {
#             "origCoordSystem": "0-based interbase",
#             "seqType": "DNA",
#             "refAllele": "CC",
#             "altAllele": "C",
#             "start": 1014263,
#             "end": 1014265,
#             "allelicState": None,
#             "geneSymbol": None,
#             "hgncId": None,
#             "chrom": None,
#             "genomeBuild": None,
#             "sequenceId": "NC_000001.11",
#         }
#             },
#             "phir" : {
#                 "version": "" # Key represents the version and the key represent the string of the variant
#             }
#         }
#     ]
# }


# {
#     "metadata": {
#         "description": "This is a collection of examples of variants in different formats",
#         "technique": "This is a test data for the database"
#     },
#     "example_data": [
#         {
#             "example_name": "Deletion",
#             "source_url": "https://www.ncbi.nlm.nih.gov/clinvar/variation/2085710/",
#             "spdi": {
#                 "version": "1.0",
#                 "expression": "NC_000001.11:1014263:CC:C"
#             },
#             "hgvs": {
#                 "version": "1.0",
#                 "expression": "NC_000001.11:g.1014265del"
#             },
#             "vrs": [
#                 {
#                     "version": "1.3",
#                     "expression": {
#                         "_id": "ga4gh:VA.BmF3zr2l6XLpLaK8GInM6Q3Emc3JyPD3",
#                         "type": "Allele",
#                         "location": {
#                             "_id": "ga4gh:VSL.i6Of9s2jVDuJ4vwU6sCeG-jT7ygmlfx6",
#                             "type": "SequenceLocation",
#                             "sequence_id": "ga4gh:SQ.Ya6Rs7DHhDeg7YaOSg1EoNi3U_nQ9SvO",
#                             "interval": {
#                                 "type": "SequenceInterval",
#                                 "start": {"type": "Number", "value": 1014263},
#                                 "end": {"type": "Number", "value": 1014265}
#                             }
#                         },
#                         "state": {"type": "LiteralSequenceExpression", "sequence": "C"}
#                     }
#                 },
#                 {
#                     "version": "2.0",
#                     "expression": {
#                         // Provide expression for version 2.0 of vrs here
#                     }
#                 }
#             ],
#             "cvc": [
#                 {
#                     "version": "1.0",
#                     "expression": {
#                         "origCoordSystem": "0-based interbase",
#                         "seqType": "DNA",
#                         "refAllele": "CC",
#                         "altAllele": "C",
#                         "start": 1014263,
#                         "end": 1014265,
#                         "allelicState": null,
#                         "geneSymbol": null,
#                         "hgncId": null,
#                         "chrom": null,
#                         "genomeBuild": null,
#                         "sequenceId": "NC_000001.11"
#                     }
#                 },
#                 {
#                     "version": "2.0",
#                     "expression": {
#                         // Provide expression for version 2.0 of cvc here
#                     }
#                 }
#             ],
#             "phir": [
#                 {
#                     "version": "", // No expression provided for this version
#                 },
#                 {
#                     "version": "2.0",
#                     "expression": {
#                         // Provide expression for version 2.0 of phir here
#                     }
#                 }
#             ]
#         }
#     ]
# }


# CREATE TABLE Examples (
#     example_id INTEGER PRIMARY KEY,
#     example_name TEXT,
#     description TEXT,
#     technique TEXT,
#     source_url TEXT
# );

# CREATE TABLE Variants (
#     variant_id INTEGER PRIMARY KEY,
#     example_id INTEGER,
#     variant_type TEXT,
#     version TEXT,
#     expression TEXT,
#     FOREIGN KEY (example_id) REFERENCES Examples(example_id)
# );