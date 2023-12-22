from bioutils.normalize import normalize, NormalizationMode
from ga4gh.vrs.dataproxy import SequenceProxy
from src.api.seqrepo_api import SeqRepoAPI
from src.spdi.spdi_class import SPDI

#TODO: documentation for this class
class VocaNormalizeSpdi:

    def __init__(self):
        self.cn = SeqRepoAPI("https://services.genomicmedlab.org/seqrepo")
        self.dp = self.cn.dp   

    def spdi_voca_normalize(self, expression: str) -> str:

        if isinstance(expression, str):
            sequence,position,deletion,insertion = expression.split(":")
            expression = SPDI(sequence,position,deletion,insertion)

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
            interval, new_allele = normalize(sequence,
                                    interval=(start_pos, end_pos), 
                                    alleles=(None, expression.insertion),
                                    bounds=(0, len(sequence)),
                                    mode=NormalizationMode.EXPAND,
                                    )
        
            expression.position = interval[0]
            expression.deletion = new_allele[0]
            expression.insertion = new_allele[1]

        except ValueError as e:
            return(f"Normalization failed: {e}")

        return str(expression)
