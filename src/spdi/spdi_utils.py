from src.api.ncbi_variation_services_api import VarServAPI
from src.api.seqrepo_api import SeqRepoAPI

import hgvs.parser
import json


class SPDITranslate:
    def __init__(self):

        self.cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp = self.cn.dp
        self.tlr = self.cn.tlr
        self.var_serv_api = VarServAPI()
        self.hp = hgvs.parser.Parser()

    def from_spdi_to_rightshift_hgvs(
        self, expression, validate=True, format_output="string"
    ):
        """Translate SPDI expression to right-shift HGVS expression using NCBI API.

        Args:
            expression (str): SPDI expression.
            validate (bool, optional): Perform SPDI validation. Defaults to True.
            format_output (bool, optional): Format the output as a string or parse it into an HGVS object.
                Defaults to True.

        Returns:
            str or hgvs.parser.ParserResult: Right-shift normalized HGVS expression.
        """
        # Raises:
        #     ValueError: If validation fails or there's an issue with the translation.

        if not isinstance(validate, bool):
            raise ValueError(
                f"Invalid value for 'validate': {validate}. Expected a boolean."
            )
        if format_output not in {"string", "parse"}:
            raise ValueError(
                f"Unsupported format_output: {format_output}. Supported values are string' or 'parse'."
            )

        try:
            if validate:
                spdi_expression = self.var_serv_api.validate_spdi(expression)
            else:
                spdi_expression = expression

            hgvs_expression = self.var_serv_api.spdi_to_hgvs(spdi_expression)

            if format_output == "string":
                return hgvs_expression
            else:
                return self.hp.parse_hgvs_variant(hgvs_expression)
        except Exception as e:
            return f"{e}. Expression Error: {spdi_expression}"
            # raise ValueError(f"{e}. Expression Error: {spdi_expression}")

    def from_spdi_to_vrs(self, expression, validate=True, format_output="obj"):
        """Translate SPDI expression to VRS expression.

        Args:
            expression (str): SPDI expression
            validate (bool, optional): Perform SPDI validation. Defaults to True.
            format_output (str, optional): Output format ('obj', 'dict', 'json'). Defaults to 'obj'.

        Returns:
            object or dict or str: Translated VRS expression.
        """

        # Raises:
        #     ValueError: If validation fails or there's an issue with the translation.

        if not isinstance(validate, bool):
            raise ValueError(
                f"Invalid value for 'validate': {validate}. Expected a boolean."
            )
        if format_output not in {"obj", "dict", "json"}:
            raise ValueError(
                f"Unsupported format_output: {format_output}. Supported values are 'obj', 'dict', and 'json'."
            )

        if validate:
            spdi_expression = self.var_serv_api.validate_spdi(expression)
        else:
            spdi_expression = expression

        try:
            vrs_expression = self.tlr.translate_from(spdi_expression, "spdi")

            if format_output == "obj":
                return vrs_expression
            elif format_output == "dict":
                return vrs_expression.as_dict()
            elif format_output == "json":
                return json.dumps(vrs_expression.as_dict())
        except Exception as e:
            return f"{e}. Expression Error: {spdi_expression}"
            # raise ValueError(f"{e}. Expression Error: {spdi_expression}")
