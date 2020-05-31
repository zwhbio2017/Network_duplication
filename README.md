# Network_duplication

This repository contains code and files that are required to repeat the simulation we did in our paper. Running these scripts will generate the results of our simulation, calculate k mean, visualize network, and perform linear regression on the network data. 

> Code by Weihao Zhao

## Prerequisites

These scripts were run on Python 3.8.0. Other packages, including their versions, are listed below: 

```
numpy         1.18.4

pandas        1.0.3

scikit-learn  0.23.1

matplotlib    3.2.1

networkx      2.4
```

## Run the simulation

### Duplication network

The command to run the simulation of duplication network is: 

```
python Run_SimpleNetwork.py <parameter> <time>
```

#### Parameters

`<parameter>`: You can choose different parameters for the SimpleNetwork. Possible values: {2002, 2003}, corresponding to different parameters used in previous papers.
  
`<time>`: You can choose to extract different network information of different iteration time. Possible values: {1-100}, corresponding to iteration times, default 100.
  
#### Output

This command will output files in `File` directory named with SimpleNetwork, including network information of desired iteration (Named `SimpleNetwork_network_result_<parameter>.txt`) and connection number of nodes after 100, 500, and 1000 times of duplication (Named `SimpleNetwork_connection_result_<time>_<parameter>.txt`). 

Network information is stored in the file while every column and row represents a certain node and every 1 represents connection between two nodes.

Connection result is stored in the file while the first column represents connection number of a node, and other columns represents node number with certain connection number in each iteration.

### Random network

The command to run the simulation of random network is: 

```
python Run_RandomNetwork.py
```

This command has no parameters and the output is similar to the simulation of duplication network.

## Calculate k mean

The command to calculate k mean is: 

```
python Network_k_mean.py <node_number> <network_type> <parameter>
```

#### Parameters

`<node_number>`: You can choose certain node number for connection result. Possible values: {100, 500, 1000}.

`<network_type>`: You can choose which kind of network data you will be using. Possible values: {SimpleNetwork, RandomNetwork}.

`<parameter>`: You can choose different parameters for the SimpleNetwork. Possible values: {2002, 2003}, corresponding to different parameters used in previous papers. (Not required for RandomNetwork)
  
#### Output

The command will output k mean value for the connection result.

## Perform linear regression

The command to perform linear regression is: 

```
python Network_regression.py <node_number> <network_type> <parameter>
```

#### Parameters

`<node_number>`: You can choose certain node number for connection result. Possible values: {100, 500, 1000}.

`<network_type>`: You can choose which kind of network data you will be using. Possible values: {SimpleNetwork, RandomNetwork}.

`<parameter>`: You can choose different parameters for the SimpleNetwork. Possible values: {2002, 2003}, corresponding to different parameters used in previous papers. (Not required for RandomNetwork)
  
#### Output

The command will output a graph with black dots indicating data point and blue lines indicating lines fitted for the data. Also it will output the R^2 value of linear regression model.

## Visualize network

The command to visualize network is: 

```
python Network_visualize.py <node_number> <network_type> <parameter>
```

#### Parameters

`<node_number>`: You can choose certain node number for connection result. Possible values: {100, 500, 1000}.

`<network_type>`: You can choose which kind of network data you will be using. Possible values: {SimpleNetwork, RandomNetwork}.

`<parameter>`: You can choose different parameters for the SimpleNetwork. Possible values: {2002, 2003}, corresponding to different parameters used in previous papers. (Not required for RandomNetwork)
  
#### Output

This command will output a graph with the visualization of the network.
