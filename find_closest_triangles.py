from graph_tool.all import *
import numpy as np
from get_neighbors import *

# we want to find closest triangle from node inside a clique.
# therefore, this triangle can`t be inside the clique we are checking
def find_closest_triangles (g, vertex_dict, pivot, clique):
	marked_dict = {}
	queue = []
	queue.append(pivot)
	marked_dict[pivot] = True
	triangles = []

	while (len(queue) != 0 and len(triangles) == 0):
		w = queue.pop(0) #BFS
		for e in g.edges(): #edge u, v
			u = e.source()
			v = e.target()
			if g.edge(v, vertex_dict[w]) != None and g.edge(u, vertex_dict[w]) != None:
				t = []
				t.append(g.vp.labels[v])
				t.append(w)
				t.append(g.vp.labels[u])
				t.sort()
				if (sublist(t, clique)):
					continue
				if (t not in triangles):
					triangles.append(t)
		neighbors = get_neighbors(w, g, vertex_dict)
		for n in neighbors:
			if (n not in marked_dict):
				marked_dict[n] = True
				queue.append(n)
	return triangles

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True
