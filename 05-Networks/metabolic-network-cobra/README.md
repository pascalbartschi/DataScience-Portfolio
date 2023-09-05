# About

This directory hold network analyses of metabolic network with the python library *conda*. It summarizes what approaches I learnt to perform with this library.

# Contents

### [Toy-model](toy-model-introduction.ipynb)

In this notebook we explore the basic functions of the cobra library and common tools of network flow analysis such as FBA or FVA. A toy model is implemented from scratch to get a feeling for the total workflow of analysing networks.

### [E. coli core metabolism](ecolicore-metabolism-analysis.ipynb)

Here, we analyse the E-coli core metabolism. We0 used data from the research of [Orth et al, 2010](https://pubmed.ncbi.nlm.nih.gov/26443778/) and available in the [BiGG database](http://bigg.ucsd.edu/models/e_coli_core). You can find a graphical description of the model in this picture:

We analyses the relationship between the use of different carbon sources and biomass production

### [Biomass growth in genome scale network](genome-scale-network-analysis.ipynb)

In this analysis we try to identify the molecular components of a cell (protein, DNA, RNA, lipids) whose precursors need the greatest amounts of resources for their synthesis. Different networks were prepared with different growth objectives, either missing a major component or only focusing on one.
We focus on analysing output of molecular components in different modified networks. The highlight of this analysis is the classification of essential reactions into subsystems of compartment use.

### [E. coli iJO1366 analysis](ecoli_iJO1366_analysis.ipynb)

In this analysis we explore the metabolism of E. coli with the [iJO1366](http://bigg.ucsd.edu/models/iJO1366) network from the BIGG database.
We study:
* the effects of employing different metabolites as carbon source
* identify subsystems of essential reactions
* performance in different minimal environments
* compare minimal with rich environments
comparing minimal glucose and acetate environments
rich environments
carbon sources
