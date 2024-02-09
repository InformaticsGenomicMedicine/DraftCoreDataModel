from pydantic import BaseModel,Field
import typing

class MolecularDefinitionHaplotype(BaseModel):

    resource_type: typing.Literal['Haplotype'] = Field("Haplotype", description="MUST be 'Haplotype' ")

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

    memberState: typing.List = Field(
        None,
        alias="memberState",
        title="Member",
        description="A member or part of this molecule.",
        element_property=True,
    )