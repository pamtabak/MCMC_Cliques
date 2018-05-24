from graph_tool.all import *
from generate_graph import *
from clique import *

#graph_data = read_graph("Datasets/frb30-15-2.clq", False)
graph_data = read_graph("Datasets/teste.txt", False)
g = graph_data[0]
find_clique(g, g.vertex(0))
#graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(500, 500))