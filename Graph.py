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
import networkx as nx
import dwave_networkx as dnx
# for showing the result as Graph
import matplotlib.pyplot as plt

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

my_sampler = EmbeddingComposite(DWaveSampler())

# empty Graph
G = nx.Graph()
# fill the Graph -> to adapt 
# for independent set or Max Cut
G.add_edges_from([(1,4),(2,4),(2,5),(2,7),(2,9),(2,11),(3,5),(3,9),(3,11),(4,8),(5,10),(6,12),(7,8),(7,11),(7,12)])

# solve independent set
S = dnx.maximum_independent_set(G, sampler=my_sampler,num_reads=10)
# solve Max Cut
#S = dnx.algorithms.max_cut.maximum_cut(G,sampler=my_sampler,num_reads=10)

# Travelling Salesman needs weights in graph
# Social needs signs in graph

# print solutiom
print('Max intependent Nodes: ', len(S))
#print('Max Cut Nodes: ', len(S))
print(S)

# show solution as Graph
# for independent set or Max Cut
k = G.subgraph(S)
notS = list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(k,pos=pos)
nx.draw(othersubgraph,pos=pos, node_color='r')
plt.show()
