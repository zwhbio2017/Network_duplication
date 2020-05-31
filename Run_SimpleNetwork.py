import random
import numpy as np
import pandas as pd
import sys
import SimpleNetwork

parameter = sys.argv[1]
if len(sys.argv) == 2:
    network_extract = 100
else:
    network_extract = int(sys.argv[2])
random.seed(12)

for time in range(100):
    if (time + 1) % 10 == 0:
        print('Iteration ' + str(time + 1))
    if parameter == '2002':
        network = SimpleNetwork.SimpleNetwork(n_start=5, n_end=1000, beta=0.16, delta=0.58, k_mean=2.0)
    elif parameter == '2003':
        network = SimpleNetwork.SimpleNetwork(n_start=5, n_end=1000, beta=0.155, delta=0.562, k_mean=2.5)
    while True:
        if network.n >= network.n_end:
            connection_1000 = []
            for i in range(len(network.network)):
                connection_1000.append(sum(network.network['gene_' + str(i + 1)]))
            break
        if network.n == 100:
            connection_100 = []
            for i in range(100):
                connection_100.append(sum(network.network['gene_' + str(i + 1)]))
        if network.n == 500:
            connection_500 = []
            for i in range(500):
                connection_500.append(sum(network.network['gene_' + str(i + 1)]))

        network.gene_duplication()
        network.remove_linkage()
        network.create_linkage()

    if (time + 1) == network_extract:
        network_result = pd.DataFrame(network.network)
        if parameter == '2002':
            network_result.to_csv('File/SimpleNetwork_network_result_2002.txt', sep='\t', header=False, index=False)
        elif parameter == '2003':
            network_result.to_csv('File/SimpleNetwork_network_result_2003.txt', sep='\t', header=False, index=False)

    connection_num_100 = np.arange(0, 100, 1)
    connection_num_500 = np.arange(0, 500, 1)
    connection_num_1000 = np.arange(0, 1000, 1)
    gene_num_100 = np.zeros(100, dtype=int)
    gene_num_500 = np.zeros(500, dtype=int)
    gene_num_1000 = np.zeros(1000, dtype=int)

    for item in connection_100:
        gene_num_100[item] += 1

    for item in connection_500:
        gene_num_500[item] += 1

    for item in connection_1000:
        gene_num_1000[item] += 1

    connection_num_100.reshape(100)
    connection_num_500.reshape(500)
    connection_num_1000.reshape(1000)
    gene_num_100.reshape(100)
    gene_num_500.reshape(500)
    gene_num_1000.reshape(1000)

    if time == 0:
        result_100 = pd.DataFrame(None, columns=['connection_num', 'gene_num_1'])
        result_100['connection_num'] = connection_num_100
        result_100['gene_num_1'] = gene_num_100
        result_500 = pd.DataFrame(None, columns=['connection_num', 'gene_num_1'])
        result_500['connection_num'] = connection_num_500
        result_500['gene_num_1'] = gene_num_500
        result_1000 = pd.DataFrame(None, columns=['connection_num', 'gene_num_1'])
        result_1000['connection_num'] = connection_num_1000
        result_1000['gene_num_1'] = gene_num_1000
    else:
        result_100['gene_num_' + str(time + 1)] = gene_num_100
        result_500['gene_num_' + str(time + 1)] = gene_num_500
        result_1000['gene_num_' + str(time + 1)] = gene_num_1000

if parameter == '2002':
    result_100.to_csv('File/SimpleNetwork_connection_result_100_2002.txt', sep='\t', header=False, index=False)
    result_500.to_csv('File/SimpleNetwork_connection_result_500_2002.txt', sep='\t', header=False, index=False)
    result_1000.to_csv('File/SimpleNetwork_connection_result_1000_2002.txt', sep='\t', header=False, index=False)
elif parameter == '2003':
    result_100.to_csv('File/SimpleNetwork_connection_result_100_2003.txt', sep='\t', header=False, index=False)
    result_500.to_csv('File/SimpleNetwork_connection_result_500_2003.txt', sep='\t', header=False, index=False)
    result_1000.to_csv('File/SimpleNetwork_connection_result_1000_2003.txt', sep='\t', header=False, index=False)
