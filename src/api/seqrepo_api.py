from ga4gh.vrs.dataproxy import SeqRepoRESTDataProxy
from ga4gh.vrs.extras.translator import Translator
import configparser

class SeqRepoAPI:
    # SEQREPO_URL = "https://services.genomicmedlab.org/seqrepo"

    def __init__(self, seqrepo_rest_service_url: str = None) -> None:
        """Initialize the SeqRepoAPI instance with the specified SeqRepo REST service URL.

        Args:
            seqrepo_rest_service_url (str): The base URL of the SeqRepo REST service.

        Attributes:
            seqrepo_data_proxy (ga4gh.vrs.dataproxy.SeqRepoRESTDataProxy): The data proxy for SeqRepoRESTData.
                It allows retrieval of genomic sequence data.
            tlr (ga4gh.vrs.extras.translator.Translator): The translator for handling genomic variations.
                It provides functionalities such as translation, normalization, and identification.
        """

        self.url = "https://services.genomicmedlab.org/seqrepo"
        self.seqrepo_rest_service_url = seqrepo_rest_service_url or self.url 
        self.seqrepo_data_proxy = SeqRepoRESTDataProxy(base_url=self.seqrepo_rest_service_url)
        self.tlr = Translator(
            data_proxy=self.seqrepo_data_proxy,
            translate_sequence_identifiers=True,
            normalize=True,
            identify=True,
        )
