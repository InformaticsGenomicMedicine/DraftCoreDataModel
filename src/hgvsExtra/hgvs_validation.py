import argparse
import pandas as pd
import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator
from hgvs.exceptions import HGVSError

class HGVSValidator:
    def __init__(self, input_file, output_file, example_column, human_curated):
        self.input_file = input_file
        self.output_file = output_file
        self.example_column = example_column
        self.human_curated = human_curated

        self.hp = hgvs.parser.Parser()
        self.hdp = hgvs.dataproviders.uta.connect()
        self.vr = hgvs.validator.Validator(hdp=self.hdp)

    def _validate_hgvs_variants(self, hgvsExpressions):
        validate_results = []
        error_messages = []

        for hgvs in hgvsExpressions:
            try:
                if isinstance(hgvs, str):
                    parsed_variant = self.hp.parse_hgvs_variant(hgvs)
                    self.vr.validate(parsed_variant)
                    validate_results.append('pass')
                    error_messages.append('')
                else:
                    validate_results.append('fail')
                    error_messages.append('')
            except HGVSError as e:
                validate_results.append('fail')
                error_messages.append(e)
        return validate_results, error_messages
    
    def process_data(self):
        if self.input_file.lower().endswith('.xlsx'):
            try:
                input_data = pd.read_excel(self.input_file, engine='openpyxl')
            except pd.errors.ParserError:
                print("Error: Unable to read the Excel file.")
                return
        elif self.input_file.lower().endswith('.csv'):
            try:
                input_data = pd.read_csv(self.input_file, sep=",")
            except pd.errors.ParserError:
                print("Error: Unable to read the CSV file.")
                return
        else:
            print("Unsupported file format. Provide an Excel (XLSX) or CSV file.")
            return

        input_data[self.example_column] = input_data[self.example_column].str.strip()
        hgvsExamples = input_data[self.example_column]
        validate_results, error_messages = self._validate_hgvs_variants(hgvsExamples)

        hgvs_results = {
            'HGVS': hgvsExamples,
            'human_curated_expecated_pass_fail': input_data[self.human_curated],
            'hgvs_validation_pass_fail': validate_results,
            'error_message': error_messages
        }

        result_df = pd.DataFrame(hgvs_results)
        result_df.to_csv(self.output_file, index=False)

        print("Script execution completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate HGVS expressions from an Excel or CSV file.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    parser.add_argument("example_column", help="Name of the column containing HGVS examples")
    parser.add_argument('human_curated', help='Name of the column containing human curated results')

    args = parser.parse_args()

    hgvs_validator = HGVSValidator(args.input_file, args.output_file, args.example_column, args.human_curated)
    hgvs_validator.process_data()

