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
