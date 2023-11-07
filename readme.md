# Evaluation of Gender Bias within the Software Engineering Community

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This is the repository containing the data and the replication package of the experiments described in the paper _Uncovering Gender Bias in Academia: A Comprehensive Analysis within the Software Engineering Community_.

---

The structure of this project is the following:

1. [environment.yml](#env)
2. [literature_review.csv](#litrev)
3. [network_analysis](./network_analysis/README.md)
4. [Disparate_impact](./Disparate_impact/README.md)

### Environment <a name="env"></a>

environment.yml includes all the necessary requirements to execute the code in this repository. If you have conda installed, you can execute:

` conda install -f environment.yml`

on your terminal to create an environment called "fairness" with all the requirements included. Don't forget to activate the environment after.

### literature_review.csv <a name="litrev"></a>

This file contains details on the 49 papers that are part of the Literature Review presented in our work.

### from_dataset_to_graph.ipynb

This notebook includes the necessary code to transform the source dataset into a Networkx-compatible dataset, which is later used to create the graph.
