from graph_tool.all import *

def get_neighbors(v, g, vertex_dict):
	neighbors = []
	for n in g.vertex(vertex_dict[v]).out_neighbors():
		neighbors.append(g.vp.labels[n])
	return neighbors
