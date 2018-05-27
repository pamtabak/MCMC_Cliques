from graph_tool.all import *
import numpy as np
from get_neighbors import *

def find_triangle (g, vertex_dict):
	triangles = []
	for e in g.edges(): #edge u, v
		u = e.source()
		v = e.target()
		for w in g.vertices():
			if g.edge(v, w) != None and g.edge(u, w) != None:
				t = []
				t.append(g.vp.labels[v])
				t.append(g.vp.labels[w])
				t.append(g.vp.labels[u])
				t.sort()
				if (t not in triangles):
					triangles.append(t)
	return triangles
