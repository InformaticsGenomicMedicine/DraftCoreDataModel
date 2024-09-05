from pydantic import Field 
import typing
from fhir.resources import backboneelement, domainresource, fhirtypes # type: ignore
import src.fhircibuild.resources.fhirtypeextra as fhirtypeextra
from fhir_core.types import CodeType,StringType,BooleanType,IntegerType


class AlleleMolecularDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource MolecularDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Representation of a Molecular Definition.
    """
    __resource_type__ = "AlleleMolecularDefinition"

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
            "type",
            "location",
            "representation",
        ]
    
class MolecularDefinitionRepresentation(backboneelement.BackboneElement):

    __resource_type__ = "MolecularDefinitionRepresentation"

    
    allSlices: fhirtypeextra.MolecularDefinitionRepresentationLiteralType= Field(  # type: ignore
        None,
        alias="allSlices",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    contextState: fhirtypeextra.MolecularDefinitionRepresentationExtractedType = Field(  # type: ignore
        None,
        alias="contextState",
        title="...",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    alleleState: fhirtypeextra.MolecularDefinitionRepresentationRepeatedType = Field(  # type: ignore
        None,
        alias="alleleState",
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
            "allSlices",
            "contextState",
            "alleleState",
        ]