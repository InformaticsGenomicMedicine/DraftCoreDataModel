from pydantic import BaseModel, Field
import typing

# Important links: 
# https://build.fhir.org/branches/cg-im-moldef_work_in_progress_2/moleculardefinition.html
# https://hl7.org/fhir/molecularsequence.html
# https://github.com/SalemBajjali/fhir.resources/blob/main/fhir/resources/molecularsequence.py#L184
# https://github.com/SalemBajjali/fhir.resources/blob/molseqplus_dev_sb/fhir/resources/molecularsequenceplus.py#L440

class MolecularDefinition(BaseModel):
    resource_type: str = Field("MolecularDefinition", Literal=True)

    identifier: typing.List = Field(
        None,
        alias="identifier",
        title="Unique ID for this particular sequence",
        description="A unique identifier for this particular resource instance.",
        element_property=True,
    )

    type: str = Field(
        None,
        alias="type",
        title="aa | dna | rna",
        description="The type of the Molecular Definition (Amino Acid, DNA, RNA).",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["aa", "dna", "rna"],
    )

    name: typing.List = Field(
        None,
        alias="name",
        title="Label of this MolecularDefinition",
        description="The label associates with this MolecularDefinition.",
        # if property is element of this resource.
        element_property=False,
    )

    location: typing.List = Field(
        None,
        alias="location",
        title="Location of this molecule",
        description="The molecular location of this molecule.",
        # if property is element of this resource.
        element_property=True,
    )

    memberState: typing.List = Field(
        None,
        alias="memberState",
        title="Member",
        description="A member or part of this molecule.",
        element_property=True,
    )

    representation: typing.List = Field(
        None,
        alias="representation",
        title="Representation",
        description=(
            "The representation of this molecular definition, e.g., as a literal or repeated elements."
        ),
        element_property=True,
    )
# -------------------------------------
#             Location
# -------------------------------------
class MolecularDefinitionLocation(BaseModel):

    resource_type : str = Field("MolecularDefinitionLocation", Literal = True)

    sequenceLocation: typing.List = Field(
        None,
        alias="sequenceLocation",
        title="Location of this molecule in context of a sequence",
        description=("The Location of this molecule in context of a sequence."),
        element_property=True,
    )

    cytobandLocation: typing.List = Field(
        None,
        alias="cytobandLocation",
        title="Location of this molecule in context of a cytoband",
        description=("The location of this molecule in context of a cytoband."),
        element_property=True,
    )

    featureLocation: typing.List = Field(
        None,
        alias="featureLocation",
        title="Location in context of a feature",
        description=("The location of this molecule in context of a feature."),
        element_property=True,
    )

class MolecularDefinitionLocationSequenceLocation(BaseModel):

    resource_type: str = Field("MolecularDefinitionLocationSequenceLocation", Literal = True)

    sequenceContext: typing.List = Field(
        ...,
        alias="sequenceContext",
        title="Reference sequence",
        description="The reference Sequence that contains this location.",
        element_property=True,
    )

    coordinateInterval: typing.List = Field(
        None,
        alias="coordinateInterval",
        title="Coordinate Interval for this location",
        description="The coordinate interval for this location.",
        element_property=True,
    )
#TODO: double check if this would be an enum_values.
    strand: str = Field(
        None,
        alias="strand",
        title="Forward or Reverse",
        description="The identification of the strand direction, i.e, forward vs reverse strand.",
        element_property=True,
        # enum_values=["forward", "reverse"],
    )

class MolecularDefinitionCoordinateInterval(BaseModel):

    resource_type : str = Field("MolecularDefinitionCoordinateInterval", Literal = True)

    numberingSystem: str = Field(
        None,
        alias="numberingSystem",
        title="Coordinate System",
        description="The coordinate system of this interval.",
        element_property=True,
    )
    
    #TODO: double check this
    startQuantity: typing.List = Field(
        None,
        alias="startQuantity",
        title="Start",
        description="The start of this interval.",
        element_property=True,
    )

    startRange: typing.List = Field(
        None,
        alias="startRange",
        title="Start",
        description="The start of this interval.",
        element_property=True,
    )

    endQuantity: typing.List = Field(
        None,
        alias="endQuantity",
        title="End",
        description="The end of this interval.",
        element_property=True,
    )

    endRange: typing.List = Field(
        None,
        alias="endRange",
        title="End",
        description="The end of this interval.",
        element_property=True,
    )

class MolecularDefinitionLocationCytobandLocation(BaseModel):

    resource_type : str = Field("MolecularDefinitionLocationCytobandLocation", Literal = True)

    genomeAssembly: typing.List = Field(
        None,
        alias="genomeAssembly",
        title="Reference Genome",
        description="The reference genome assemble.",
        element_property=True,
    )

    cytobandInterval: typing.List = Field(
        None,
        alias="cytobandInterval",
        title="Cytoband Interval",
        description="The Cytoband Interval.",
        element_property=True,
    )

class MolecularDefinitionGenomeAssembly(BaseModel):

    resource_type : str = Field("MolecularDefinitionGenomeAssembly", Literal = True)

    organism: str = Field(
        None,
        alias="organism",
        title="Species of the organism",
        description="Species of the organism.",
        element_property=False,
    )

    build: str = Field(
        None,
        alias="build",
        title="Build number",
        description="The build number of this genome assemble.",
        element_property=False,
    )
    
    accession: str = Field(
        None,
        alias="accession",
        title="Accession",
        description="The accession of this genome assemble.",
        element_property=False,
    )
    #TODO: double check this
    descriptionMarkdown: str = Field(
        None,
        alias="descriptionMarkdown",
        title="Genome assemble description",
        description="The description of this genome assemble.",
        element_property=False,
    )

    descriptionString: str = Field(
        None,
        alias="descriptionString",
        title="Genome assemble description",
        description="The description of this genome assemble.",
        element_property=False,
    )

class MolecularDefinitionCytobandInterval(BaseModel):

    resource_type : str = Field("MolecularDefinitionLocationCytobandLocation", Literal = True)

    chromosome: str = Field(
        ...,
        alias="chromosome",
        title="Chromosome",
        description="The chromosome where this cytoband interval occurs.",
        element_property=True,
    )

    startCytoband: typing.List = Field(
        None,
        alias="startCytoband",
        title="Start",
        description="The start of this cytoband Interval.",
        element_property=True,
    )

    endCytoband: typing.List = Field(
        None,
        alias="endCytoband",
        title="End",
        description="The end of this cytoband Interval.",
        element_property=True,
    )

class MolecularDefinitionStartCytoband(BaseModel):

    resource_type : str = Field("MolecularDefinitionStartCytoband", Literal = True)

    armCode: str = Field(
        None,
        alias="armCode",
        title="Arm",
        description="The arm of this start interval.",
        element_property=False,
    )

    armString: str = Field(
        None,
        alias="armString",
        title="Arm",
        description="The arm of this start interval.",
        element_property=False,
    )

    regionCode: str = Field(
        None,
        alias="regionCode",
        title="Region",
        description="The region of this start interval.",
        element_property=False,
    )

    regionString: str = Field(
        None,
        alias="regionString",
        title="Region",
        description="The region of this start interval.",
        element_property=False,
    )

    bandCode: str = Field(
        None,
        alias="bandCode",
        title="Band",
        description="The band of this start interval.",
        element_property=False,
    )

    bandString: str = Field(
        None,
        alias="bandString",
        title="Band",
        description="The band of this start interval.",
        element_property=False,
    )

    subBandCode: str = Field(
        None,
        alias="subBandCode",
        title="SuBand",
        description="The sub-band of this start interval.",
        element_property=True,
    )

    subBandString: str = Field(
        None,
        alias="subBandString",
        title="SuBand",
        description="The sub-band of this start interval.",
        element_property=True,
    )

class MolecularDefinitionEndCytoband(BaseModel):

    resource_type : str = Field("MolecularDefinitionStartCytoband", Literal = True)

    armCode: str = Field(
        None,
        alias="armCode",
        title="Arm",
        description="The arm of this end interval.",
        element_property=False,
    )

    armString: str = Field(
        None,
        alias="armString",
        title="Arm",
        description="The arm of this end interval.",
        element_property=False,
    )

    regionCode: str = Field(
        None,
        alias="regionCode",
        title="Region",
        description="The region of this end interval.",
        element_property=False,
    )

    regionString: str = Field(
        None,
        alias="regionString",
        title="Region",
        description="The region of this end interval.",
        element_property=False,
    )

    bandCode: str = Field(
        None,
        alias="bandCode",
        title="Band",
        description="The band of this end interval.",
        element_property=False,
    )

    bandString: str = Field(
        None,
        alias="bandString",
        title="Band",
        description="The band of this end interval.",
        element_property=False,
    )

    subBandCode: str = Field(
        None,
        alias="subBandCode",
        title="SuBand",
        description="The sub-band of this end interval.",
        element_property=False,
    )

    subBandString: str = Field(
        None,
        alias="subBandString",
        title="SuBand",
        description="The sub-band of this end interval.",
        element_property=False,
    )

class MolecularDefinitionLocationFeatureLocation(BaseModel):

    resource_type : str = Field("MolecularDefinitionLocationFeatureLocation", Literal = True)

    geneId: str = Field(
        None,
        alias="geneId",
        title="Gene Id",
        description="The gene Id where this molecule occurs.",
        element_property=True,
    )


# -------------------------------------
#            Representation
# -------------------------------------


class MolecularDefinitionRepresentation(BaseModel):

    resource_type: str = Field("MolecularDefinitionRelativeEdit", Literal = True)

    literal: typing.List = Field(
        None,
        alias="literal",
        title="A literal representation",
        description=("A literal representation."),
        element_property=True,
    )

    resolvable: typing.List = Field(
        None,
        alias="resolvable",
        title="A resolvable representation of a molecule that optionally contains formatting in addition to the specification of the primary sequence itself",
        description=("A resolvable representation of a molecule that optionally contains formatting in addition to the specification of the primary sequence itself. The sequence may be provided inline as an attached document or through a resolvable URI."),
        element_property=True,
    )

    extracted : typing.List = Field(
        None,
        alias="extracted",
        title="A Molecular Sequence that is represented as an extracted portion of a different Molecular Sequence",
        description=("A Molecular Sequence that is represented as an extracted portion of a different Molecular Sequence."),
        element_property=True,
    )

    repeated: typing.List = Field(
        None,
        alias="repeated",
        title="A Molecular Sequence that is represented as a repeated sequence motif",
        description=("A Molecular Sequence that is represented as a repeated sequence motif."),
        element_property=True,
    )

    concatenated: typing.List = Field(
        None,
        alias="concatenated",
        title="A Molecular Sequence that is represented as an ordered concatenation of two or more Molecular Sequences",
        description=("A Molecular Sequence that is represented as an ordered concatenation of two or more Molecular Sequences."),
        element_property=True,
    )

    relative: typing.List = Field(
        None,
        alias="relative",
        title="A Molecular Definition that is represented as an ordered series of edits on a specified starting sequence",
        description=("A Molecular Definition that is represented as an ordered series of edits on a specified starting sequence."),
        element_property=True,
    )


class MolecularDefinitionLiteral(BaseModel):
    
    resource_type: str = Field("MolecularDefinitionLiteral", Literal = True)

    encoding: typing.List = Field(
        None,
        alias="encoding",
        title="The encoding used for the expression of the primary sequence",
        description=("The encoding used for the expression of the primary sequence." 
                     "This defines the characters that may be used in the primary sequence"
                     "and it permits the explicit inclusion/exclusion of IUPAC ambiguity codes."),
        element_property=True,
    )

    value: str = Field(
        ...,
        alias="value",
        title="The primary (linear) sequence, expressed as a literal string",
        description=("The primary (linear) sequence, expressed as a literal string."),
        element_property=True,
    )

class MolecularDefinitionExtracted(BaseModel):

    resource_type: str = Field("MolecularDefinitionExtracted", Literal = True)

    startingMolecule: typing.List = Field(
        ...,
        alias="startingMolecule",
        title="The Molecular Sequence that serves as the parent sequence, from which the intended sequence will be extracted",
        description=("The Molecular Sequence that serves as the parent sequence, from which the intended sequence will be extracted."),
        element_property=True,
    )

    start: int = Field(
        ...,
        alias="start",
        title="The start coordinate (on the parent sequence) of the interval that defines the subsequence to be extracted",
        description=("The start coordinate (on the parent sequence) of the interval that defines the subsequence to be extracted."),
        element_property=True,
    )

    end: int = Field(
        ...,
        alias="end",
        title="The end coordinate (on the parent sequence) of the interval that defines the subsequence to be extracted",
        description=("The end coordinate (on the parent sequence) of the interval that defines the subsequence to be extracted."),
        element_property=True,
    )

    coordinateSystem: str = Field(
        ...,
        alias="coordinateSystem",
        title="The coordinate system used to define the interval that defines the subsequence to be extracted. Coordinate systems are usually 0- or 1-based",
        description=("The coordinate system used to define the interval that defines the subsequence to be extracted. Coordinate systems are usually 0- or 1-based."),
        element_property=True,
    )

    reverseComplement: bool = Field(
        None,
        alias="reverseComplement",
        title="A flag that indicates whether the extracted sequence should be reverse complemented",
        description=("A flag that indicates whether the extracted sequence should be reverse complemented."),
        element_property=True,
    )

class MolecularDefinitionRepeated(BaseModel):

    resource_type: str = Field("MolecularDefinitionRepeated", Literal = True)

    sequenceMotif: typing.List = Field(
        ...,
        alias="sequenceMotif",
        title="The sequence that defines the repeated motif",
        description=("The sequence that defines the repeated motif."),
        element_property=True,
    )

    copyCount: int = Field(
        ...,
        alias="copyCount",
        title="The number of repeats (copies) of the sequence motif",
        description=("The number of repeats (copies) of the sequence motif."),
        element_property=True,
    )

class MolecularDefinitionConcatenated(BaseModel):

    resource_type: str = Field("MolecularDefinitionConcatenated", Literal = True)

    sequenceElement: typing.List = Field(
        ...,
        alias="sequenceElement",
        title="One element of a concatenated Molecular Sequence",
        description=("One element of a concatenated Molecular Sequence."),
        element_property=True,
    )

class MolecularDefinitionSequenceElement(BaseModel):

    resource_type: str = Field("MolecularDefinitionSequenceElement", Literal = True)

    sequence: typing.List = Field(
        ...,
        alias="sequence",
        title="The Molecular Sequence corresponding to this element",
        description=("The Molecular Sequence corresponding to this element."),
        element_property=True,
    )

    ordinalIndex: int = Field(
        ...,
        alias="ordinalIndex",
        title="The ordinal position of this sequence element within the concatenated Molecular Sequence",
        description=("The ordinal position of this sequence element within the concatenated Molecular Sequence."),
        element_property=True,
    )

class MolecularDefinitionRelative(BaseModel):

    resource_type: str = Field("MolecularDefinitionRelative", Literal = True)
    
    startingMolecule: typing.List = Field(
        ...,
        alias="startingMolecule",
        title="The Molecular Sequence that serves as the starting sequence, on which edits will be applied",
        description=("The Molecular Sequence that serves as the starting sequence, on which edits will be applied."),
        element_property=True,
    )

    edit: typing.List = Field(
        None,
        alias="edit",
        title="An edit (change) made to a sequence",
        description=("An edit (change) made to a sequence."),
        element_property=True,
    )

class MolecularDefinitionEdit(BaseModel):

    resource_type: str = Field("MolecularDefinitionEdit", Literal = True)

    editOrdinal: int = Field(
        None,
        alias="editOrdinal",
        title="The order of this edit, relative to other edits on the starting sequence",
        description=("The order of this edit, relative to other edits on the starting sequence."),
        element_property=False,
    )

    coordinateSystem: str = Field(
        ...,
        alias="coordinateSystem",
        title="The coordinate system used to define the edited intervals on the starting sequence. Coordinate systems are usually 0- or 1-based",
        description=("The coordinate system used to define the edited intervals on the starting sequence. Coordinate systems are usually 0- or 1-based."),
        element_property=True,
    )

    start: int = Field(
        ...,
        alias="start",
        title="The start coordinate of the interval that will be edited",
        description=("The start coordinate of the interval that will be edited."),
        element_property=True,
    )

    end: int = Field(
        ...,
        alias="end",
        title="The end coordinate of the interval that will be edited",
        description=("The end coordinate of the interval that will be edited."),
        element_property=True,
    )

    replacementMolecule: typing.List = Field(
        ...,
        alias="replacementMolecule",
        title="The sequence that defines the replacement sequence used in the edit operation",
        description=("The sequence that defines the replacement sequence used in the edit operation."),
        element_property=True,
    )

    replacedMolecule: typing.List = Field( 
        None,
        alias="replacedMolecule",
        title="The sequence on the 'starting' sequence for the edit operation, defined by the specified interval, that will be replaced during the edit",
        description=("The sequence on the 'starting' sequence for the edit operation, defined by the specified interval, that will be replaced during the edit."),
        element_property=True,
    )

    
# -------------------------------------
#            Sequence
# -------------------------------------

# -------------------------------------
#            Allele
# -------------------------------------


# -------------------------------------
#            Genotype
# -------------------------------------


# -------------------------------------
#            Haplotype
# -------------------------------------

