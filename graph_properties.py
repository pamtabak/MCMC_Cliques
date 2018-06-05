import argparse
import sys
import json
import numpy as np
from graph_tool.all import *
from read_graph import *
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

data = {}
data['file'] = args.file

g, vertex_dict = read_graph(args.file, False)
print("finished reading graph")

data['density'] = 2 * g.num_edges() / (g.num_vertices() * (g.num_vertices() - 1))

nodes = [v for v in g.vp.labels]

data['global_clustering'] = global_clustering(g)
data['average_degree'] = vertex_average(g, "out")
data['diameter'] = pseudo_diameter(g)[0]

degree_hist = vertex_hist(g, "out")
plt.title(args.file.replace("Datasets/", ""))
plt.xlabel('Grau')
plt.ylabel('Contagem')
plt.bar(degree_hist[1][:len(degree_hist[1]) - 1], degree_hist[0])
plt.savefig('Results/degree_hist_{}.png'.format(args.file.replace("Datasets/", "")))

with open('Results/results_properties_{}.json'.format(args.file.replace("Datasets/", "")), 'w') as f:
	f.write(json.dumps(data, indent=4, sort_keys=True))
