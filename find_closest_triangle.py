from graph_tool.all import *
import numpy as np
from get_neighbors import *
from bfs import *

# we want to find closest triangle from node inside a clique.
# therefore, this triangle can`t be inside the clique we are checking
def find_closest_triangle (g, vertex_dict, pivot, clique):
	for e in g.edges(): #edge u, v
		u = e.source()
		v = e.target()
		nodes = bfs (pivot, g, vertex_dict)
		for w in nodes:
			if g.edge(v, vertex_dict[w]) != None and g.edge(u, vertex_dict[w]) != None:
				t = []
				t.append(g.vp.labels[v])
				t.append(w)
				t.append(g.vp.labels[u])
				if (sublist(t, clique)):
					continue
				return t

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True
