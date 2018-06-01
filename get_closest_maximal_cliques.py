from graph_tool.all import *
import numpy as np
from functools import reduce
from get_neighbors import *
from find_closest_triangles import *
import copy

def get_closest_maximal_cliques (g, vertex_dict, pivot, clique):
	closest_triangles = find_closest_triangles (g, vertex_dict, pivot, clique)
	maximal_cliques   = []
	
	#then we only need to calculate distance between nodes once
	min_dist = {}

	for closest_triangle in closest_triangles:
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
		triangle = closest_triangle[0]

		#we get the neighbors from each node inside clique and see how many match
		neighbors = []
		for n in triangle:
			neighbors.append(get_neighbors(n, g, vertex_dict))
		nodes_in_common = reduce(np.intersect1d,neighbors)
		for n in triangle:
			nodes_in_common = np.delete(nodes_in_common, np.where(nodes_in_common == str(n)))

		if (len(nodes_in_common) == 0):
			triangle.sort()
			if (triangle not in maximal_cliques):
				maximal_cliques.append(triangle)
			continue

		cliques = []
		# preciso gerar todos os possiveis subconjuntos com nodes_in_common
		# ver se e valido (todos sao arestas)
		# ver se e maximal (no final)

		binary_subset  = []
		one_binary     = ""
		for i in range(len(nodes_in_common)):
			binary_subset.append(0)
			if (i == len(nodes_in_common) - 1):
				one_binary += "1"
			else:	
				one_binary += "0"

		binary_subset[0] = 0

		while (not (all(item == '1' for item in binary_subset))):
			binary = ''.join(map(str, binary_subset))

			binary = bin_add(binary, one_binary)
			for b in range(len(binary_subset)):
				if (b >= len(binary)):
					binary_subset[b] = 0
				else:
					binary_subset[b] = binary[b]

			#check if valid clique. each element with 1 needs to be adjacent
			nodes_to_check = []
			for i in range(0, len(binary_subset)):
				if (binary_subset[i] == '1'):
					nodes_to_check.append(nodes_in_common[i])
			valid_clique = True
			for u in range(0, len(nodes_to_check)):
				if (not valid_clique):
					break
				for v in range(u+1, len(nodes_to_check)):
					if (g.edge(vertex_dict[nodes_in_common[u]], vertex_dict[nodes_in_common[v]]) == None):
						valid_clique = False
						break
			if (valid_clique):
				clique = copy.copy(triangle)
				for n in nodes_to_check:
					clique.append(n)
				clique.sort()
				if (clique not in cliques):
					cliques.append(clique)

		for c1 in range(0, len(cliques)):
			for c2 in range(0, len(cliques)):
			#we need to see if clique is maximal or not
				if (sublist(cliques[c1], cliques[c2])):
					continue
				if (clique not in maximal_cliques):
					maximal_cliques.append(clique)

	return maximal_cliques

def bin_add(*args): 
	return bin(sum(int(x, 2) for x in args))[2:]

def sublist(list1, list2):
	for element in list1:
		if (element not in list2):
			return False
	return True