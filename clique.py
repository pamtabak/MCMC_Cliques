from graph_tool.all import *
import numpy as np

def BronKerbosch2(R, P, X, g, v_prop, vertex_dict):
	if (len(P) == 0 and len(X) == 0):
		print(R)
		return R
	choose_node_from_array = np.union1d(P, X)
	index = np.random.randint(len(choose_node_from_array))
	pivot = choose_node_from_array[index]
	for v in P:
		pivot_neighbors = get_neighbors(pivot, g, v_prop, vertex_dict)
		if v not in pivot_neighbors:
			neighbors = get_neighbors(v, g, v_prop, vertex_dict)
			BronKerbosch2(np.union1d(R, v), np.intersect1d(P, neighbors), np.intersect1d(X, neighbors), g, v_prop, vertex_dict)
			P = np.delete(P, np.where(P == v))
			X = np.append(X, v)

def get_neighbors(v, g, v_prop, vertex_dict):
	neighbors = []
	for n in g.vertex(vertex_dict[v]).out_neighbors():
		neighbors.append(v_prop[n])
	return neighbors

# Wikipedia algorithm
# BronKerbosch2(R,P,X):
#        if P and X are both empty:
#            report R as a maximal clique
#        choose a pivot vertex u in P ⋃ X
#        for each vertex v in P \ N(u):
#            BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
#            P := P \ {v}
#            X := X ⋃ {v}