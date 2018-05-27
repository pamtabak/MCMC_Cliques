from graph_tool.all import *
import numpy as np
from get_neighbors import *

def bfs (pivot, g, v_prop, vertex_dict):
	marked_dict = {}
	queue = []
	queue.append(pivot)
	bfs = []
	marked_dict[pivot] = True

	while (len(queue) != 0):
		element = queue.pop(0)
		bfs.append(element)
		neighbors = get_neighbors(element, g, v_prop, vertex_dict)
		for n in neighbors:
			if (n not in marked_dict):
				marked_dict[n] = True
				queue.append(n)
	return bfs