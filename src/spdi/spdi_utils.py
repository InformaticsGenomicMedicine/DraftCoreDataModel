from src.api.ncbi_variation_services_api import VarServAPI
from src.api.seqrepo_api import SeqRepoAPI

import hgvs.parser
import json
from typing import Union


class SPDITranslate:
    def __init__(self) -> None:
        self.seqrepo_api = SeqRepoAPI()
        self.dp = self.seqrepo_api.seqrepo_data_proxy 
        self.tlr = self.seqrepo_api.tlr
        self.var_serv_api = VarServAPI()
        self.hp = hgvs.parser.Parser()

    def from_spdi_to_rightshift_hgvs(
            self, expression: str, validate: bool = True, output_format: str = "string"
        ):
        """ Translates a given SPDI expression to a right-shift HGVS expression. (Using NCBI API)

        Args:
            expression (str): The SPDI expression to be translated.
            validate (bool, optional): If True, the SPDI expression will be validated before translation. Defaults to True.
            output_format (str, optional): The format of the output. Supported values are 'string' or 'parse'. Defaults to "string".

        Raises:
            ValueError: If validate is not a boolean.
            ValueError: If output_format is not supported.

        Returns:
            str or hgvs.parser.ParserResult: The translated right-shift HGVS expression. If output_format is 'string', a string is returned. If output_format is 'parse', a hgvs.parser.ParserResult is returned.
            
        Raises:
            ValueError: If an error occurs while translating the SPDI expression to a right-shift HGVS expression.
        """
        
        if not isinstance(validate, bool):
            raise ValueError(
                f"Invalid value for 'validate': {validate}. Expected a boolean."
            )
        if output_format not in {"string", "parse"}:
            raise ValueError(
                f"Unsupported output_format: {output_format}. Supported values are 'string' or 'parse'."
            )

        try:
            if validate:
                spdi_expression = self.var_serv_api.validate_spdi(expression)
            else:
                spdi_expression = expression

            hgvs_expression = self.var_serv_api.spdi_to_hgvs(spdi_expression)

            if output_format == "string":
                return hgvs_expression
            elif output_format == "parse":
                return self.hp.parse_hgvs_variant(hgvs_expression)
        except Exception as e:
            raise ValueError(
                f"An error occurred while translating the SPDI expression '{expression}' to a right-shift HGVS expression: {e}"
            )

    def from_spdi_to_vrs(
            self, expression: str, validate: bool = True, output_format: str = "obj"
        ) -> Union[object, dict, str]:
        """ Translates an SPDI expression to a VRS expression.

        Args:
            expression (str): The SPDI expression to translate.
            validate (bool, optional): Whether to validate the SPDI expression before translating it. Defaults to True.
            output_format (str, optional): The format in which to return the VRS expression. Supported values are 'obj', 'dict', and 'json'. Defaults to "obj".

        Raises:
            ValueError: If validate is not a boolean.
            ValueError: If output_format is not one of 'obj', 'dict', or 'json'.
            ValueError: If an error occurs while translating the SPDI expression to a VRS expression.

        Returns:
            Union[object, dict, str]: The translated VRS expression. The format of the return value depends on the value of output_format.
        """
        if not isinstance(validate, bool):
            raise ValueError(
                f"Invalid value for 'validate': {validate}. Expected a boolean."
            )
        if output_format not in {"obj", "dict", "json"}:
            raise ValueError(
                f"Unsupported format_output: {output_format}. Supported values are 'obj', 'dict', and 'json'."
            )

        if validate:
            spdi_expression = self.var_serv_api.validate_spdi(expression)
        else:
            spdi_expression = expression

        try:
            vrs_expression = self.tlr.translate_from(spdi_expression, "spdi")

            if output_format == "obj":
                return vrs_expression
            elif output_format == "dict":
                return vrs_expression.as_dict()
            elif output_format == "json":
                return json.dumps(vrs_expression.as_dict())
        except Exception as e:
            raise ValueError(
                f"An error occurred while translating the SPDI expression '{spdi_expression}' to a VRS expression: {e}"
            )
