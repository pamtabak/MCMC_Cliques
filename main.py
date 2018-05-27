from graph_tool.all import *
from generate_graph import *
from bronkerbosch2 import *
from bfs import *
from find_triangle import *
from find_closest_triangle import *
from get_closest_maximal_clique import *

# graph_data = read_graph("Datasets/teste.txt", False)
graph_data  = read_graph("Datasets/KarateClub.txt", False)
g 	        = graph_data[0]
vertex_dict = graph_data[1]

nodes = []
for v in g.vp.labels:
	nodes.append(v)

# print(get_closest_maximal_clique (g, vertex_dict, nodes[0], ['0', '1', '2']))
#print()
print(get_closest_maximal_clique (g, vertex_dict, nodes[0], ['1','3','9']))
#print()
#print(find_closest_triangle (g, vertex_dict, nodes[0], ['0','1','2']))
#print()
#print(find_triangle(g, vertex_dict))
#print()

# BronKerbosch2([], nodes, [], g, vertex_dict)
