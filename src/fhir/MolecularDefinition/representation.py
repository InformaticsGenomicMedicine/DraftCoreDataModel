from pydantic import BaseModel, Field
import typing

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

