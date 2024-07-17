## Notebooks


### 1. Introduction to CoreVariantClass
The [CoreVariantClass](introduction_to_corevariantclass.ipynb) is an internal core class developed to facilitate seamless bidirectional translations between various standards, including FHIR, VRS, SPDI, and HGVS. This notebook provides an overview of the attributes of the CoreVariantClass, as well as the normalization method. The CoreVariantClass is currently in alpha stage and is subject to potential changes.

### 2. Introduction to GoldStandardDatabase
The [GoldStandardDatabase](introduction_to_database.ipynb) (GSDB) is a database developed for test suites to ensure software quality and reliability. The GSDB is a human-curated database designed to provide reliable and accurate data for various applications. It utilizes SQLite3 as the database management system due to its lightweight and serverless nature. The notebooks provide an overview of how to connect to the database, convert the data into a pandas DataFrame, and also provide methods to perform various functions on the database.

### 3. Explore CoreVariantClass Translator
The [CoreVariantClass Translator](cvc_translation_examples.ipynb) uses a combination of classes to perform bidirectional translations between: CVC <-> HGVS, CVC <-> SPDI, and CVC <-> VRS. The bidirectional translations between CVC and FHIR are currently in ongoing development, and there are no examples in the notebook yet. This notebook demonstrates how to utilize these scripts to perform the bidirectional translations. Currently, the translations are divided into two scripts, but they will be consolidated into one script in the future.

### 4 Exploring HGVS Translator 
The [HGVS Translator](hgvs_translation_examples.ipynb) notebook demonstrates bidirectional translations between HGVS <-> SPDI, HGVS <-> VRS, and HGVS <-> CVC. Translations to SPDI utilize the NCBI API, while translations to VRS utilize the vrs-python translator module. 

### 5 Exploring the SPDI Translator
The [SPDI Translator](spdi_translation_examples.ipynb) notebook demonstrates bidirectional translations between SPDI <-> HGVS, SPDI <-> VRS, and SPDI <-> CVC. Translations to HGVS utilize the NCBI API, while translations to VRS utilize the vrs-python translator module. Additionally, the notebook includes the developed SPDI class, designed for creating, validating, and representing an SPDI expression. 

### 6 Exploring VRS Translator 
The [VRS Translator](vrs_translation_examples.ipynb) notebook demonstrates bidirectional translations between VRS <-> SPDI, VRS <-> HGVS, and VRS <-> CVC. These translations are done utilize the vrs-python tranlator module in vrs 1.3. 






