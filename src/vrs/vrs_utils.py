from src.api.variation_norm_api import VarNormRestApi
from src.api.seqrepo_api import SeqRepoAPI
from typing import Union


class VrsTranslate:
    def __init__(self) -> None:
        """Initialize class with the API URL"""

        self.cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp = self.cn.dp
        self.tlr = self.cn.tlr
        self.var_norm_api = VarNormRestApi()

    def from_vrs_to_spdi(self, expression: Union[dict, object]) -> str:
        """
        Translates a Variant Representation Specification (VRS) expression to a SPDI expression.

        Args:
            expression (Union[dict, object]): The VRS expression to translate.

        Raises:
            ValueError: If an error occurs while translating the VRS expression to a SPDI expression.

        Returns:
            str: The SPDI expression.
        """
        try:
            if isinstance(expression, dict):
                vrs_dict = self.tlr.translate_from(expression, "vrs")
                return self.tlr.translate_to(vrs_dict, "spdi")[0]
            elif isinstance(expression, object):
                return self.tlr.translate_to(expression, "spdi")[0]
        except Exception:
            raise ValueError(
                f"An error occurred while translating the VRS expression '{expression}' to a SPDI expression."
            )
        
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
        except Exception:
            raise ValueError(
                f"An error occurred while translating the VRS expression '{expression}' to a HGVS expression."
            )

