import re
import json

from src.exceptions import (
    InvalidInputConditionsError,
    InvalidCoordinateSystemError,
    InvalidSequenceTypeError,
    InvalidReferenceAlleleError,
    InvalidAlternativeAlleleError,
    InvalidCoordinateTypeError,
    InvalidCoordinateValueError,
    StartCoordinateGreaterThanEndError,
    InvalidAllelicStateError,
    InvalidGeneSymbolError,
    InvalidHGNCIdTypeError,
    InvalidHGNCIdError,
    InvalidChromosomeError,
    InvalidGenomeBuildTypeError,
    InvalidSequenceIdTypeError)

class CoreVariantClass:

    """The CoreVariantClass is draft schema."""

    def __init__(
        self,
        origCoordSystem: str,
        seqType: str,
        refAllele: str,
        altAllele: str,
        start: int,
        end: int,
        allelicState: str = None,
        geneSymbol: str = None,
        hgncId: int = None,
        chrom: str = None,
        genomeBuild: str = None,
        sequenceId: str = None,
        **kwargs: dict,
    ) -> None:
        # saving initial parameters
        self.initParamValues: dict = {
            "origCoordSystem": origCoordSystem,
            "seqType": seqType,
            "refAllele": refAllele,
            "altAllele": altAllele,
            "start": start,
            "end": end,
            "allelicState": allelicState,
            "geneSymbol": geneSymbol,
            "hgncId": hgncId,
            "chrom": chrom,
            "genomeBuild": genomeBuild,
            "sequenceId": sequenceId,
            "kwargs": kwargs,
        }
        
# post init in data classes
        self._validate_input_conditions(chrom, genomeBuild, sequenceId)
        self.origCoordSystem: str = self._validate_orig_coord_system(origCoordSystem)
        self.seqType: str = self._validate_seq_type(seqType)
        self.refAllele: str = self._validate_reference_allele(refAllele)
        self.altAllele: str = self._validate_alternative_allele(altAllele)
        self.start: int = self._validate_coordinates(start, "start")
        self.end: int = self._validate_coordinates(end, "end")
        self._validate_start_coord_end_coord()
        self.allelicState: str = self._validate_allelic_state(allelicState)
        self.geneSymbol: str = self._validate_gene_symbol(geneSymbol)
        self.hgncId: int = self._validate_hgnc_id(hgncId)
        self.chrom: str = self._validate_chrom(chrom)
        self.genomeBuild: str = self._validate_genome_build(genomeBuild)
        self.sequenceId: str = self._validate_sequence_id(sequenceId)
        self.kwargs: dict = kwargs

    def __repr__(self) -> str:
        """Returns a string representation of the CoreVariantClass object.

        Returns:
            str: A string representation of the CoreVariantClass object.
        """
        return f"CoreVariantClass({self.origCoordSystem},{self.seqType},{self.refAllele},{self.altAllele},{self.start},{self.end},{self.allelicState},{self.geneSymbol},{self.hgncId},{self.chrom},{self.genomeBuild},{self.sequenceId},{self.kwargs})"

    def as_dict(self) -> dict:
        """Converts CoreVariantClass object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        return {
            "origCoordSystem": self.origCoordSystem,
            "seqType": self.seqType,
            "refAllele": self.refAllele,
            "altAllele": self.altAllele,
            "start": self.start,
            "end": self.end,
            "allelicState": self.allelicState,
            "geneSymbol": self.geneSymbol,
            "hgncId": self.hgncId,
            "chrom": self.chrom,
            "genomeBuild": self.genomeBuild,
            "sequenceId": self.sequenceId,
            "kwargs": self.kwargs,
        }

    def as_json(self) -> str:
        """Converts CoreVariantClass object to a JSON string representation.

        Returns:
            str: A JSON formatted string of the CoreVariantClass object.
        """
        return json.dumps(self.as_dict(), indent=2)

    # NOTE: The validation step occurs within the constructor (__init__) method. If an error occurs during validation,
    # a ValueError is raised, and the object is not fully instantiated.
    #  This means that the values are captured in the __init__ method, but if an error occurs, the object won't be created.

    def init_params(self) -> dict:
        """A dictionary of the initial parameters.

        Returns:
            dict: A dictionary (Key: Initial parameters, Values: parameters values).
        """
        return self.initParamValues

    def _normalize_origCoordSystem(self):
        """Normalize the origCoordSystem to "0-based interbase".

        Raises:
            ValueError: If the specified origCoordSystem is not one of the allowed types.
        """
        if self.origCoordSystem == "0-based interbase":
            pass
        elif self.origCoordSystem == "0-based counting":
            self.start += 1
            self.origCoordSystem = "0-based interbase"
        elif self.origCoordSystem == "1-based counting":
            self.start -= 1
            self.origCoordSystem = "0-based interbase"
        else:
            raise ValueError("Invalid coordinate system specified.")

    # TODO: this was created to for test purpose this will be removed later
    def init_normalized_data(self) -> dict:
        """Generates a dictionary representation of normalized data.

        Returns:
            dict: A dictionary representation of normalized data.
        """
        self._normalize_origCoordSystem()

        return {
            "origCoordSystem": self.origCoordSystem,
            "seqType": self.seqType,
            "refAllele": self.refAllele,
            "altAllele": self.altAllele,
            "start": self.start,
            "end": self.end,
            "allelicState": self.allelicState,
            "geneSymbol": self.geneSymbol,
            "hgncId": self.hgncId,
            "chrom": self.chrom,
            "genomeBuild": self.genomeBuild,
            "sequenceId": self.sequenceId,
            "kwargs": self.kwargs,
        }

    # TODO: create test
    # TODO: Currently went we translate SPDI,HGVS,VRS it is translated into the CVC base format and not the normalized_data format.
    # We need to address the point of this normalized_data method. Currently I dont see much use of this especially that is has a different format then the base format.
    # Seems that we are over complicating things by having two different formats structures. IF we want to say that 0-based interbase is the normalized form then i dont think we need to create a whole new output format.
    # we can just use the _normalize_origCoordSystem which will change the start coordinate to 0-based interbase and then we can just use the base format to output the data.

    def normalized_data(self) -> dict:
        """Generates a dictionary representation of normalized data.

        Returns:
            dict: A dictionary representation of normalized data.
        """
        self._normalize_origCoordSystem()

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

    def _validate_input_conditions(self, chrom, genomeBuild, sequenceId):
        """Validate the required conditions for chrom, genomeBuild, and sequenceId. Requirements include
        that the user inputs either both "chrom" and "genomeBuild" or just "sequenceId.

        Args:
            chrom (str): Chromosome input.
            genomeBuild (str): Genomic Build input.
            sequenceId (str): Sequence ID input.

        Raises:
            ValueError: If the input arguments do not meet the required conditions.
        """
        if not ((chrom and genomeBuild) or sequenceId):
            raise InvalidInputConditionsError(
                "Required to have both (chrom AND genomeBuild) or sequenceId"
            )

    def _validate_orig_coord_system(self, origCoordSystem):
        """Validate original coordinate system input. Method checks if the provided origCoordSystem
        is one of the allowed types: ('0-based interbase','0-based counting','1-based counting').

        Args:
            origCoordSystem (str): The origCoordSystem to be validated.

        Raises:
            ValueError: If the provided OrigCoordSystem is not one of the allowed types.

        Returns:
            str: The validated origCoordSystem value input.
        """
        value = origCoordSystem.strip()
        allowedOrigCoordSystem = (
            "0-based interbase",
            "0-based counting",
            "1-based counting",
        )
        if value not in allowedOrigCoordSystem:
            raise InvalidCoordinateSystemError(
                f'Invalid origCoordSystem input: "{origCoordSystem}". Allowed types: {allowedOrigCoordSystem}.'
            )
        return value

    def _validate_seq_type(self, seqType):
        """Validate sequence type input. Method checks if the provided seqType is one of the allowed types: ('DNA','RNA','PROTEIN').

        Args:
            seqType (str): The seqType to be validated.

        Raises:
            ValueError: If the provided seqType is not in the allowed types.

        Returns:
            str: The validate sequence type value input.
        """
        value = seqType.upper().strip()
        allowedSeqType = ("DNA", "RNA", "PROTEIN")
        if value not in allowedSeqType:
            raise InvalidSequenceTypeError(
                f'Invalid seqType input: "{seqType}". Allowed types: {allowedSeqType} (Case Insensitive).'
            )
        return value

    def _validate_reference_allele(self, refAllele):
        """Validate the reference allele. See summary for more information.

        Args:
            refAllele (str): The reference allele to be validated.

        Raises:
            ValueError: If the provided refAllele is not empty and does not match the expected pattern for the given sequence type.
            ValueError: If the provided sequence type is not recognized.

        Returns:
            str: The validated reference allele value input.
        """
        val = refAllele.upper().strip()

        pat = {
            "EMPTY": "^$",
            "DIGIT": r"^\d+$",
            "DNA": r"^[ACGT]*$",
            "RNA": r"^[ACGU]*$",
            "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
        }

        if re.match(pat["EMPTY"], val, re.IGNORECASE):
            return ""
        if self.seqType in ("DNA", "RNA"):
            if not (re.match(pat[self.seqType], val) or re.match(pat["DIGIT"], val)):
                raise InvalidReferenceAlleleError(
                    f'Invalid {refAllele} input: "{val}". Value need to match regular expression patter:({pat[self.seqType]} or {pat["DIGIT"]}).'
                )
            return val
        elif self.seqType == "PROTEIN":
            if not re.match(pat["PROTEIN"], val):
                raise InvalidReferenceAlleleError(
                    f'Invalid {refAllele} input: "{val}". Value need to match regular expression patter: ({pat["PROTEIN"]}).'
                )
            return val

    def _validate_alternative_allele(self, altAllele):
        """Validate the alternative allele. See summary for more information.

        Args:
            altAllele (str): The alternative allele to be validated.

        Raises:
            ValueError: If the provided altAllele is not empty and does not match the expected pattern for the given sequence type.
            ValueError: If the provided sequence type is not recognized.

        Returns:
            str: The validated alternative allele value input.
        """
        val = altAllele.upper().strip()

        pat = {
            "EMPTY": "^$",
            "DNA": r"^[ACGT]*$",
            "RNA": r"^[ACGU]*$",
            "PROTEIN": r"^[ACDEFGHIKLMNPQRSTVWY]$",
        }

        if re.match(pat["EMPTY"], val, re.IGNORECASE):
            return ""
        if self.seqType in ("DNA", "RNA"):
            if not re.match(pat[self.seqType], val):
                raise InvalidAlternativeAlleleError(
                    f'Invalid {altAllele} input: "{val}". Value need to match regular expression patter:({pat[self.seqType]}).'
                )
            return val
        elif self.seqType == "PROTEIN":
            if not re.match(pat["PROTEIN"], val):
                raise InvalidAlternativeAlleleError(
                    f'Invalid {altAllele} input: "{val}". Value need to match regular expression patter:({pat[self.seqType]}).'
                )
            return val

    def _validate_coordinates(self, value, attributeName):
        """Validate the coordinate input. Method checks if the value is an integer and is greater than or equal to 0.

        Args:
            value (int): The coordinate value to be validated.
            attributeName (str): The name of the attribute associated with the coordinate value.

        Raises:
            ValueError: If the provided {attributeName} is not an integer.
            ValueError: If the validated {attributeName} is not greater than or equal to 0.

        Returns:
            int: The validated coordinate value input.
        """
        if not isinstance(value, int):
            raise InvalidCoordinateTypeError(
                f'Invalid {attributeName} input: "{value}": is not an integer.'
            )
        if value < 0:
            raise InvalidCoordinateValueError(
                f'Invalid {attributeName} input: "{value}": is not greater then or equal to 0.'
            )
        return value

    def _validate_start_coord_end_coord(self):
        """Validate the start and end coordinate input. Method checks if the start coordinate is greater than the
        end coordinate.

        Raises:
            ValueError: If the start coordinate is greater than the end coordinate.
        """
        if self.start > self.end:
            raise StartCoordinateGreaterThanEndError(
                f"The start coordinate value: {self.start} can not be greater than or equal to the end coordinate value {self.end}."
            )

    def _validate_allelic_state(self, allelicState):
        """Validate allelicState input. Method checks if the provided allelicState is one of the allowed types: ('heterozygous','homozygous').

        Args:
            allelicState (str or None): The allelicState to be validated.

        Raises:
            ValueError: if the provided alleleicState is not None and not one of the allowed types.

        Returns:
            str or None: The validated allelicState value input.
        """
        if allelicState is None:
            return allelicState

        value = allelicState.lower().strip()
        allowed_allelicState = ("heterozygous", "homozygous")
        if value not in allowed_allelicState:
            raise InvalidAllelicStateError(
                f'Invalid allelicState input: "{allelicState}". Allowed types: {allowed_allelicState} (Case Insensitive).'
            )
        return value

    def _validate_gene_symbol(self, geneSymbol):
        """Validate geneSymbol input. Method checks if input value matches regular expression pattern ^[a-zA-Z0-9]*$ .

        Args:
            geneSymbol (str or None): The geneSymbol to be validated.

        Raises:
            ValueError: if the provided geneSymbol is not NOne or not matching the regular expression pattern.

        Returns:
            str or None: The validated geneSymbol value input.
        """

        if geneSymbol is None:
            return geneSymbol

        pat = r"^[a-zA-Z0-9]*$"
        value = geneSymbol.strip()
        if not re.match(pat, value):
            raise InvalidGeneSymbolError(
                f'Invalid geneSymbol input: "{geneSymbol}". Allowed type: alphanumeric characters only.'
            )
        return value

    def _validate_hgnc_id(self, hgncId):
        """Validate the hgncId input. Method checks if the value is an integer and is greater than 1.

        Args:
            hgncId (int or None): The hgncId value to be validated.

        Raises:
            ValueError: If the provided hgncID is not None and not an integer.
            ValueError: If the validated hgncId is not greater than or equal to 1.

        Returns:
            int or None: The validated HGNC value input.
        """

        if hgncId is None:
            return hgncId

        if not InvalidHGNCIdTypeError(hgncId, int):
            raise ValueError(f'Invalid hgncId input: "{hgncId}": is not an integer.')
        if hgncId < 1:
            raise InvalidHGNCIdError(
                f'Invalid hgncId input: "{hgncId}": is not greater then or equal to 1.'
            )
        return hgncId

    def _validate_chrom(self, chrom):
        """Validate the chromosome identifier. Method allows chr prefix and checks if the provided chromosome is one of the allowed inputs: (1-22, X, Y, MT) or None.

        Args:
            chrom (str or None): The chromosome identifier to be validated.

        Raises:
            ValueError: If the provided chrom is not None and does not match the expected format.
            ValueError: ValueError: If the provided input is not one of the allowed types.

        Returns:
            str or None: The validated chromosome value input.
        """

        if chrom is None:
            return chrom

        value = chrom.upper().strip()

        allowedChrom = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "X",
            "Y",
            "MT",
        )

        pat = r"^(chr\s*)?([0-9a-zA-z]+)$"

        match = re.match(pat, value, re.IGNORECASE)

        if not match:
            raise InvalidChromosomeError(
                f'Invalid chrom input: "{chrom}". It does not match the expected format.'
            )

        chromValue = match.group(2)
        if chromValue not in allowedChrom:
            raise InvalidChromosomeError(
                f'Invalid chrom input:"{chrom}". Allowed types: {allowedChrom}'
            )
        return chromValue

    def _validate_genome_build(self, genomeBuild):
        """Validate genomeBuild input. Method checks if input value is string or None.

        Args:
            genomeBuild (str or None): The genomeBuild to be validated.

        Raises:
            ValueError: If the provided genomeBuild is not None and not a string.

        Returns:
            str or None: The validated genomeBuild value input.
        """
        if genomeBuild is None:
            return genomeBuild
        value = genomeBuild.strip()
        if not isinstance(value, str):
            raise InvalidGenomeBuildTypeError(
                f'Invalid genomeBuild input: "{genomeBuild}". Allowed types: None or string'
            )
        return value

    def _validate_sequence_id(self, sequenceId):
        """Validate sequenceId input. Method checks if input value is a string or None.

        Args:
            sequenceId (str or None): The sequenceId to be validated.

        Raises:
            ValueError: If the provided sequenceId is not None and not a string.

        Returns:
            str or None: The validated sequenceId value input.
        """
        if sequenceId is None:
            return sequenceId
        if not isinstance(sequenceId, str):
            raise InvalidSequenceIdTypeError(
                f'Invalid sequenceId input: "{sequenceId}". Allowed types: None or string'
            )
        return sequenceId
