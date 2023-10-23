from src.api.ncbi_variation_services_api import VarServAPI
class SPDI:

    def __init__(self,sequence: str, position: int, deletion: str, insertion: str):
        """Initialize SPDI object.

        Args:
            sequence (str): The sequence identifier.
            position (int): The starting position of the variation.
            deletion (str): The deleted sequence.
            insertion (str): The inserted sequence.

        Raises:
            SPDIValidationException: If there is an issue validating the SPDI expression.
        """
        self.sequence = sequence
        self.position = position
        self.deletion = deletion
        self.insertion = insertion
        self.api = VarServAPI()

        spdi = f"{sequence}:{position}:{deletion}:{insertion}"
        # TODO: test new method
        self.api.validate_spdi(spdi)
        # TODO: delete after testing
        # try:
        #     self.api.validate_spdi(spdi)
        # except Exception as e:
        #     raise e

    def to_string(self) -> str:
        """Convert SPDI object to a string representation.

        Returns:
            str: The string representation of the SPDI object.
        """
        spdi_expression = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        return spdi_expression 

    def to_dict(self) -> dict:
        """Convert SPDI object to a dictionary.

        Returns:
            dict: A dictionary representation of the SPDI object.
        """
        return {
            'sequence': self.sequence,
            'position':self.position,
            'deletion': self.deletion,
            'insertion': self.insertion
        }