### Module Overview

#### 1) api_class.py  

* The purpose of this module is to connect to two different APIs and retrieve information from specific endpoints. The first API is the Variation Services by NCBI, from which it fetches data from the endpoints (/spdi/{spdi}/hgvs) and (/hgvs/{hgvs}/contextuals). The second API is the VICC Variation Normalizer, and it fetches data from the endpoints (/variation/to_vrs).


#### 2) translate_class.py

* This module utilizes the methods in api_class.py to translate variations. If the API cannot translate a specific variation, it will return an error message along with the variation.

#### 3) core_variant.py 

* A class named CoreVariantClass has been created to store data in our database. It includes two methods, initParamValues and normalizedData, each with validation steps for their respective parameters. The initParamValues method returns a dictionary of the parameters inputted by the user, while the normalizedData method validates the initial parameters and returns a dictionary if the data meets the validation criteria.

#### 4) corevariantclass_to.py 

* The purpose of this module is to utilize the translate_class.py module to translate variations from CoreVariantClass to SPDI, right-shift HGVS, fully-norm HGVS, and VRS.

#### 5) database_extract.py 

* I have created a local demo database in PostgreSQL that includes a few sample data. The purpose of this module is to connect to this database, fetch examples from it, and translate the example data into CoreVariantClass. Data from this database can be extracted in two different ways: the first way is using rowId, and the second way is by extracting all examples available in the database.

