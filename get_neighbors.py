from graph_tool.all import *

def get_neighbors(v, g, v_prop, vertex_dict):
	neighbors = []
	for n in g.vertex(vertex_dict[v]).out_neighbors():
		neighbors.append(v_prop[n])
	return neighbors
