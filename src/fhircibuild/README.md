## MolecularDefinition FHIR Resource Overview

This project implements a sample FHIR resource called **MolecularDefinition**, designed based on the [**MolecularDefinition resource** from the FHIR CI-Build](https://build.fhir.org/branches/cg-im-moldef_work_in_progress_2/moleculardefinition.html). The resource was built using existing Python packages, specifically `fhir-core` and `fhir.resources`, to create two custom modules: `moleculardefinition.py` and `fhirtypesextra.py`, both of which reside in the `resource` folder.

While this version of the MolecularDefinition resource covers most aspects outlined in the [**MolecularDefinition resource** from the FHIR CI-Build](https://build.fhir.org/branches/cg-im-moldef_work_in_progress_2/moleculardefinition.html), the `cytobandLocation` attribute is not yet included and will be added in a future update. This implementation allows you to create and manipulate MolecularDefinition FHIR resources in Python and aligns with the evolving FHIR specification.

**Disclaimer**: The MolecularDefinition resource and its Python implementation are subject to change as development progresses. This project showcases the current version.

## Project Goals

The goal of this project is to develop and implement the `MolecularDefinition` resource in Python, with a focus on enabling translations between HL7 FHIR and Variation Representation Specification (VRS) version 1.3. The key objectives are:

- **Implementing the `MolecularDefinition` Resource**: Develop a Python implementation of the `MolecularDefinition` resource.
- **Developing Bidirectional Translations**: Create translations between the HL7 FHIR `MolecularDefinition` resource and VRS (version 1.3) to ensure data interoperability.
- **Providing Educational Notebooks**: Develop comprehensive notebooks that explain the `MolecularDefinition` resource and showcase the bidirectional translations between HL7 FHIR `MolecularDefinition` resource and VRS.
- **Accessibility via GitHub Codespaces**: The project will be accessible through GitHub Codespaces, enabling users to explore the notebooks and interact with the code in an integrated development environment.

## Current Work and Capabilities

Currently, in the `src/fhircibuild/notebooks` directory, you will find JSON examples and Jupyter notebooks related to the `MolecularDefinition` resource implementation. Specifically:

- **JSON Examples**: Located in the `src/fhircibuild/notebooks` directory, This directory will store JSON examples of the `MolecularDefinition` resource.
- **Jupyter Notebooks**:
  - `moldef_example_1.ipynb`: Illustrates how to create the `simple_sequence_example.json` using the MolecularDefinition Python implementation.
  - `literal_example.ipynb`: Demonstrates the process of translating a VRS Literal Sequence Expression to a FHIR Sequence profile (literal representation).

HL7 FHIR Molecular Definition to GA4GH Variation Representation Specification (VRS) Mapping

The [FHIR_MolDef-VRS_1.3_Mappings.xlsx](src/fhircibuild/FHIR_MolDef-VRS_1.3_Mappings.xlsx) file illustrates the mapping between MolecularDefinition and VRS version 1.3. The following section explains what the different colors represent: 

- **Green**: indicates that a mapping exists, but it does not imply a one-to-one relationship. A single element from VRS may be represented by multiple elements in FHIR due to FHIR’s structured approach and data types. 
- **Red**: indicates that there is no corresponding match yet. 
- **Yellow**: indicates that the mapping is not complete or fully accurate.

**_Please note:_**  The mapping is a work in progress and may be subject to changes, corrections, and updates.

While initial translational mappings between VRS and FHIR have been established, a comprehensive Python implementation of the translation framework is still a work in progress. The existing notebooks and examples highlight the foundational work and offer insights into the ongoing development efforts for these translations. Future work will focus on developing additional examples and notebooks, as well as completing the bidirectional translations between HL7 FHIR and GA4GH VRS.







