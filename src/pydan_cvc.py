from pydantic import field_validator,model_validator,Field,ConfigDict,ValidationInfo
from pydantic import BaseModel, PositiveInt
from typing import Optional,Dict,Any,Union
import re

# Citation of pydantic BaseModel: https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel

class pdCVC(BaseModel):
    origCoordSystem: str
    seqType: str
    refAllele: str
    altAllele: str
    start: PositiveInt 
    end: PositiveInt
    allelicState: Optional[str] = None
    geneSymbol: Optional[str] =  Field(default=None, pattern = r"^[a-zA-Z0-9]*$",strip_whitespace=True)
    hgncId: Optional[PositiveInt] = None
    chrom: Optional[str] = None
    genomeBuild: Optional[str] = Field(default=None, strip_whitespace=True)
    sequenceId: Optional[str] = Field(default=None, strip_whitespace=True)
    model_config = ConfigDict(extra='allow') #can potentially set it to ignore then would need to create a method to capture the extra data.
    #By default, Pydantic models won't error when you provide data for unrecognized fields, they will just be ignored

    # def get_extra_fields(self):
    #     return self.__pydantic_extra__
    
    @field_validator("origCoordSystem")
    def origCoordSystem_is_valid(cls, v):
        """Validate original coordinate system input. Method checks if the provided origCoordSystem
        is one of the allowed types: ('0-based interbase','0-based counting','1-based counting').


        Args:
            v (str): The origCoordSystem to be validated.

        Raises:
            ValueError: If the provided OrigCoordSystem is not one of the allowed types.

        Returns:
            str: The validated origCoordSystem value input.
        """
        v = v.strip()
        allowedOrigCoordSystem = (
            "0-based interbase",
            "0-based counting",
            "1-based counting",
        )
        if v not in allowedOrigCoordSystem:
            raise ValueError(
                f'Invalid origCoordSystem input: "{v}". Allowed types: {allowedOrigCoordSystem}.'
            )
        return v
    
    @field_validator("seqType")
    def seqType_is_valid(cls, v):
        """Validate sequence type input. Method checks if the provided seqType is one of the allowed types: ('DNA','RNA','PROTEIN').

        Args:
            v (str): The seqType to be validated.

        Raises:
            ValueError: If the provided seqType is not in the allowed types.

        Returns:
            str: The validate sequence type value input.
        """
        v = v.upper().strip()
        allowedSeqType = ("DNA", "RNA", "PROTEIN")
        if v not in allowedSeqType:
            raise ValueError(
                f'Invalid seqType input: "{v}". Allowed types: {allowedSeqType} (Case Insensitive).'
            )
        return v
    
    @field_validator("refAllele")
    def refAllele_is_valid(cls,v: str, info: ValidationInfo):
        """Validate the reference allele. See summary for more information.

        Args:
            v (str): The reference allele to be validated.
            info (ValidationInfo): _description_

        Raises:
            ValueError: If the provided refAllele is not empty and does not match the expected pattern for the given sequence type.
            ValueError: If the provided sequence type is not recognized.

        Returns:
            str: The validated reference allele value input.
        
        Summary:
            Method checks the input against defined regular expression patterns based on the sequence type.
            The allowed sequence types and corresponding patterns are as follows:
                - EMPTY: Only contains an empty string.
                - DIGIT: Only contains digits.
                - DNA: Only contains characters ('A', 'C', 'G', and 'T') or digits.
                - RNA: Only contains characters ('A', 'C', 'G', and 'U') or digits.
                - PROTEIN: Only contains 1-letter IUPAC codes (ACDEFGHIKLMNPQRSTVWY)
        """
        val = v.upper().strip()
        pat = {
            "EMPTY": "^$",
            "DIGIT": r"^\d+$",
            "DNA": r"^[ACGT]*$",
            "RNA": r"^[ACGU]*$",
            "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
        }

        if re.match(pat["EMPTY"], val, re.IGNORECASE):
            return ""
        if info.data['seqType'] in ("DNA", "RNA"):
            if not (re.match(pat[info.data['seqType']], val) or re.match(pat["DIGIT"], val)):
                raise ValueError(
                    f'Invalid reference Allele input: "{val}". Value need to match regular expression patter:({pat[info.data["seqType"]]} or {pat["DIGIT"]}).'
                )
            return val
        elif info.data['seqType'] == "PROTEIN":
            if not re.match(pat["PROTEIN"], val):
                raise ValueError(
                    f'Invalid reference Allele input: "{val}". Value need to match regular expression patter: ({pat["PROTEIN"]}).'
                )
            return val

    @field_validator("altAllele")
    def altAllele_is_valid(cls,v: str, info: ValidationInfo):
        """Validate the alternative allele. See summary for more information.

        Args:
            v (str): The alternative allele to be validated.
            info (ValidationInfo): _description_

        Raises:
            ValueError: If the provided altAllele is not empty and does not match the expected pattern for the given sequence type.
            ValueError: If the provided sequence type is not recognized.

        Returns:
            str: The validated alternative allele value input.

        Summary:
            Method checks the input against defined regular expression patterns based on the sequence type.
            The allowed sequence types and corresponding patterns are as follows:
                - EMPTY: Only contains an empty string.
                - DNA: Only contains characters 'A', 'C', 'G', and 'T'.
                - RNA: Only contains characters 'A', 'C', 'G', and 'U'.
                - PROTEIN: Only contains 1-letter IUPAC codes (ACDEFGHIKLMNPQRSTVWY).
        """
        val = v.upper().strip()
        pat = {
            "EMPTY": "^$",
            "DNA": r"^[ACGT]*$",
            "RNA": r"^[ACGU]*$",
            "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
        }

        if re.match(pat["EMPTY"], val, re.IGNORECASE):
            return ""
        if info.data['seqType'] in ("DNA", "RNA"):
            if not re.match(pat[info.data['seqType']], val):
                raise ValueError(
                    f'Invalid alternative Allele input: "{val}". Value need to match regular expression patter:({pat[info.data["seqType"]]}).'
                )
            return val
        elif info.data['seqType'] == "PROTEIN":
            if not re.match(pat["PROTEIN"], val):
                raise ValueError(
                    f'Invalid alternative Allele input: "{val}". Value need to match regular expression patter:({pat[info.data["seqType"]]}).'
                )
            return val

    @field_validator("allelicState")
    def allelicState_is_valid(cls, v):
        """Validate allelicState input. Method checks if the provided allelicState is one of the allowed types: ('heterozygous','homozygous').

        Args:
            v (str or None): The allelicState to be validated.

        Raises:
            ValueError: if the provided alleleicState is not None and not one of the allowed types.

        Returns:
            str or None: The validated allelicState value input.
        """
        if v is None:
            return v
        v = v.lower().strip()
        allowed_allelicState = ("heterozygous", "homozygous")
        if v not in allowed_allelicState:
            raise ValueError(
                f'Invalid allelicState input: "{v}". Allowed types: {allowed_allelicState} (Case Insensitive).'
            )
        return v

    @field_validator('end')
    def validate_start_end(cls, v: int, info: ValidationInfo):
        """Validate the start and end coordinate input. Method checks if the start coordinate is grater than the
        end coordinate.

        Args:
            v (int): _description_
            info (ValidationInfo): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if info.data['start'] > v:
            raise ValueError(
                f"The start coordinate value: {info.data['start']} can not be greater than or equal to the end coordinate value {v}."
            )
        return v

    @field_validator("chrom")
    def chrom_is_valid(cls, v):
        """Validate the chromosome identifier. Method allows chr prefix and checks if the provided chromosome is one of the allowed inputs: (1-22, X, Y, MT) or None.

        Args:
            v (str or None): The chromosome identifier to be validated.

        Raises:
            ValueError: If the provided chrom is not None and does not match the expected format.
            ValueError: ValueError: If the provided input is not one of the allowed types.

        Returns:
            str or None: The validated chromosome value input.
        """
        allowedChrom = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","Y","MT",)
        if v is None:
            return v
        value = v.upper().strip()

        pat = r"^(chr\s*)?([0-9a-zA-z]+)$"

        match = re.match(pat, value, re.IGNORECASE)

        if not match:
            raise ValueError(
                f'Invalid chrom input: "{v}". It does not match the expected format.'
            )

        chromValue = match.group(2)
        if chromValue not in allowedChrom:
            raise ValueError(
                f'Invalid chrom input:"{v}". Allowed types: {allowedChrom}'
            )
        return chromValue

    @model_validator(mode='after')
    def input_conditions_valid(self):
        """Validate the required conditions for chrom, genomeBuild, and sequenceId. Requirements include
        that the user inputs either both "chrom" and "genomeBuild" or just "sequenceId.

        Raises:
            ValueError:  If the input arguments do not meet the required conditions.
        """
        if not ((self.chrom and self.genomeBuild) or self.sequenceId):
            raise ValueError(
                "Either (chrom AND genomeBuild) or sequenceId is required."
            )

    def normalized_data(self) -> dict:
        #TODO: double check this implementation
        # if self.origCoordSystem == "0-based interbase":
        #     pass
        # elif self.origCoordSystem == "0-based counting":
        #     self.start += 1
        #     self.origCoordSystem = "0-based interbase"
        # elif self.origCoordSystem == "1-based counting":
        #     self.start -= 1
        #     self.origCoordSystem = "0-based interbase"
        # else:
        #     raise ValueError("Invalid coordinate system specified.")
        
        return {
            "origCoordSystem": self.origCoordSystem,
            "seqType": self.seqType,
            "allelicState": self.allelicState,
            "associatedGene": {
                "geneSymbol": self.geneSymbol,
                "hgncId": self.hgncId,
            },
            "refAllele": self.refAllele,
            "altAllele": self.altAllele,
            "position": {
                "chrom": self.chrom,
                "genomeBuild": self.genomeBuild,
                "start": self.start,
                "end": self.end,
                "sequenceId": self.sequenceId,
            },
        }



