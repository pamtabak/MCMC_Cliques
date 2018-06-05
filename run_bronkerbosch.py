import argparse
import sys
import json
import numpy as np
from graph_tool.all import *
from read_graph import *
from bronkerbosch2 import *
import time

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

data = {}
data['file'] = args.file

start_time = time.time()

g, vertex_dict = read_graph(args.file, False)
print("finished reading graph")

nodes = [v for v in g.vp.labels]

elapsed_time = time.time() - start_time
print("bronkerbosch2")
bron_kerbosch2([], nodes, [], g, vertex_dict, [])
data['elapsed_time'] = elapsed_time

with open('Results/results_bronkerbosch_{}.json'.format(args.file.replace("Datasets/", "")), 'w') as f:
	f.write(json.dumps(data, indent=4, sort_keys=True))
