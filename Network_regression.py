import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sys

node_number = int(sys.argv[1])
network_type = sys.argv[2]
if network_type == 'SimpleNetwork':
    network_parameter = sys.argv[3]

if network_type == 'SimpleNetwork':
    result = pd.read_table('File/' + network_type + '_connection_result_' + str(node_number) + '_' + network_parameter + '.txt', header=None)
else:
    result = pd.read_table('File/' + network_type + '_connection_result_' + str(node_number) + '.txt', header=None)

result.columns = ['connection'] + ['num_' + str(i + 1) for i in range(100)]

data_1 = result[['connection', 'num_5']]
data_1['logk'] = np.log(data_1['connection'])
data_1['logPk'] = np.log(data_1['num_5'] / 1000)
data_1 = data_1[(data_1['logk'] != -np.inf) & (data_1['logPk'] != -np.inf)]

y = np.array(data_1['logPk']).reshape(-1, 1)
x = np.array(data_1['logk']).reshape(-1, 1)

model = LinearRegression()
model.fit(X=x, y=y)
predicts = model.predict(x)
R2 = model.score(X=x, y=y)
print('R2 = ' + str(R2))

plt.scatter(x, y)
plt.plot(x, predicts, color='black')

plt.xlabel('log10(k)')
plt.ylabel('log10(P(k))')
ax = plt.gca()
ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')

plt.show()
