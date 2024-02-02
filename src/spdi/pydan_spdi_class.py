from pydantic import BaseModel, field_validator,Field,ValidationInfo
from typing import ClassVar
import re


class DASPDI(BaseModel):
    sequence: str
    position: str = Field(...,pattern=r'^\d+$')
    deletion: str
    insertion: str

    sequence_prefix_map: ClassVar[dict] = {
        "NC_": "DNA",
        "NM_": "DNA",
        "NG_": "DNA",
        "NR_": "RNA",
        "NP_": "PROTEIN",
    }
    # IUPC nucleotide codes: https://www.bioinformatics.org/sms/iupac.html
    pattern: ClassVar[dict] = {
        "EMPTY": "^$",
        "DIGIT": r"^\d+$",
        "DNA": r"^[ACGTRYSWKMBDHVN]*$",
        "RNA": r"^[ACGU]*$",
        "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
    }

    @field_validator("sequence")
    def sequence_valid(cls,v):
        """Validates a given reference sequence.

        Args:
            v (str): The reference sequence to be validated.

        Raises:
            ValueError: If the reference sequence prefix is not one of ["NC_", "NM_", "NG_", "NR_", "NP_"].

        Returns:
            str: The validated reference sequence.
        """
        sequence_prefix = v[:3]
        if sequence_prefix not in cls.sequence_prefix_map:
            raise ValueError(f"Invalid reference sequence prefix: {sequence_prefix}")
        return v
    
    @field_validator("deletion")
    def deletion_valid(cls,v,info: ValidationInfo):
        """Validates the deletion sequence.

        Args:
            v (str): The deletion sequence to validate.
            info (ValidationInfo): All of the fields and data being validated for this model.

        Raises:
            ValueError: If the deletion sequence is not valid or the sequence type is unknown.

        Returns:
            str: The validated deletion sequence.
        """
        deletion = v.upper().strip()
        if re.match(cls.pattern["EMPTY"], deletion):
            return ""
        if re.match(cls.pattern["DIGIT"], deletion):
            return deletion
        
        sequence_prefix = info.data["sequence"][:3]
        sequence_type = cls.sequence_prefix_map.get(sequence_prefix)
        if sequence_type not in cls.pattern:
            raise ValueError(f"Unknown sequence type: {sequence_type}")
        
        if isinstance(deletion, str):
            if not re.match(cls.pattern[sequence_type], deletion):
                raise ValueError(
                    f"Invalid deletion sequence for {sequence_type} reference sequence"
                )
        return deletion
    
    @field_validator("insertion")
    def insertion_valid(cls,v,info: ValidationInfo):
        """Validates the insertion sequence.

        Args:
            v (str): The insertion sequence to validate.
            info (ValidationInfo): All of the fields and data being validated for this model.

        Raises:
            ValueError: If the insertion sequence is not valid or the sequence type is unknown.

        Returns:
            str: The validated insertion sequence.
        """
        insertion = v.upper().strip()
        if re.match(cls.pattern["EMPTY"], insertion):
            return ""
        sequence_prefix = info.data["sequence"][:3]
        sequence_type = cls.sequence_prefix_map.get(sequence_prefix)
        if sequence_type not in cls.pattern:
            raise ValueError(f"Unknown sequence type: {sequence_type}")
        if isinstance(insertion, str):
            if not re.match(cls.pattern[sequence_type], insertion):
                raise ValueError(
                    f"Invalid insertion sequence for {sequence_type} reference sequence"
                )
        return insertion
