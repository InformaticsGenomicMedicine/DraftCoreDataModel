from src.api.variation_norm_api import VarNormRestApi
from src.api.seqrepo_api import SeqRepoAPI
from src.api.ncbi_variation_services_api import VarServAPI
from typing import Union


class VrsTranslate:
    def __init__(self) -> None:
        """Initialize class with the API URL"""

        self.seqrepo_api = SeqRepoAPI()
        self.dp = self.seqrepo_api.seqrepo_dataproxy 
        self.tlr = self.seqrepo_api.tlr
        self.var_norm_api = VarNormRestApi()
        self.var_serv_api = VarServAPI()

    def from_vrs_to_spdi(self, expression: Union[dict, object],validate: bool = True) -> str:
        """
        Translates a Variant Representation Specification (VRS) expression to a SPDI expression.

        Args:
            expression (Union[dict, object]): The VRS expression to translate.
            validate (bool): If True, translates numerical deletion position into a nucleotide string in the SPDI expression.

        Raises:
            ValueError: If an error occurs while translating the VRS expression to a SPDI expression.

        Returns:
            str: The SPDI expression.
        """
        try:
            spdi_expr = None
            if isinstance(expression, dict):
                vrs_dict = self.tlr.translate_from(expression, "vrs")
                spdi_expr = self.tlr.translate_to(vrs_dict, "spdi")[0]
            elif isinstance(expression, object):
                spdi_expr = self.tlr.translate_to(expression, "spdi")[0]
            else:
                raise TypeError("Unsupported type for 'expression'. Must be 'dict' or 'object'.") 
            if validate:
                spdi_expr = self.var_serv_api.validate_spdi(spdi_expr)
            return spdi_expr
        except Exception as e:
            raise ValueError(
                f"An error occurred while translating the VRS expression '{expression}' to a SPDI expression. {e}"
            )
    #NOTE: This is currently not working because the variation normalizer returned the status code: 422.
    def from_vrs_to_normalize_hgvs(self, expression: Union[dict, object]) -> str:
        """
        Translates a Variant Representation Specification (VRS) expression to a normalized HGVS expression.

        Args:
            expression (Union[dict, object]): A VRS expression to be translated to a HGVS expression.

        Raises:
            ValueError: If an error occurs while translating the VRS expression to a HGVS expression.

        Returns:
            str: The normalized HGVS expression.
        """
        try:
            if isinstance(expression, dict):
                # if input is a dictionary need to convert it to a vrs object in order to translate it to a HGVS expression using variation normalizer
                vrs_object = self.tlr.translate_from(expression, "vrs")
                return self.var_norm_api.to_hgvs(vrs_object)[0]
            elif isinstance(expression, object):
                return self.var_norm_api.to_hgvs(expression)[0]
        except Exception as e:
            raise ValueError(
                f"An error occurred while translating the VRS expression '{expression}' to a HGVS expression. {e}"
            )

    def from_vrs_to_hgvs(self, expression: Union[dict, object]) -> str:
        """
        Translates a Variant Representation Specification (VRS) expression to a normalized HGVS expression.
        Using the trl.translate_to method to convert the VRS to HGVS. Different from the from_vrs_to_normalize_hgvs method.
        Because the from_vrs_to_normalize_hgvs method uses the variation normalizer to convert the VRS to HGVS.

        Args:
            expression (Union[dict, object]): A VRS expression to be translated to a HGVS expression.

        Raises:
            ValueError: If an error occurs while translating the VRS expression to a HGVS expression.

        Returns:
            str: The normalized HGVS expression.
        """
        try:
            if isinstance(expression, dict):
                # if input is a dictionary need to convert it to a vrs object in order to translate it to a HGVS expression using variation normalizer
                vrs_object = self.tlr.translate_from(expression, "vrs")
                return self.tlr.translate_to(vrs_object,'hgvs')[0]
            elif isinstance(expression, object):
                return self.tlr.translate_to(expression, "hgvs")[0]
        except Exception as e:
            raise ValueError(
                f"An error occurred while translating the VRS expression '{expression}' to a HGVS expression. {e}"
            ) 