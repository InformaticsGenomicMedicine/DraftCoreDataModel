### Module Overview

#### 1) api Directory

* The api directory currently comprises of three modules: ncbi_variation_services_api.py, seqrepo_api.py, and vicc_api.py. Each of these modules is designed to establish connections with specific APIs for retrieving targeted information.

    * The variation_norm_api.py module utilizes resources developed by the Variant Interpretation for Cancer Consortium (VICC) (citation: https://normalize.cancervariants.org/ and https://normalize.cancervariants.org/variation). This API is essential in converting HGVS, gnomAD VCF, or free-text variations on the GRCh37 or GRCh38 assembly to VRS Variation. This endpoint is capable to handle expressions beyond the current scope of the vrs-python translator module (cite: https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/extras/translator.py). It can create VRS text objects for expressions that may not be translatable or normalizable.
        *Methods:
            * variation_to_vrs()
    * The ncbi_variation_services_api.py module interfaces with resources developed by the National Institute of Health (NIH) Variation Services (citation: https://api.ncbi.nlm.nih.gov/variation/v0/). Leveraging this resources facilitates validation and translation methods currently not implemented in vrs-python translator module (cite: https://github.com/ga4gh/vrs-python/blob/main/src/ga4gh/vrs/extras/translator.py). This API facilitates various methods, including the validation of SPDI expressions, the translation of SPDI expressions to right-shift HGVS expressions, and the translation of HGVS expressions to SPDI expressions. 
        * Methods: 
            * validate_spdi()
            * spdi_to_hgvs()
            * hgvs_to_spdi()
    * The seqrepo_api.py module establishes connection with the SeqRepo REST API provided by Biocommons (citation: https://biocommons.org/). Within this module, the SeqRepoAPI class is initialized with the specified SeqRepo REST service URL. The SeqRepo REST API serves as an interface for retrieving biological sequences and associated metadata. These sequences and metadata are crucial for performing translations, normalizations, and identifications. 


#### 2) database Directory

* database_extract.py 

    * A local demo database in PostgreSQL was created to house a set of sample data points. The module's purpose is centered around connecting to this database, retrieving examples, and translating the sample data into CoreVariantClass. Two distinct extraction methods are available: one utilizing the rowId, and the other involving the retrieval of all examples existing in the database.
        * Methods:
            * getExample()
            * getAllExamples()
            * db_to_cvc()
    * Future goals: Create a larger sample dataset, which will then be utilized to generate examples for notebook demonstrations and testing purposes.
    

#### 3) fhir Directory

* The file contains mappings between VRS (Variant Representation Specification) and FHIR (Fast Healthcare Interoperability Resources) molecular sequence mappings in JSON format. Our intention is to create translation methods that bridge VRS and FHIR in the upcoming stages. The development of MolecularSequence R5 Plus has taken place in a separate repository, and you can find the relevant code at the following citation: https://github.com/SalemBajjali/fhir.resources/blob/molseqplus_dev_sb/fhir/resources/molecularsequenceplus.py. This code reflects the enhancements and modifications made to the MolecularSequence resources, as outlined in the following citation: https://build.fhir.org/branches/cg-im-molseq-work_in_progress_2/molecularsequence.html.


#### 4) hgvsExtra Directory 

* hgvs_validation.py
    * Designed as an HGVS expression validator, this Python script leverages the biocommons hgvs library for parsing and validating HGVS expressions. It operates on input files in either Excel or CSV format, containing a column of HGVS examples. The script was designed to compare the expected pass/fail outcomes, as curated by humans, with the results produced by the biocommons hgvs library.

* hgvs_utils.py 
    * The hgvs_utils.py module initializes connections to SeqRepo and VarNormAPI and utilizes the biocommons hgvs library for validating HGVS expressions. The module was created to facilitate translations, converting HGVS expressions to both SPDI and VRS formats. The translation from HGVS to SPDI is performed using the ncbi_variation_services_api.py, while the translation from HGVS to VRS utilizes the vicc_api.py.
        * Methods: 
            * from_hgvs_to_vrs()
            * from_hgvs_to_spdi()


#### 5) spdi Directory

* spdi_class.py
    * The spdi_class.py module was created to define an SPDI class object representing the Sequence Position Deletion Insertion format. This class utilizes the ncbi_variation_services_api.py module to validate the SPDI object. The module includes methods for converting the SPDI object to either a string or a dictionary.

* spdi_utils.py
    * The spdi_utils.py module was created to facilitate translations, converting SPDI expressions to both right-shifted HGVS expressions and Variation Representation Specification (VRS) expressions.For the SPDI to HGVS translation, the module utilizes the NCBI API and the biocommons hgvs package, offering a method that allows for optional validation and flexible output formatting, supporting both string and parsed HGVS object representations. In the SPDI to VRS translation, the module employs the vrs-python translator module, which utilizes the SeqRepoAPI. This method also supports validation and multiple output formats (object, dictionary, or JSON).
        * Methods:
            * from_spdi_to_rightshfit_hgvs()
            * from_spdi_to_vrs()

#### 6) vrs Directory
# Relook at
* vrs_utils.py 
    * The vrs-python translator module currently has implementation to convert vrs objects to spdi and normalized hgvs expression. Using the current framework we added the ability to input  either a VRS dictionary or object, and additional measures have been implemented to handle potential translation errors and exceptions more effectively.
        * Method: 
            * from_vrs_to_spdi()
            * from_vrs_to_normalized_hgvs()


#### 7) core_variant_translate.py

* The core_variant_translate module relies on other mentioned modules within this readme, along with external Python packages, to execute various translations. Main objective is the translation of various variations (SPDI, HGVS, VRS) into a CoreVariantClass object and vice versa. By leveraging the functionalities provided by the associated modules and external packages, the core_variant_translate module serves as a crucial component in the bi-directional translation of genomic variations, enabling seamless conversion between different representation formats.


#### 8) core_variant.py 

* The CoreVariantClass has been created to serve as a foundational schema for data storage in a database. Its design is meant for flexibility, allowing diverse variations such as SPDI, HGVS, and VRS to be generated from this central class. The core functionality of the CoreVariantClass extends beyond data storage; it provides a range of methods for representation, validation, and normalization of variations. This class plays a crucial role within the core_variant_translate module, facilitating bi-directional translations between various genomic variations. Furthermore, the CoreVariantClass has been architected with the future implementation of FHIR specifications in mind, currently residing in an alpha stage of development. 