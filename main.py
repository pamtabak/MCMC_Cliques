from graph_tool.all import *
from generate_graph import *
from bronkerbosch2 import *

graph_data = read_graph("Datasets/KarateClub.txt", False)
# graph_data = read_graph("Datasets/teste.txt", False)
g 	   = graph_data[0]
v_prop = graph_data[1]
vertex_dict = graph_data[2]

nodes = []
for v in v_prop:
	nodes.append(v)
# print(nodes)

BronKerbosch2([], nodes, [], g, v_prop, vertex_dict)
#find_clique(g, g.vertex(0))
#graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(500, 500))
