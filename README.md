# DraftCoreDataModel
Draft of CoreDataModel 

To be able to interact with the notebooks in this repository, please click the tag: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/InformaticsGenomicMedicine/DraftCoreDataModel.git/dev-sb)

A few things to note: 
* Mybinder may take a few minutes to load up.
* Mybinder session will be disablled when the user logs fof or become inactive for more than a few minutes.
* You are able to edit the files but once the mybinder tab is closed NONE of the changes will be saved. 
* Only way to save changes that were made in mybinder is by downloading the file the changes were made to.
* File: notebooks/databse_examples.ipynb is currently not working because it is configured to my local database.



src/
├── spdi/
│   ├── __init__.py
│   ├── spdi.py
│   ├── spdi_utils.py
│   ├── spdi_constants.py
│   ├── spdi_exceptions.py
│   ├── spdi_data.py
│   └── spdi_tests.py
├── vrs/
│   ├── __init__.py
│   ├── vrs.py
│   ├── vrs_utils.py
│   ├── vrs_constants.py
│   ├── vrs_exceptions.py
│   ├── vrs_data.py
│   └── vrs_tests.py
├── hgvs/
│   ├── __init__.py
│   ├── hgvs.py
│   ├── hgvs_utils.py
│   ├── hgvs_constants.py
│   ├── hgvs_exceptions.py
│   ├── hgvs_data.py
│   └── hgvs_tests.py
├── api/
│   ├── __init__.py
│   ├── api_client.py
│   ├── vrs_api.py
│   ├── hgvs_api.py
│   ├── spdi_api.py
│   └── api_tests.py
└── main.py
