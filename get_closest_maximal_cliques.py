from graph_tool.all import *
import numpy as np
from functools import reduce
from get_neighbors import *
from find_closest_triangles import *
import copy
from bronkerbosch2 import *
import ast

def get_closest_maximal_cliques (g, vertex_dict, init_clique):
	min_dist  = len(vertex_dict)
	triangles = {}
	for pivot in init_clique:
		pivot_closest_triangles = find_closest_triangles (g, vertex_dict, pivot, init_clique)
		if (pivot_closest_triangles[1] > min_dist):
			continue
		min_dist 		 = pivot_closest_triangles[1]
		triangles[pivot] = pivot_closest_triangles

	closest_triangles = []
	maximal_cliques   = []

	for t_info in triangles:
		if (triangles[t_info][1] == min_dist):
			for t in triangles[t_info][0]:
				if (t not in closest_triangles):
					closest_triangles.append(t)

					#now we need to get maximal cliques with this triangle
					triangle = copy.copy(t)

					#we get the neighbors from each node inside clique and see how many match
					neighbors = []
					for n in triangle:
						neighbors.append(get_neighbors(n, g, vertex_dict))
					nodes_in_common = reduce(np.intersect1d,neighbors)
					for n in triangle:
						nodes_in_common = np.delete(nodes_in_common, np.where(nodes_in_common == str(n)))

					if (len(nodes_in_common) == 0):
						triangle.sort()
						if (triangle not in maximal_cliques and not (sublist(triangle, init_clique))):
							maximal_cliques.append(triangle)
						continue

					cliques = []
					bron_kerbosch2([], nodes_in_common, [], g, vertex_dict, cliques)

					for c1 in range(0, len(cliques)):
						for c2 in range(0, len(cliques)):
							if (c1 == c2):
								continue
							#we need to see if clique is maximal or not
							clique_1 = list(ast.literal_eval(cliques[c1]))
							clique_2 = list(ast.literal_eval(cliques[c2]))
							if (sublist(clique_1, clique_2)):
								continue
							for n in t:
								clique_1.append(n)
							clique_1.sort()
							if (clique_1 not in maximal_cliques):
								maximal_cliques.append(clique_1)
	return maximal_cliques

def bin_add(*args):
	return bin(sum(int(x, 2) for x in args))[2:]

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True
