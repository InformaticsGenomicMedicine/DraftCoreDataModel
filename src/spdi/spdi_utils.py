from src.api.ncbi_variation_services_api import VarServAPI
from src.api.seqrepo_api import SeqRepoAPI

import hgvs.parser
import json
from typing import Union


class SPDITranslate:
    def __init__(self) -> None:

        self.cn: SeqRepoAPI = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp: str = self.cn.dp
        self.tlr: str = self.cn.tlr
        self.var_serv_api: VarServAPI = VarServAPI()
        self.hp: hgvs.parser.Parser = hgvs.parser.Parser()

    def from_spdi_to_rightshift_hgvs(
        self, expression: str, validate: bool = True, output_format: str = "string"
    ) -> Union[str, hgvs.parser.ParserResult]:
        """Translate SPDI expression to right-shift HGVS expression using NCBI API.

        Args:
            expression (str): SPDI expression.
            validate (bool, optional): Perform SPDI validation. Defaults to True.
            output_format (str, optional): Format the output as a string or parse it into an HGVS object.
                Defaults to 'string'.

        Returns:
            str or hgvs.parser.ParserResult: Right-shift normalized HGVS expression.

        Raises:
             ValueError: If validation fails or there's an issue with the translation.
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
        except Exception:
            raise ValueError(
                f"An error occurred while translating the SPDI expression '{expression}' to a right-shift HGVS expression."
            )

    def from_spdi_to_vrs(
        self, expression: str, validate: bool = True, output_format: str = "obj"
    ) -> Union[object, dict, str]:
        """Translate SPDI expression to VRS expression.

        Args:
            expression (str): SPDI expression
            validate (bool, optional): Perform SPDI validation. Defaults to True.
            format_output (str, optional): Output format ('obj', 'dict', 'json'). Defaults to 'obj'.

        Returns:
            object or dict or str: Translated VRS expression.

        Raises:
            ValueError: If validation fails or there's an issue with the translation.
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
