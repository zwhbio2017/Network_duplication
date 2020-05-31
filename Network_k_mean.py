import pandas as pd
import sys

node_number = int(sys.argv[1])
network_type = sys.argv[2]
if network_type == 'SimpleNetwork':
    network_parameter = sys.argv[3]

if network_type == 'SimpleNetwork':
    result = pd.read_table('File/' + network_type + '_connection_result_' + str(node_number) + '_' + network_parameter + '.txt', header=None)
else:
    result = pd.read_table('File/' + network_type + '_connection_result_' + str(node_number) + '.txt', header=None)
result.columns = ['connection_num'] + ['gene_num_' + str(i + 1) for i in range(100)]
k_total = []

for i in range(100):
    k_total.append(sum(result['connection_num'] * result['gene_num_' + str(i + 1)]) / node_number)

print('mean of K: ' + str(sum(k_total) / 100))
