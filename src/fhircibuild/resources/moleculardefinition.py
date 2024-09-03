from pydantic import Field 
import typing
from fhir.resources import backboneelement, domainresource, fhirtypes # type: ignore
import src.fhircibuild.resources.fhirtypeextra as fhirtypeextra
from fhir_core.types import CodeType,StringType,BooleanType,IntegerType



class MolecularDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource MolecularDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Representation of a Molecular Definition.
    """
    __resource_type__ = "MolecularDefinition"

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique ID for this particular sequence",
        description="A unique identifier for this particular sequence instance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: CodeType = Field( # type: ignore
        None,
        alias="type",
        title="aa | dna | rna",
        description="Amino Acid Sequence/ DNA Sequence / RNA Sequence.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["aa", "dna", "rna"],
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_type", title="Extension field for ``type``."
    )

    location: typing.List[fhirtypeextra.MolecularDefinitionLocationType] = Field(  # type: ignore
        None,
        alias="location",
        title="Location of this molecule",
        description="The molecular location of this molecule.",
        json_schema_extra={
            "element_property": True,
        },
    )

    memberState: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="memberState",
        title="A member or part of this molecule.",
        description="A member or part of this molecule.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    representation: typing.List[fhirtypeextra.MolecularDefinitionRepresentationType] = Field(  # type: ignore
        None,
        alias="representation",
        title="...",
        description="The representation of this molecular definition, e.g., as a literal or repeated elements.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequencePlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "type",
            "location",
            "memberState",
            "representation",
        ]

class MolecularDefinitionLocation(backboneelement.BackboneElement):


    __resource_type__ = "MolecularDefinitionLocation"

    sequenceLocation: fhirtypeextra.MolecularDefinitionLocationSequenceLocationType = Field(  # type: ignore
        None,
        alias="sequenceLocation",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    featureLocation: typing.List[fhirtypeextra.MolecularDefinitionLocationFeatureLocationType] = Field(  # type: ignore
        None,
        alias="featureLocation",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRelativePlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLocation",
            "featureLocation",
        ]

class MolecularDefinitionLocationSequenceLocation(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionLocationSequenceLocation"

        
    sequenceContext: fhirtypes.ReferenceType= Field(  # type: ignore
        ...,
        alias="sequenceContext",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    coordinateInterval: typing.List[fhirtypeextra.MolecularDefinitionLocationSequenceLocationCoordinateIntervalType] = Field( # type: ignore
        None,
        alias="coordinateInterval",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    strand: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="strand",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["Forward", "Reverse"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceContext",
            "coordinateInterval",
            "strand",
        ]

class MolecularDefinitionLocationSequenceLocationCoordinateInterval(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionLocationSequenceLocationCoordinateInterval"

    numberingSystem: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias= "numberingSystem",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    startQuantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="startQuantity",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e sequence[x]
            "one_of_many": "start",
            "one_of_many_required": False,
        },
    )

    startRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="startRange",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e sequence[x]
            "one_of_many": "start",
            "one_of_many_required": False,
        },
    )
    
    endQuantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="endQuantity",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e sequence[x]
            "one_of_many": "end",
            "one_of_many_required": False,
        },
    )

    endRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="endRange",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e sequence[x]
            "one_of_many": "end",
            "one_of_many_required": False,
        },
        
    )
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "numberingSystem",
            "startQuantity",
            "startRange",
            "endQuantity",
            "endRange",
        ]
    
    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "start": [
                "startQuantity",
                "startRange",
            ],
            "end": [
                "endQuantity",
                "endRange"
            ]
        }
        return one_of_many_fields
    
class MolecularDefinitionLocationFeatureLocation(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionLocationFeatureLocation"


    geneId: fhirtypes.CodeableConceptType =  Field(  #type: ignore
        None,
        alias="geneId",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "geneId",
        ]

class MolecularDefinitionRepresentation(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentation"

    
    focus: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="focus",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="code",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        },
    )
    # getting rid of list:typing.List[]
    literal: fhirtypeextra.MolecularDefinitionRepresentationLiteralType= Field(  # type: ignore
        None,
        alias="literal",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    # getting rid of list:typing.List[]
    resolvable: fhirtypes.AttachmentType= Field(  # type: ignore
        None,
        alias="resolvable",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        },
    )
    # getting rid of list:typing.List[]
    extracted: fhirtypeextra.MolecularDefinitionRepresentationExtractedType = Field(  # type: ignore
        None,
        alias="extracted",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    # getting rid of list:typing.List[]
    repeated: fhirtypeextra.MolecularDefinitionRepresentationRepeatedType = Field(  # type: ignore
        None,
        alias="repeated",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    # getting rid of list:typing.List[]
    concatenated: fhirtypeextra.MolecularDefinitionRepresentationConcatenatedType = Field(  # type: ignore
        None,
        alias="concatenated",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    # getting rid of list:typing.List[]
    relative: fhirtypeextra.MolecularDefinitionRepresentationRelativeType = Field(  # type: ignore
        None,
        alias="relative",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "focus",
            "code",
            "literal",
            "resolvable",
            "extracted",
            "repeated",
            "concatenated",
            "relative",
        ]

class MolecularDefinitionRepresentationLiteral(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationLiteral"


    encoding: fhirtypes.CodeableConceptType = Field(  #type: ignore
        None,
        alias="encoding",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        },
    )

    value: StringType = Field(  #type: ignore
        ...,
        alias="value",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "encoding",
            "value",
        ]

class MolecularDefinitionRepresentationExtracted(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationExtracted"


    startingMolecule: fhirtypes.ReferenceType = Field(  #type: ignore
        ...,
        alias="startingMolecule",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    start: IntegerType = Field(  #type: ignore
        ...,
        alias="start",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True
        }
  
    )

    end: IntegerType = Field(  #type: ignore
        ...,
        alias="end",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True
        }
    )

    coordinateSystem: fhirtypes.CodeableConceptType = Field(  #type: ignore
        ...,
        alias="coordinateSystem",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True
        }
    )
    
    reverseComplement: BooleanType = Field(  #type: ignore
        None,
        alias="reverseComplement",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True
        }
    )


    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "startingMolecule",
            "start",
            "end",
            "coordinateSystem",
            "reverseComplement",
        ]

class MolecularDefinitionRepresentationRepeated(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationRepeated"

    sequenceMotif: typing.List[fhirtypes.ReferenceType] = Field(  #type: ignore
        ...,
        alias="sequenceMotif    ",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    copyCount: IntegerType = Field(  #type: ignore
        ...,
        alias="copyCount",
        title="...",
        description=(None),
        json_schema_extra={
            "element_property": True,
        }
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceMotif",
            "copyCount",
        ]

class MolecularDefinitionRepresentationConcatenated(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationConcatenated"

    
    sequenceElement: typing.List[fhirtypeextra.MolecularDefinitionRepresentationConcatenatedSequenceElementType] = Field(  #type: ignore
        None,
        alias="sequenceElement",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceElement",
        ]

class MolecularDefinitionRepresentationConcatenatedSequenceElement(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationConcatenatedSequenceElement"


    sequence: fhirtypes.ReferenceType = Field(  #type: ignore
        ...,
        alias="sequence",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    ordinalIndex: IntegerType = Field(  #type: ignore
        ...,
        alias="ordinalIndex",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "ordinalIndex",
        ]

class MolecularDefinitionRepresentationRelative(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationRelative"

    startingMolecule: fhirtypes.ReferenceType = Field(  #type: ignore
        ...,
        alias="startingMolecule",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    edit: typing.List[fhirtypeextra.MolecularDefinitionRepresentationRelativeEditType] = Field(  #type: ignore
        None,
        alias="edit",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "startingMolecule",
            "edit",
        ]

class MolecularDefinitionRepresentationRelativeEdit(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentationRelativeEdit"

        
    editOrder: IntegerType = Field(  #type: ignore
        None,
        alias="editOrder",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    coordinateSystem: fhirtypes.CodeableConceptType = Field(  #type: ignore
        ...,
        alias="coordinateSystem",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    start: IntegerType = Field(  #type: ignore
        ...,
        alias="start",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    end: IntegerType = Field(  #type: ignore
        ...,
        alias="end",
        title="...",
        description=None,
       json_schema_extra={
            "element_property": True,
        },
    )

    replacementMolecule: fhirtypes.ReferenceType = Field(  #type: ignore
        ...,
        alias="replacementMolecule",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    replacedMolecule: fhirtypes.ReferenceType = Field(  #type: ignore
        None,
        alias="replacedMolecule",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["MolecularDefinition"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "editOrder",
            "coordinateSystem",
            "start",
            "end",
            "replacementMolecule",
            "replacedMolecule",
        ]

