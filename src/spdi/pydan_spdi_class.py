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
        sequence_prefix = v[:3]
        if sequence_prefix not in cls.sequence_prefix_map:
            raise ValueError(f"Invalid reference sequence prefix: {sequence_prefix}")
        return v
    
    @field_validator("deletion")
    def deletion_valid(cls,v,info: ValidationInfo):
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
