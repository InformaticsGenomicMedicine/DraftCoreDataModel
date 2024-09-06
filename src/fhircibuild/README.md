## MolecularDefinition FHIR Resource Overview

This project implements a sample FHIR resource called **MolecularDefinition** using the `fhir-core` and `fhir.resources` packages. The resource definition is based on the [**MolecularDefinition** from the FHIR CI-Build](https://build.fhir.org/branches/cg-im-moldef_work_in_progress_2/moleculardefinition.html). The functionality is provided through two Python modules: `moleculardefinition.py` and `fhirtypesextra.py`, located in the `resource` folder. 

While this version of the MolecularDefinition resource covers most aspects outlined in the [FHIR CI-Build](https://build.fhir.org/branches/cg-im-moldef_work_in_progress_2/moleculardefinition.html), the `cytobandLocation` attribute is not yet included and will be added in a future update. This implementation allows you to create and manipulate MolecularDefinition FHIR resources in Python and aligns with the evolving FHIR specification.

## Project Goals

The goal of this project is to develop and implement the `MolecularDefinition` resource in Python, with a focus on enabling translations between HL7 FHIR and Variation Representation Specification (VRS) version 1.3. The key objectives are:

- **Implementing the `MolecularDefinition` Resource**: Create the `MolecularDefinition` resource in Python using the `fhir-core` and `fhir.resources` packages.
- **Developing Bidirectional Translations**: Create translations between HL7 FHIR and VRS version 1.3 to ensure data interoperability.
- **Providing Educational Notebooks**: Develop comprehensive notebooks that explain the `MolecularDefinition` resource and showcase the bidirectional translations between FHIR and VRS.
- **Accessibility via GitHub Codespaces**: The project is accessible through GitHub Codespaces, enabling users to explore the notebooks and interact with the code in an integrated development environment.

## Current Work and Capabilities

Currently, in the `src/fhircibuild/notebooks` directory, you will find JSON examples and Jupyter notebooks related to the `MolecularDefinition` resource implementation. Specifically:

- **JSON Examples**: Located in the `src/fhircibuild/notebooks` directory, This directory will store JSON examples of the `MolecularDefinition` resource.
- **Jupyter Notebooks**:
  - `moldef_example_1.ipynb`: Illustrates how to create the `simple_sequence_example.json` using the MolecularDefinition Python implementation.
  - `literal_example.ipynb`: Demonstrates the process of translating a VRS Literal Sequence Expression to a FHIR Sequence profile (literal representation).

While initial translational mappings between VRS and FHIR have been established, a comprehensive Python implementation of the translation framework is still a work in progress. The existing notebooks and examples highlight the foundational work and offer insights into the ongoing development efforts for these translation capabilities. Future work will focus on developing additional examples and notebooks, as well as completing the bidirectional translations between FHIR and VRS.







