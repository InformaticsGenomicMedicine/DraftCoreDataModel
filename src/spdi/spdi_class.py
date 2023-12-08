# import sys

# sys.path.append("..")
import re
from src.api.ncbi_variation_services_api import VarServAPI

class SPDI:
    sequence_prefix_map = {
        "NC_": "DNA",
        "NM_": "DNA",
        "NG_": "DNA",
        "NR_": "RNA",
        "NP_": "protein",
    }
    # IUPC nucleotide codes: https://www.bioinformatics.org/sms/iupac.html
    pattern = {
        "EMPTY": "^$",
        "DIGIT": r"^\d+$",
        "DNA": r"^[ACGTRYSWKMBDHVN]*$",
        "RNA": r"^[ACGU]*$",
        "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
    }

    def __init__(
        self, sequence: str, position: str, deletion: str, insertion: str
    ) -> None:
        """Initialize SPDI object.

        Args:
            sequence (str): The sequence identifier.
            position (int): The starting position of the variation.
            deletion (str): The deleted sequence.
            insertion (str): The inserted sequence.

        Raises:
            SPDIValidationException: If there is an issue validating the SPDI expression.
        """

        self.api = VarServAPI()
        self.sequence = self._validate_sequence(sequence)
        self.position = self._validate_position(position)  
        self.deletion = self._validate_deletion(deletion)
        self.insertion = self._validate_insertion(insertion)

        spdi = f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        self.api.validate_spdi(spdi)

    def _validate_sequence(self, sequence: str) -> str:
        """ Validates a given reference sequence.

        Args:
            sequence (str): The reference sequence to be validated.

        Raises:
            TypeError: If the reference sequence is not a string.
            ValueError: If the reference sequence prefix is not one of ["NC_", "NM_", "NG_", "NR_", "NP_"].

        Returns:
            str: The validated reference sequence.
        """
        if not isinstance(sequence, str):
            raise TypeError(f"Sequence must be a string, not {type(sequence)}")

        sequence_prefix = sequence[:3]
        if sequence_prefix not in self.sequence_prefix_map:
            raise ValueError(f"Invalid reference sequence prefix: {sequence_prefix}")
        return sequence
    
# TODO:Remove this code once the above code is tested 
# TODO: this need to handle strings so we need to use a regular expression. 
    # def _validate_position(self, position: int) -> int:
    #     """
    #     Validates the given position.

    #     Args:
    #         position (int): The position to validate.

    #     Raises:
    #         TypeError: If the position is not an integer.
    #         ValueError: If the position is less then 0.

    #     Returns:
    #         int: The validated position.
    #     """
    #     if not isinstance(position, int):
    #         raise TypeError(f"Position must be an integer, not {type(position)}")
    #     if position < 0:
    #         raise ValueError(f"Position must be greater than or equal to 0.")
    #     return position

    # need to match the reference sequence with the correct regular expression

    def _validate_position(self, position: str) -> str:

        if not re.match(self.pattern["DIGIT"], position):
            raise ValueError(f"Position must be an nonnegative integer value.")
        return position

    def _match_refseq_to_regex(self) -> str:
        """Matches the reference sequence with the correct regular expression.

        Raises:
            ValueError: If the sequence type is unknown.

        Returns:
            str: The sequence type.
        """
        sequence_prefix = self.sequence[:3]
        sequence_type = self.sequence_prefix_map.get(sequence_prefix)
        if sequence_type not in self.pattern:
            raise ValueError(f"Unknown sequence type: {sequence_type}")
        return sequence_type

    def _validate_deletion(self, deletion: str) -> str:
        """Validates the deletion sequence.

        Args:
            deletion (str): The deletion sequence to validate.

        Raises:
            ValueError: If the deletion sequence is invalid.

        Returns:
            str: The validated deletion sequence.
        """
        deletion = deletion.strip().upper()
        if re.match(self.pattern["EMPTY"], deletion, re.IGNORECASE):
            return ""
        if re.match(self.pattern["DIGIT"], deletion):
            return deletion

        sequence_type = self._match_refseq_to_regex()
        if isinstance(deletion, str):
            if not re.match(self.pattern[sequence_type], deletion):
                raise ValueError(
                    f"Invalid deletion sequence for {sequence_type} reference sequence"
                )
        return deletion

    def _validate_insertion(self, insertion: str) -> str:
        """Validates the insertion sequence.

        Args:
            insertion (str): The insertion sequence to validate.

        Raises:
            ValueError: If the insertion sequence is invalid.

        Returns:
            str: The validated insertion sequence.
        """
        insertion = insertion.strip().upper()
        if re.match(self.pattern["EMPTY"], insertion, re.IGNORECASE):
            return ""
        sequence_type = self._match_refseq_to_regex()
        if isinstance(insertion, str):
            if not re.match(self.pattern[sequence_type], insertion):
                raise ValueError(
                    f"Invalid insertion sequence for {sequence_type} reference sequence"
                )
        return insertion
    
    # TODO:Remove this code once the above code is tested 
    # def _validate_deletion(self, deletion):
    #     """
    #     Validates the deletion sequence for a given reference sequence.

    #     Args:
    #         deletion (str): The deletion sequence to be validated.

    #     Raises:
    #         ValueError: If the sequence type is unknown.
    #         ValueError: If the deletion sequence is invalid for a DNA reference sequence.
    #         ValueError: If the deletion sequence is invalid for an RNA reference sequence.
    #         ValueError: If the deletion sequence is invalid for a protein reference sequence.

    #     Returns:
    #         str: The validated deletion sequence.
    #     """
    #     sequence_prefix_map = {
    #         "NC_": "DNA",
    #         "NM_": "DNA",
    #         "NG_": "DNA",
    #         "NR_": "RNA",
    #         "NP_": "protein",
    #     }
    #     pat = {
    #         "emp_pat": "^$",
    #         "digit": r"^\d+$",
    #         "DNA": r"^[ACGTRYSWKMBDHVN]*$",
    #         "RNA": r"^[ACGU]*$",
    #         "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
    #     }

    #     if re.match(pat["emp_pat"], deletion, re.IGNORECASE):
    #         return ""

    #     if isinstance(deletion, str):
    #         sequence_prefix = self.sequence[:3]
    #         sequence_type = sequence_prefix_map.get(sequence_prefix)

    #         if sequence_type not in pat:
    #             raise ValueError(f"Unknown sequence type: {sequence_type}")

    #         deletion = deletion.strip().upper()

    #         if re.match(pat["digit"], deletion):
    #             return deletion

    #         if sequence_type == "DNA":
    #             if not re.match(pat["DNA"], deletion):
    #                 raise ValueError(
    #                     f"Invalid deletion sequence for DNA reference sequence."
    #                 )
    #         elif sequence_type == "RNA":
    #             if not re.match(pat["RNA"], deletion):
    #                 raise ValueError(
    #                     f"Invalid deletion sequence for RNA reference sequence."
    #                 )
    #         elif sequence_type == "protein":
    #             if not re.match(pat["protein"], deletion):
    #                 raise ValueError(
    #                     f"Invalid deletion sequence for protein reference sequence."
    #                 )
    #         return deletion

    # def _validate_insertion(self, insertion: str) -> None:
    #     """Validates the insertion sequence for the reference sequence.

    #     Args:
    #         insertion (str): The insertion sequence to be validated.

    #     Raises:
    #         ValueError: If the sequence type is unknown.
    #         ValueError: If the insertion sequence is invalid for a DNA reference sequence.
    #         ValueError: If the insertion sequence is invalid for an RNA reference sequence.
    #         ValueError: If the insertion sequence is invalid for a protein reference sequence.

    #     Returns:
    #         str: The validated insertion sequence.
    #     """
    #     sequence_prefix_map = {
    #         "NC_": "DNA",
    #         "NM_": "DNA",
    #         "NG_": "DNA",
    #         "NR_": "RNA",
    #         "NP_": "protein",
    #     }
    #     pat = {
    #         "emp_pat": "^$",
    #         "DNA": r"^[ACGTRYSWKMBDHVN]*$",
    #         "RNA": r"^[ACGU]*$",
    #         "protein": r"^[ACDEFGHIKLMNPQRSTVWY]*$",
    #     }

    #     if re.match(pat["emp_pat"], insertion, re.IGNORECASE):
    #         return ""

    #     sequence_prefix = self.sequence[:3]
    #     sequence_type = sequence_prefix_map.get(sequence_prefix)

    #     if sequence_type not in pat:
    #         raise ValueError(f"Unknown sequence type: {sequence_type}")

    #     insertion = insertion.strip().upper()
    #     if sequence_type == "DNA":
    #         if not re.match(pat["DNA"], insertion, re.IGNORECASE):
    #             raise ValueError(
    #                 f"Invalid insertion sequence for DNA reference sequence."
    #             )
    #     elif sequence_type == "RNA":
    #         if not re.match(pat["RNA"], insertion, re.IGNORECASE):
    #             raise ValueError(
    #                 f"Invalid insertion sequence for RNA reference sequence."
    #             )
    #     elif sequence_type == "protein":
    #         if not re.match(pat["protein"], insertion, re.IGNORECASE):
    #             raise ValueError(
    #                 f"Invalid insertion sequence for protein reference sequence."
    #             )
    #     return insertion

    def to_string(self) -> str:
        """Convert SPDI object to a string representation.

        Returns:
            str: The string representation of the SPDI object.
        """
        spdi_expression = (
            f"{self.sequence}:{self.position}:{self.deletion}:{self.insertion}"
        )
        return spdi_expression

    def to_dict(self) -> dict:
        """Convert SPDI object to a dictionary.

        Returns:
            dict: A dictionary representation of the SPDI object.
        """
        return {
            "sequence": self.sequence,
            "position": self.position,
            "deletion": self.deletion,
            "insertion": self.insertion,
        }


if __name__ == "__main__":
    ex1 = SPDI(
        sequence="NC_000001.11", position='161629780', deletion="CC", insertion="C"
    )
    # print(ex1.to_string())
    print(ex1.sequence)
    print(ex1.position)
    print(ex1.deletion)
    print(ex1.insertion)
    # print(int(ex1.deletion))
