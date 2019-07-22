# Copyright 2018 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
