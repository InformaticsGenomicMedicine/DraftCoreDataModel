from pydantic import BaseModel, Field
import typing

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