import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import sys

node_number = int(sys.argv[1])
network_type = sys.argv[2]
if network_type == 'SimpleNetwork':
    network_parameter = sys.argv[3]

if network_type == 'SimpleNetwork':
    network = pd.read_table('File/' + network_type + '_network_result_' + network_parameter + '.txt', header=None)
else:
    network = pd.read_table('File/' + network_type + '_network_result.txt', header=None)

network.columns = ['gene_' + str(i + 1) for i in range(1000)]
network.index = ['gene_' + str(i + 1) for i in range(1000)]

G = nx.Graph()

for i in range(node_number):
    for j in range(i + 1):
        if network.iat[i, j] == 1:
            G.add_edge('gene_' + str(i + 1), 'gene_' + str(j + 1))

nx.draw(G, with_labels=False, edge_color='black', node_color='black', node_size=20)
plt.show()
