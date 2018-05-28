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
	triangles = [] #tuple containing: triangle, dist - min_dist, dist, node
	aux_triangles = [] #list containing triangles only, to verify duplicates

	#min distance between pivot and any triangle
	dist 	 = -1
	bfs_dist = {} #key is node and value is distance from pivot
	bfs_dist[pivot] = 0

	while (len(queue) != 0):
		w = queue.pop(0) #BFS
		if (dist != -1 and bfs_dist[w] > (dist + 1)):
			#It means we have already find triangles at min distance and there are no more
			#nodes at that min distance to be checked
			#We want to return also triangles at dist + 1, because then we can look for triangles from only
			#one node from the clique (since all nodes at a clique are dist 1). But we will need to check if
			#triangles is dist from at least one of the nodes from the clique
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
					if (t not in aux_triangles):
						if (dist == -1):
						# it means we found the first triangle
							dist = bfs_dist[w]
						aux_triangles.append(t)
						triangles.append((t, bfs_dist[w] - dist, dist, w))
	return triangles

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True
