import networkx as nx
from ogb.graphproppred import DglGraphPropPredDataset, collate_dgl
from torch.utils.data import DataLoader

#Subgraphing Section
def subgraph(startnode, khop):
    subgraph = nx.Graph()
    shortestpaths = nx.shortest_path_length(G, source=startnode, method='dijkstra')
    for j in list(shortestpaths.keys()):
        if shortestpaths[j] <= khop:
            subgraph.add_edge(startnode, shortestpaths[j], weight=1)
            #figure out how to get iterated node in the shortestpaths list
    return subgraph

G = nx.Graph()

dataset = DglGraphPropPredDataset(name = "ogbg-molhiv")

graph = dataset[0]

total_edges = int(graph.get("edge_index").size / 2)
print(total_edges)
"""
for i in range(0, total_edges):
  print(i)  
  node1 = graph.get("edge_index")[0][i]
  node2 = graph.get("edge_index")[1][i]
  G.add_edge(node1, node2, weight = 1)

totalnodes = graph.get("num_nodes")
khop = 5
"""
"""for i in range(0, totalnodes):
subg = subgraph(i, khop)"""
#startnode = int(totalnodes/2)
#subg = subgraph(startnode, khop)

#print(G.number_of_edges())
#print(G.number_of_nodes())
