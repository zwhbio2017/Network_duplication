import random
import numpy as np
import pandas as pd
import RandomNetwork


random.seed(12)
cc = []

for time in range(100):
    if (time + 1) % 10 == 0:
        print('Iteration ' + str(time + 1))
    network = RandomNetwork.RandomNetwork(1000, 2.0)

    network_result = pd.DataFrame(network.network)
    network_result.to_csv('File/RandomNetwork_network_result.txt', sep='\t', header=False, index=False)

    connection_1000 = []
    for i in range(len(network.network)):
        connection_1000.append(sum(network.network['gene_' + str(i + 1)]))

    connection_num_1000 = np.arange(0, 1000, 1)
    gene_num_1000 = np.zeros(1000, dtype=int)

    for item in connection_1000:
        gene_num_1000[item] += 1

    connection_num_1000.reshape(1000)
    gene_num_1000.reshape(1000)

    if time == 0:
        result_1000 = pd.DataFrame(None, columns=['connection_num', 'gene_num_1'])
        result_1000['connection_num'] = connection_num_1000
        result_1000['gene_num_1'] = gene_num_1000
    else:
        result_1000['gene_num_' + str(time + 1)] = gene_num_1000

result_1000.to_csv('File/RandomNetwork_connection_result_1000.txt', sep='\t', header=False, index=False)
