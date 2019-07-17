#env3

import networkx as nx
import dwave_networkx as dnx

#for hybrid
import dimod
import hybrid

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
# for showing the result as Graph
import matplotlib.pyplot as plt
import numpy as np

# random Graph
#small
G = nx.random_geometric_graph(20, 0.24, seed=0)
#big
#G = nx.random_geometric_graph(1000, 0.075, seed=0)	

# solve independent set
#Hybrid:
kerberos = hybrid.Kerberos()
qubo_rnd = dnx.algorithms.independent_set.maximum_weighted_independent_set_qubo(G)
bqm_rnd = dimod.BQM.from_qubo(qubo_rnd)
state = hybrid.State.from_problem(bqm_rnd)
result = kerberos.run(state).result()

# print solutiom
selected_nodes = np.flatnonzero(result.samples.record.sample[0] == 1)
subgraph = G.subgraph(selected_nodes)

selected_nodes_2 = np.flatnonzero(result.samples.record.sample[0] == 0)
othersubgraph = G.subgraph(selected_nodes_2)

pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(subgraph,pos=pos)
nx.draw(othersubgraph,pos=pos, node_color='b')
plt.show()