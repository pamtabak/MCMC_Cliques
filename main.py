from graph_tool.all import *
from generate_graph import *
#from bronkerbosch2 import *
#from bfs import *
#from find_triangle import *
#from find_closest_triangles import *
#from get_closest_maximal_cliques import *
from get_neighboring_cliques import *

# graph_data = read_graph("Datasets/teste.txt", False)
g, vertex_dict = read_graph("Datasets/teste.txt", False)

nodes = []
for v in g.vp.labels:
	nodes.append(v)

# print(get_closest_maximal_cliques (g, vertex_dict, nodes[0], ['0', '1', '2']))
#print()
#print(get_closest_maximal_cliques (g, vertex_dict, nodes[0], ['1','3','9']))
#print()
#print(find_closest_triangle (g, vertex_dict, nodes[0], ['0','1','2']))
#print()
#print(find_triangle(g, vertex_dict))
#print()
print(get_neighboring_cliques(g, vertex_dict, ['0','1','2']))

# BronKerbosch2([], nodes, [], g, vertex_dict)
