## Fairness Project

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)



This is the repository for the submitted paper "xx".

# Datasets

The datasets are publicly available here (link).
Download them and put them in a folder named "processed_data" for seamless execution of the scripts.

------

The structure of this project is the following:

# Root
1. [environment.yml](#env)
2. [from_dataset_to_graph.ipynb](#graph)
3.  Network_Analysis 
    1. [Net Analysis](#net_analysis)
    2. [Mean_metrics](#meanmetrics)
4.  Disparate_Impact 
    1. [publications.ipynb](#di)
    2. [metrics.py](#metrics)

<a name="env"></a>
### Environment

environment.yml includes all the necessary requirements to execute the code in this repository. If you have conda installed, you can execute:

``` conda install -f environment.yml``` 

on your terminal to create an environment called "fairness" with all the requirements included. Don't forget to activate the environment after.

<a name="graph"></a>
### from_dataset_to_graph.ipynb

This notebook includes the necessary code to transform the source dataset into a Networkx-compatible dataset, which is later used to create the graph.

<a name="net_analysis"></a>
### network_analysis/net_analysis.ipynb

This is the code to compute Homophily, Clustering Coefficient and Modularity on the network graphs. We only include the code for the worldwide community, but it is the same for the Italian community.

<a name="net_analysis"></a>
### network_analysis/mean_metrics.ipynb

This script contains the code to evaluate mean statistics on publications and citations for each gender group.

<a name="di"></a>
### Disparate_impact/publications.ipynb

This is the code to compute the metrics for the best performing researchers on the field. The code for plotting the graphs is also included.

<a name="metrics"></a>
### Disparate_impact/metrics.py

Helper class containing the definition of Disparate Impact.