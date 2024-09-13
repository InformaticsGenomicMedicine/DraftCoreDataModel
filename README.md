# DraftCoreDataModel

Welcome to the DraftCoreDataModel repository. This repository contains an alpha version of the CoreVariantClass and GoldStandardDatabase. The CoreVariantClass is an internal core class developed to facilitate seamless bidirectional translations between various standards, including FHIR, VRS, SPDI, and HGVS. This repository also includes bidirectional translations between VRS and SPDI, HGVS and VRS, and SPDI and HGVS. These translations are achieved using external packages and APIs acknowledged bellow. The GoldStandardDatabase (GSDB) is a human-curated database designed to provide reliable and accurate data for various applications. This repository is in the early stages of development and may undergo occasional changes as progress is made.


## Interacting with Notebooks

To interact with the DraftCoreDataModel, there's no need to install or clone the repository. Instead, you can use GitHub Codespaces to access and work with the Jupyter Notebooks directly. If you plan to make changes, please fork the repository and submit your suggestions or modifications via an issue and a pull request. Personal accounts receive 120 free hours of Codespaces usage, while Pro accounts receive 180 hours. Be aware that Codespaces has a default timeout period of 30 minutes. For more information about Codespaces, refer to the links provided below. If you're already familiar with Codespaces and Jupyter Notebooks, you can proceed with the instructions below.

If you're new to using **Codespaces**, the following resources may be helpful:
- [Codespaces Overview](https://docs.github.com/en/codespaces/overview)
- [Codespaces Getting Started Documentation](https://docs.github.com/en/codespaces/getting-started/quickstart)

## Access Jupyter Notebooks in Github Codespace. 

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=issue-dev-sb&repo=670718709&skip_quickstart=true&machine=standardLinux32gb&geo=UsEast)

## 1. Starting Codespace
- Begin by clicking the **Codespaces** badge above to get started.
- A prompt to build a Codespace will appear with certain specifications.
- Click on **Create Codespace**.
- **Note:** It may take a few minutes to build your virtual machine.

## 2. Selecting a Kernel
- Navigate to the notebooks and select the one you wish to run.
- Locate the **Select Kernel** option on the top right-hand side of the interface.
- Click on **Select Kernel**.

## 3. Choosing a Python Environment
- After clicking **Select Kernel**, choose **Python Environment...**.
- From the dropdown menu, select the Pipenv environment labeled `DraftCoreDataModel-`.

## 4. Running Notebooks
- Once the appropriate kernel is selected, you can proceed to run the cells within the Jupyter notebooks.

## 5. Deactivating Codespace
- In the bottom left corner of your browser, click on **Codespaces**.
- Select **Stop Current Codespace** (this process may take a few minutes).
- Once completed, your Codespace will be successfully deactivated.

## 6. Reactivating Codespace
- Navigate back to the GitHub repository.
- Click the green **Code** button.
- Select the **Codespaces** tab.
- Under the "On other branches" section, click the meatball menu (three vertical dots) and choose **Open in Browser**.

## Running pytest scripts inside of Codespace

To run pytest scripts within a Codespace environment the following steps need to be followed:

### 1. Activate the pipenv virtual environment:

To execute the test scripts, it is essential to ensure that you are operating within the virtual environment configured by Pipenv.

```shell
# Activate pipenv virtual environment
pipenv shell
```
### 2. Navigate to the test directory:

Change your directory to the test folder where your test files are located.

```shell
cd test
```

### 3. Run the pytest command:

Once the virutal environment is activated, navigate to the test directory via the terminal. You can then execute pytest by specifying the particular files you intend to test.

```shell
# Execute the specified test file 
pytest file_name.py
```


## Acknowledgments
This project utilizes several external packages and APIs. The following packages were used:

- **[vrs-python](https://github.com/ga4gh/vrs-python)**
- **[biocommons.seqrepo](https://github.com/biocommons/biocommons.seqrepo)**
- **[biocommons.uta](https://github.com/biocommons/uta)**
- **[hgvs](https://github.com/biocommons/hgvs)**
- **[NCBI Variation Services](https://api.ncbi.nlm.nih.gov/variation/v0/)**
- **[HL7 FHIR](https://build.fhir.org/branches/cg-im-moldef_work_in_progress_2/moleculardefinition.html)**

<!--
---

## Access Notebooks (MyBinder)

**Note:** MyBinder is currently undergoing maintenance, and access to notebooks may be limited. We apologize for any inconvenience.

- Link for issue-dev-sb branch: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/InformaticsGenomicMedicine/DraftCoreDataModel/issue-dev-sb)
<!--
- Link for dev-sb branch: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/InformaticsGenomicMedicine/DraftCoreDataModel.git/dev-sb)
-->
<!--
## Notes:
- MyBinder sessions may take a few minutes to load.
- Sessions will be disabled if the user logs off or becomes inactive for an extended period.
- While you can edit files during the session, changes won't be saved once the MyBinder tab is closed.
- To preserve changes made in MyBinder, remember to download the modified files before closing the session.
- Please note that the file `notebooks/databse_examples.ipynb` is currently non-functional due to configuration issues with a local database. We are working on resolving this.

Thank you for your patience and understanding! If you encounter any issues or have questions, feel free to reach out.

---
<!--
## TODO: Future Implementation: Access Notebooks (VSCODE)



### Access Notebooks (VSCODE)

To get started with the project, follow these steps to clone the repository to your local machine:

1. **Open Terminal (Mac/Linux) or Command Prompt (Windows):**
   - On macOS, you can use Terminal. On Windows, you can use Command Prompt or Git Bash if Git is installed.
   - Navigate to the directory where you want to clone the repository.

2. **Copy Clone URL:**
   - On GitHub, navigate to the repository you want to clone.
   - Click on the "Code" button.
   - Copy the HTTPS or SSH URL provided.

3. **Clone the Repository:**
   - In your Terminal or Command Prompt, use the `git clone` command followed by the repository URL you copied.
     ```
     git clone <repository_URL>
     ```
   - Paste the URL you copied after `git clone` command and press Enter.
   
4. **Prerequisite**
   - Before proceeding, make sure you have the following installed:
     - [Visual Studio Code](https://code.visualstudio.com/download)
     - [Docker Desktop](https://www.docker.com/)
   - Once you have Visual Studio Code installed, you will need to click on the Extension icon in the Activity Bar on the left-hand side. In the "Search Extensions in Marketplace," type "Dev Containers." The Extension should look like this: [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Then go ahead and click install inside of your VS Code. 

3. **Connect to the Dev Container**
   -


4. **Working in the inside of the notebooks**

---

-->
