# DraftCoreDataModel
Draft of CoreDataModel 

To be able to interact with the notebooks in this repository, please click the tag: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/InformaticsGenomicMedicine/DraftCoreDataModel.git/dev-sb)

A few things to note: 
* Mybinder may take a few minutes to load up.
* Mybinder session will be disablled when the user logs fof or become inactive for more than a few minutes.
* You are able to edit the files but once the mybinder tab is closed NONE of the changes will be saved. 
* Only way to save changes that were made in mybinder is by downloading the file the changes were made to.
* File: notebooks/databse_examples.ipynb is currently not working because it is configured to my local database.


###### THINGS TO THINK ABOUT
* What is lost but can be derived? What is lost and can not be derived or recovered?



#### NOTE: This is the current structure
notebooks/
src/
    │   
    ├── api/
    │   ├── __init__.py
    │   ├── ncbi_variation_services_api.py
    │   ├── seqrepo_api.py
    │   └── vicc_api.py
    │ 
    ├── database/
    │   ├── __init__.py
    │   └── database_extract.py
    │  
    ├── fhir/
    │  
    │  
    ├── hgvsExtra/
    │   ├── __init__.py
    │   ├── hgvs_utils.py
    │   └── hgvs_validation.py
    │  
    ├── spdi/
    │   ├── __init__.py
    │   ├── spdi_class.py
    │   └── spdi_utils.py
    │  
    ├── vrs/
    │   ├── __init__.py
    │   └── vrs_utils.py
    |
    ├── __init__.py
    |
    ├── core_variant_translate.py
    |
    ├── core_variant.py
test/

|
└── main.py
