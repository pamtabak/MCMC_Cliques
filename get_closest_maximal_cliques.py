from graph_tool.all import *
import numpy as np
from functools import reduce
from get_neighbors import *
from find_closest_triangles import *

def get_closest_maximal_cliques (g, vertex_dict, pivot, clique):
	closest_triangles = find_closest_triangles (g, vertex_dict, pivot, clique)
	maximal_cliques = []
	for closest_triangle in closest_triangles:
		#now we need to get maximal clique with this triangle
		maximal_clique = closest_triangle
		# while (True):
			#we get the neighbors from each node inside clique and see how many match
		neighbors = []
		for n in maximal_clique:
			neighbors.append(get_neighbors(n, g, vertex_dict))
		nodes_in_common = reduce(np.intersect1d,neighbors)
		for n in maximal_clique:
			nodes_in_common = np.delete(nodes_in_common, np.where(nodes_in_common == str(n)))

		if (len(nodes_in_common) == 0):
			maximal_clique.sort()
			if (maximal_clique not in maximal_cliques):
				maximal_cliques.append(maximal_clique)
			continue
		if (len(nodes_in_common) == 1):
			for n in nodes_in_common:
				maximal_clique.append(n)
				maximal_clique.sort()
				if (maximal_clique not in maximal_cliques):
					maximal_cliques.append(maximal_clique)
			continue

		for u in range(0, len(nodes_in_common)):
			u_is_inside_clique = True
			for v in range(u + 1, len(nodes_in_common)):
				if (g.edge(vertex_dict[nodes_in_common[u]], vertex_dict[nodes_in_common[v]]) == None):
					u_is_inside_clique = False
			if (u_is_inside_clique):
				maximal_clique.append(g.vp.labels[vertex_dict[nodes_in_common[u]]])
		if (len(maximal_clique) == 3):
			#it means that none of the nodes in common are adjacent
			#since we have nodes in common in the first place, maximal clique is 4
			#we simply add any of the nodes
			maximal_clique.append(g.vp.labels[nodes_in_common[np.random.randint(len(nodes_in_common))]])
		maximal_clique.sort()
		if (maximal_clique not in maximal_cliques):
			maximal_cliques.append(maximal_clique)
	return maximal_cliques
