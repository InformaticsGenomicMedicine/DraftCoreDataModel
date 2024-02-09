from pydantic import BaseModel,Field
import typing

class MolecularDefinitionSequence(BaseModel):

    resource_type: typing.Literal['Sequence'] = Field("Sequence", description="MUST be 'Sequence' ")

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
    
    representation: typing.List = Field(
        None,
        alias="representation",
        title="Representation",
        description=(
            "The representation of this molecular definition, e.g., as a literal or repeated elements."
        ),
        element_property=True,
    )