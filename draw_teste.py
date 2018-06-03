from graph_tool.all import *
from read_graph import *

g, vertex_dict = read_graph("Datasets/teste.txt", False)

graph_draw(g,
bg_color=[1.,1.,1.,1.],
vertex_text=g.vp.labels,
vertex_size=30,
vertex_fill_color=[1.,1.,1.,1.],
vertex_pen_width=3.0,
vertex_color=[0.,0.,0.,1.],
edge_pen_width=1.0,
edge_marker_size=1,
output_size=(600, 600),
output="Draw/teste_graph.png")
