import argparse
from graph_tool.all import *
from read_graph import *

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

g, vertex_dict = read_graph(args.file, False)

graph_draw(g,
bg_color=[1.,1.,1.,1.],
#vertex_text=g.vp.labels,
vertex_size=10,
vertex_fill_color=[1.,1.,1.,1.],
vertex_pen_width=2.0,
vertex_color=[0.,0.,0.,1.],
edge_pen_width=1.0,
edge_marker_size=1,
output_size=(600, 600),
output="Draw/{}.png".format(args.file.replace("Datasets/", "")))
