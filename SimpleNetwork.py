import random

class SimpleNetwork:

    def __init__(self, n_start, n_end, beta, delta, k_mean):
        self.n_start = n_start
        self.n_end = n_end
        self.delta = delta
        if beta != None:
            self.beta = beta
            self.k_mean = k_mean
        else:
            self.k_mean = k_mean
            self.beta = (self.delta - 0.5) * self.k_mean

        self.n = self.n_start

        self.genes = ['gene_' + str(i + 1) for i in range(self.n_end)]
        self.network = {}
        for gene in self.genes:
            self.network[gene] = list(0 for i in range(self.n_end))

        num_connection = random.randint(1, self.n * (self.n - 1) / 2)
        node_start = self.genes[0:self.n_start]
        for i in range(num_connection):
            while True:
                pair = random.sample(node_start, 2)
                if self.network[pair[0]][int(pair[1].split('_', 1)[1]) - 1] == 0:
                    self.network[pair[0]][int(pair[1].split('_', 1)[1]) - 1] = 1
                    self.network[pair[1]][int(pair[0].split('_', 1)[1]) - 1] = 1
                    break

    def gene_duplication(self):
        current_genes = self.genes[0:self.n]
        mother_genes = random.choice(current_genes)

        self.n += 1
        self.network['gene_' + str(self.n)] = [i for i in self.network[mother_genes]]

        for i in range(self.n):
            if self.network['gene_' + str(self.n)][i] == 1:
                self.network['gene_' + str(i + 1)][self.n - 1] = 1

    def remove_linkage(self):
        if sum(self.network['gene_' + str(self.n)][0:self.n]) != 0:
            linkages = []
            for i in range(self.n):
                if self.network['gene_' + str(self.n)][i] == 1:
                    linkages.append(i)

            for linkage in linkages:
                probability = random.random()
                if probability <= self.delta:
                    self.network['gene_' + str(self.n)][linkage] = 0
                    self.network['gene_' + str(linkage + 1)][self.n - 1] = 0

    def create_linkage(self):
        if sum(self.network['gene_' + str(self.n)][0:self.n]) != self.n - 1:
            no_linkages = []
            for i in range(self.n):
                if self.network['gene_' + str(self.n)][i] == 0:
                    no_linkages.append(i)

            for no_linkage in no_linkages:
                probability = random.random()
                if probability <= self.beta / self.n:
                    self.network['gene_' + str(self.n)][no_linkage] = 1
                    self.network['gene_' + str(no_linkage + 1)][self.n - 1] = 1

    def network_check(self):
        for i in range(self.n):
            if sum(self.network['gene_' + str(i + 1)]) == 0:
                self.n -= 1

    def network_sum(self):
        result = 0
        for gene in self.genes:
            result += sum(self.network[gene])
        return result
