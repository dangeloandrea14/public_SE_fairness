# Network Analysis

This is the code to compute Homophily, Clustering Coefficient and Modularity on the network graphs.

The folder is structured as follows:

- **data**: contains the data used by the scripts:
  - **ita_software_eng.csv**: contains the dataset on Italian Software Engineers, with the bibliometrics stats obtained from scopus
  - **italian_se_edges.csv**: is the DataFrame version of the graph we employed for Network Analysis on the Italian SE community
  - **worldwide_se.csv**: contains the total dataset on Software Engineers, with the bibliometrics stats obtained from scopus
  - **worldwide_se_edges.csv**: is the DataFrame version of the graph we employed for Network Analysis on the Worldwide SE community.
- **net_analysis.ipynb**: this is the code to compute Homophily, Clustering Coefficient and Modularity on the network graphs. We only include the code for the worldwide community, but it is the same for the Italian community.
- **mean_metrics.ipynb**: this notebook contains the code to evaluate mean statistics on publications and citations for each gender group.
