import matplotlib.pyplot as plt
import networkx as nx
from definition import G


if nx.is_forest(G) :
    print('ffforest')

def leaves(graph):
    return([n for n,d in graph.in_degree().items() if d==0])

while len(leaves(G)) > 0:
    for n in leaves(G):
        print(n)
        G.remove_node(n)


#
# for n,d in G.in_degree().items():
#     print(n)
#     print(d)


# print(nx.all_shortest_paths(G))

# print('ddd {here}'.format(here= G.number_of_nodes()))

# nx.draw(G)
# plt.show()
