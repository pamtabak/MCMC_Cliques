from graph_tool.all import *
import numpy as np
from get_neighbors import *

def find_triangle (g, v_prop, vertex_dict):
	triangles = []
	for e in g.edges(): #edge u, v
		u = e.source()
		v = e.target()
		for w in g.vertices():
			if g.edge(v, w) != None and g.edge(u, w) != None:
				t = []
				t.append(v_prop[v])
				t.append(v_prop[w])
				t.append(v_prop[u])
				t.sort()
				if (t not in triangles):
					triangles.append(t)
	return triangles