import random

class RandomNetwork:
    def __init__(self, node_num, mean_connectivity):
        self.node_num = node_num
        self.mean_connectivity = mean_connectivity
        self.genes = ['gene_' + str(i + 1) for i in range(self.node_num)]
        self.network = {}

        for gene in self.genes:
            self.network[gene] = list(0 for i in range(self.node_num))

        for i in range(self.node_num):
            for j in range(i + 1):
                probability = random.random()
                if probability <= self.mean_connectivity / self.node_num:
                    self.network['gene_' + str(i + 1)][j] = 1
                    self.network['gene_' + str(j + 1)][i] = 1
