import argparse
import pandas as pd
import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator
from hgvs.exceptions import HGVSError

class HGVSValidator:
    def __init__(self,input_file,output_file,example_column):
        self.input_file = input_file
        self.output_file = output_file
        self.example_column = example_column

        self.hp = hgvs.parser.Parser()
        self.hdp = hgvs.dataproviders.uta.connect()
        self.vr = hgvs.validator.Validator(hdp=self.hdp)

    def _validate_hgvs_variants(self,hgvsExpressions):
        validated_results = []

        for hgvs in hgvsExpressions:
            try:
                if isinstance(hgvs, str):
                    parsed_variant = self.hp.parse_hgvs_variant(hgvs)
                    self.vr.validate(parsed_variant)
                    validated_results.append(True)
                else:
                    validated_results.append(False)
            except HGVSError as e:
                validated_results.append(e)
                
        return validated_results
    
    def load_data(self):
        try:
            input_data = pd.read_excel(self.input_file)
        except Exception:
            try:
                input_data = pd.read_csv(self.input_file, sep=",")
            except Exception:
                print("Error: Unsupported file format. Please provide an Excel or CSV file.")
        
        return input_data 
    
    def validation_results(self,input_data):
        
        input_data[self.example_column] = input_data[self.example_column].str.strip()
        hgvsExamples = input_data[self.example_column]
        validation_results = self._validate_hgvs_variants(hgvsExamples)

        hgvs_results = {
            'HGVS': hgvsExamples,
            'Validator': validation_results
        }

        result_df = pd.DataFrame(hgvs_results)
        result_df.to_csv(self.output_file, index=False)

        print("Script execution completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate HGVS expressions from an Excel or CSV file.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    parser.add_argument("example_column", help="Name of the column containing HGVS examples")

    args = parser.parse_args()

    hgvs_validator = HGVSValidator(args.input_file,args.output_file,args.example_column)
    data = hgvs_validator.load_data()
    hgvs_validator.validation_results(data)