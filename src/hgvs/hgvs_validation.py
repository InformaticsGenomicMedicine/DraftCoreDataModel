import argparse
import pandas as pd
import hgvs.parser
import hgvs.dataproviders.uta
import hgvs.validator
from hgvs.exceptions import HGVSError

def validate_hgvs_variants(hp,vr,hgvs_list):
    val_output = []

    for hgvs in hgvs_list:
        try:
            parsed_variant = hp.parse_hgvs_variant(hgvs)
            vr.validate(parsed_variant)
            val_output.append(True)
        except HGVSError as e:
            val_output.append(e) 
    
    return val_output

def main():
    parser = argparse.ArgumentParser(description="Validate HGVS expressions from an Excel, CSV, or tab-delimited file.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    parser.add_argument("example_column", help="Name of the column containing HGVS examples")

    args = parser.parse_args()

    hp = hgvs.parser.Parser()
    hdp = hgvs.dataproviders.uta.connect()
    vr = hgvs.validator.Validator(hdp=hdp)
    
# TODO: need to test that the files open up correctly
    try:
        input_data = pd.read_excel(args.input_file)
    except Exception:
        try:
            input_data = pd.read_csv(args.input_file, sep=None, engine="python")
        except Exception:
            try:
                input_data = pd.read_csv(args.input_file, sep="\t")
            except Exception:
                print("Error: Unsupported file format. Please provide an Excel, CSV, or tab-delimited file.")
                return

    input_data[args.example_column] = input_data[args.example_column].str.strip()

    data = pd.DataFrame(input_data)
    hgvs_expression = data[args.example_column]

    original_error_messages = validate_hgvs_variants(hp,vr,hgvs_expression)

    hgvs_results = {
        'HGVS': data[args.example_column],
        'biocommons_validator': original_error_messages
    }

    result = pd.DataFrame(hgvs_results)

    result.to_csv(args.output_file, index=False)

    print("Script execution completed.")

if __name__ == "__main__":
    main()
