from graph_tool.all import *
import numpy as np
from get_neighbors import *

# Wikipedia algorithm
# BronKerbosch2(R,P,X):
#        if P and X are both empty:
#            report R as a maximal clique
#        choose a pivot vertex u in P ⋃ X
#        for each vertex v in P \ N(u):
#            BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
#            P := P \ {v}
#            X := X ⋃ {v}
def bron_kerbosch2(R, P, X, g, vertex_dict, results):
	if (len(P) == 0 and len(X) == 0):
		R.sort()
		if (str(list(R)) not in results):
			results.append(str(list(R)))
		return R
	p_union_x 		= np.union1d(P, X)
	pivot 	  		= p_union_x[np.random.randint(len(p_union_x))]
	pivot_neighbors = get_neighbors(pivot, g, vertex_dict)
	for v in P:
		if v not in pivot_neighbors:
			neighbors = get_neighbors(v, g, vertex_dict)
			bron_kerbosch2(np.union1d(R, v), np.intersect1d(P, neighbors), np.intersect1d(X, neighbors), g, vertex_dict, results)
			P = np.delete(P, np.where(P == v))
			X = np.append(X, v)
