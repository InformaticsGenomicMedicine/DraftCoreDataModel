from bioutils.normalize import normalize, NormalizationMode
from ga4gh.vrs.dataproxy import SequenceProxy
from src.api.seqrepo_api import SeqRepoAPI
from src.spdi.spdi_class import SPDI
from typing import Union


class VocaNormalizeSpdi:
    """A class for normalizing SPDI expressions using the Voca normalization method."""

    def __init__(self):
        self.seqrepo_api = SeqRepoAPI()
        self.dp = self.seqrepo_api.seqrepo_data_proxy

    def spdi_voca_normalize(self, expression: Union[str, SPDI]) -> str:
        """Normalize SPDI expressions using the Voca normalization method.

        Args:
            expression (Union[str,SPDI]): Spdi expression in the form of "sequence:position:deletion:insertion" or SPDI object
        Returns:
            str: Normalized SPDI expression 
        """

        if isinstance(expression, str):
            sequence, position, deletion, insertion = expression.split(":")
            expression = SPDI(sequence, position, deletion, insertion)

        # capture the start and end position
        start_pos = int(expression.position)

        try:
            ref = int(expression.deletion)
        except ValueError:
            ref = len(expression.deletion)

        end_pos = start_pos + ref

        # capture the full Sequence
        sequence = SequenceProxy(self.dp, expression.sequence)
        # voca normalize using bioutils.normalize
        try:
            interval, new_allele = normalize(
                sequence,
                interval=(start_pos, end_pos),
                alleles=(None, expression.insertion),
                bounds=(0, len(sequence)),
                mode=NormalizationMode.EXPAND,
            )

            expression.position = interval[0]
            expression.deletion = new_allele[0]
            expression.insertion = new_allele[1]

        except ValueError as e:
            return f"Normalization failed: {e}. Check the SPDI input."

        return str(expression)
