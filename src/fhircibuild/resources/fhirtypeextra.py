from __future__ import annotations as _annotations


from fhir_core.types import create_fhir_type

MolecularDefinitionType = create_fhir_type(
    "MolecularDefinitionType", "src.fhircibuild.resources.moleculardefinition.MolecularDefinition"
)

MolecularDefinitionLocationType = create_fhir_type(
    "MolecularDefinitionLocationType","src.fhircibuild.resources.moleculardefinition.MolecularDefinitionLocation"
)

MolecularDefinitionLocationSequenceLocationType = create_fhir_type(
    "MolecularDefinitionLocationSequenceLocationType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionLocationSequenceLocation"
)

MolecularDefinitionLocationSequenceLocationCoordinateIntervalType = create_fhir_type(
    "MolecularDefinitionLocationSequenceLocationCoordinateIntervalType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionLocationSequenceLocationCoordinateInterval"
)

MolecularDefinitionLocationFeatureLocationType = create_fhir_type(
    "MolecularDefinitionLocationFeatureLocationType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionLocationFeatureLocation"
)

MolecularDefinitionRepresentationType = create_fhir_type(
    "MolecularDefinitionRepresentationType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentation"
)

MolecularDefinitionRepresentationLiteralType = create_fhir_type(
    "MolecularDefinitionRepresentationLiteralType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationLiteral"
)

MolecularDefinitionRepresentationExtractedType = create_fhir_type(
    "MolecularDefinitionRepresentationExtractedType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationExtracted"
)

MolecularDefinitionRepresentationRepeatedType = create_fhir_type(
    "MolecularDefinitionRepresentationRepeatedType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationRepeated"
)

MolecularDefinitionRepresentationConcatenatedType = create_fhir_type(
    "MolecularDefinitionRepresentationConcatenatedType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationConcatenated"
)

MolecularDefinitionRepresentationConcatenatedSequenceElementType = create_fhir_type(
    "MolecularDefinitionRepresentationConcatenatedSequenceElementType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationConcatenatedSequenceElement"
)

MolecularDefinitionRepresentationRelativeType = create_fhir_type(
    "MolecularDefinitionRepresentationRelativeType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationRelative"
)

MolecularDefinitionRepresentationRelativeEditType = create_fhir_type(
    "MolecularDefinitionRepresentationRelativeEditType",
    "src.fhircibuild.resources.moleculardefinition.MolecularDefinitionRepresentationRelativeEdit"
)


__all__ = [
    #New MolecularDefinition Values
    "MolecularDefinitionType",
    "MolecularDefinitionLocationType",
    "MolecularDefinitionLocationSequenceLocationType",
    "MolecularDefinitionLocationSequenceLocationCoordinateIntervalType",
    "MolecularDefinitionLocationFeatureLocationType",
    "MolecularDefinitionRepresentationType",
    "MolecularDefinitionRepresentationLiteralType",
    "MolecularDefinitionRepresentationExtractedType",
    "MolecularDefinitionRepresentationRepeatedType",
    "MolecularDefinitionRepresentationConcatenatedType",
    "MolecularDefinitionRepresentationConcatenatedSequenceElementType",
    "MolecularDefinitionRepresentationRelativeType",
    "MolecularDefinitionRepresentationRelativeEditType",
]