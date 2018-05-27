from graph_tool.all import *
import numpy as np
from functools import reduce
from get_neighbors import *
from find_closest_triangle import *

def get_closest_maximal_clique (g, v_prop, vertex_dict, pivot, clique):
	closest_triangle = find_closest_triangle (g, v_prop, vertex_dict, pivot, clique)
	#now we need to get maximal clique with this triangle
	maximal_clique = closest_triangle
	# while (True):
		#we get the neighbors from each node inside clique and see how many match
	neighbors = []
	for n in maximal_clique:
		neighbors.append(get_neighbors(n, g, v_prop, vertex_dict))
	nodes_in_common = reduce(np.intersect1d,neighbors)
	for n in maximal_clique:
		nodes_in_common = np.delete(nodes_in_common, np.where(nodes_in_common == str(n)))
	
	if (len(nodes_in_common) == 0):
		return maximal_clique
	if (len(nodes_in_common) == 1):
		maximal_clique.append(nodes_in_common[0])
		return maximal_clique

	for u in range(0, len(nodes_in_common)):
		u_is_inside_clique = True
		for v in range(u + 1, len(nodes_in_common)):
			print(nodes_in_common[u])
			print(vertex_dict[nodes_in_common[u]])
			if (g.edge(vertex_dict[nodes_in_common[u]], vertex_dict[nodes_in_common[v]]) == None):
				u_is_inside_clique = False
		if (u_is_inside_clique):
			maximal_clique.append(v_prop[vertex_dict[nodes_in_common[u]]])
	if (len(maximal_clique) == 3):
		#it means that none of the nodes in common are adjacent
		#since we have nodes in common in the first place, maximal clique is 4
		#we simply add any of the nodes
		maximal_clique.append(v_prop[nodes_in_common[np.random.randint(len(nodes_in_common))]])
	return maximal_clique