from graph_tool.all import *
from read_graph import *

g, vertex_dict = read_graph("Draw/markov.txt", True)

graph_draw(g,
bg_color=[1.,1.,1.,1.],
vertex_size=100,
vertex_fill_color=[1.,1.,1.,1.],
vertex_pen_width=5.0,
vertex_color=[0.4,0.7,0.9,1.],
edge_pen_width=1.0,
edge_marker_size=10,
output_size=(600, 600),
output="Draw/markov.png")
