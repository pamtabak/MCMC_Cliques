from graph_tool.all import *

def read_graph (filename, directed):
	vertex_dict = {}
	g           = Graph(directed=directed)
	g.vp.labels = g.new_vertex_property("string") # translates the node's id to it's label

	file_object = open(filename, "r")
	for line in file_object:
		if (line[0] == '#'):
			continue

		line = line.replace("e ", "")

		#before adding vertex, we need to check if it`s not already in the graph
		label1 = line.split()[0]
		label2 = line.split()[1]

		v1 = None
		v2 = None
		if (label1 in vertex_dict):
			v1 = g.vertex(vertex_dict[label1])
		else:
			v1 = g.add_vertex()
			g.vp.labels[v1] = label1
			vertex_dict[label1] = int(v1)

		if (label2 in vertex_dict):
			v2 = g.vertex(vertex_dict[label2])
		else:
			v2 = g.add_vertex()
			g.vp.labels[v2] = label2
			vertex_dict[label2] = int(v2)
		g.add_edge(v1, v2)
	return (g, vertex_dict)
