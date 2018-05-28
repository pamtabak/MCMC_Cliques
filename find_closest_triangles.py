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

	#min distance between pivot and any triangle
	dist 	 = -1
	bfs_dist = {} #key is node and value is distance from pivot
	bfs_dist[pivot] = 0

	while (len(queue) != 0):
		w = queue.pop(0) #BFS
		if (dist != -1 and bfs_dist[w] > dist):
			#it means we have already find triangles at min distance and there are no more
			#nodes at that min distance to be checked
			break
		neighbors = get_neighbors(w, g, vertex_dict)
		for u in range(0, len(neighbors)):
			n1 = neighbors[u]
			if (n1 not in marked_dict):
				marked_dict[n1] = True
				queue.append(n1)
				bfs_dist[n1] = bfs_dist[w] + 1
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
					if (dist == -1):
						# it means we found the first triangle
						dist = bfs_dist[w]
					if (t not in triangles):
						triangles.append(t)
	return triangles

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True
