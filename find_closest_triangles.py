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
		neighbors = get_neighbors(w, g, vertex_dict)
		for u in range(0, len(neighbors)):
			n1 = neighbors[u]
			if (n1 not in marked_dict):
				marked_dict[n1] = True
				queue.append(n1)
			for v in range(u + 1, len(neighbors)):
				n2 = neighbors[v]
				if (g.edge(vertex_dict[n1], vertex_dict[n2]) != None):
					t = []
					t.append(g.vp.labels[vertex_dict[n2]])
					t.append(w)
					t.append(g.vp.labels[vertex_dict[n1]])
					t.sort()
					if (sublist(t, clique)):
						continue
					if (t not in triangles):
						triangles.append(t)
	return triangles

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True
