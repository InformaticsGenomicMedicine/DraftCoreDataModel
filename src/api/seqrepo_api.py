from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator


class SeqRepoAPI:
    def __init__(self, seqrepo_rest_service_url: str) -> None:
        """Initialize the SeqRepoAPI instance with the specified SeqRepo REST service URL.

        Args:
            seqrepo_rest_service_url (str): The base URL of the SeqRepo REST service.
            
        Attributes:
            dp (ga4gh.vrs.dataproxy.SeqRepoRESTDataProxy): The data proxy for SeqRepoRESTData.
                It allows retrieval of genomic sequence data.
            tlr (ga4gh.vrs.extras.translator.Translator): The translator for handling genomic variations.
                It provides functionalities such as translation, normalization, and identification.
        """
        self.seqrepo_rest_service_url = seqrepo_rest_service_url
        self.dp = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(
            data_proxy=self.dp,
            translate_sequence_identifiers=True,
            normalize=True,
            identify=True,
        )
