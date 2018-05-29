from graph_tool.all import *
import numpy as np
from functools import reduce
from get_neighbors import *
from find_closest_triangles import *

def get_closest_maximal_cliques (g, vertex_dict, pivot, clique):
	closest_triangles = find_closest_triangles (g, vertex_dict, pivot, clique)
	maximal_cliques = []
	
	#then we only need to calculate distance between nodes once
	min_dist = {}

	for closest_triangle in closest_triangles:

		if (is_triangle_inside_maximal_clique (closest_triangle[0], maximal_cliques)):
			continue

		#first we check if triangle`s "head" (4th item from tuple) is at distance d from any node of the clique
		#if param is 0, then we don`t need to check. if 1, then we do need to check
		#we already know that it`s not distance d from pivot
		correct_triangle_distance = False
		if (closest_triangle[1] == 0):
			correct_triangle_distance = True
		if (closest_triangle[1] == 1):
			for node in clique:
				if (correct_triangle_distance):
					break
				if (node == pivot):
					continue
				#get distance between triangle`s "head" and node
				node_name_concat = (str(node) + "_" + str(closest_triangle[3]))
				if (node_name_concat not in min_dist):
					min_dist[node_name_concat] = shortest_distance(g, source=g.vertex(vertex_dict[node]), target=g.vertex(vertex_dict[closest_triangle[3]]))
				if (min_dist[node_name_concat] == closest_triangle[2]):
					correct_triangle_distance = True
					break
		if (not correct_triangle_distance):
			continue

		#now we need to get maximal clique with this triangle
		maximal_clique = closest_triangle[0]

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

def is_triangle_inside_maximal_clique (triangle, maximal_cliques):
	for clique in maximal_cliques:
		if (triangle[0] == clique[0] and triangle[1] == clique[1] and triangle[2] == clique[2]):
			return True
	return False