from graph_tool.all import *
from read_graph import *

for i in range(5):
    g, vertex_dict = read_graph("Draw/clique_{}.txt".format(i), False)
    graph_draw(g,
    bg_color=[1.,1.,1.,1.],
    vertex_text=g.vp.labels,
    vertex_size=70,
    vertex_font_size=24,
    vertex_fill_color=[1.,1.,1.,1.],
    vertex_pen_width=2.0,
    vertex_color=[0.,0.,0.,1.],
    edge_pen_width=1.0,
    edge_marker_size=1,
    output_size=(200, 200),
    output="Draw/clique_{}.png".format(i))
