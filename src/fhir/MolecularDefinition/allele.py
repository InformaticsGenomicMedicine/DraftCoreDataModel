from pydantic import BaseModel,Field
import typing

class MolecularDefinitionAllele(BaseModel):

    resource_type: typing.Literal['Allele'] = Field("Allele", description="MUST be 'Allele' ")

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

    location: typing.List = Field(
        None,
        alias="location",
        title="Location of this molecule",
        description="The molecular location of this molecule.",
        # if property is element of this resource.
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