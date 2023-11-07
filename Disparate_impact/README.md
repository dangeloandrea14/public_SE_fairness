# Disparate Impact Analysis

This folder contains the code to perform the Disparate Impact analysis on academic promotions within the Italian Software Engineering and informatics communities.

The folder is structured as follows:

- **data**: contains the data used by the scripts:
  - **ita_informatics.csv**: contains the dataset on Italian Informatics, with the bibliometrics stats obtained from scopus and academic career information obtained from MIUR;
  - **ita_software_eng.csv**: contains the dataset on Italian Software Engineers, with the bibliometrics stats obtained from scopus and academic career information obtained from MIUR;
- **metrics.py**: helper file containing the definition of Disparate Impact;
- **publications.ipynb**: this is the code to compute the disparate impact considering also the number of publications and citations
