import argparse
import sys
import json
import numpy as np
from graph_tool.all import *
from read_graph import *
from bronkerbosch2 import *
from get_random_clique import *
from find_optimal_clique import *
import annealing_strategies as strats

def get_annealing_strat(strat_name):
	if strat_name == "exponential":
		return strats.exponential
	elif strat_name == "linear":
		return strats.linear
	elif strat_name == "logarithmic":
		return strats.logarithmic

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("walk_length", type=int)
parser.add_argument("initial_temperature", type=int)
parser.add_argument("--annealing_strat", choices=['exponential','linear','logarithmic'], default='exponential')
parser.add_argument("--annealing_params", type=dict, default={'beta':0.99})
args = parser.parse_args()

data = {}
data['file'] = args.file
data['walk_length'] = args.walk_length
data['initial_temperature'] = args.initial_temperature
data['annealing_strat'] = args.annealing_strat
data['annealing_params'] = args.annealing_params

g, vertex_dict = read_graph(args.file, False)
print("finished reading graph")

nodes = [v for v in g.vp.labels]

initial_clique = get_random_clique(g, vertex_dict)
print("already got initial clique, now we are searching for optimal")

optimal_clique = find_optimal_clique(g, vertex_dict, initial_clique, args.walk_length, args.initial_temperature, get_annealing_strat(args.annealing_strat), args.annealing_params)
print(optimal_clique)

data['optimal_clique'] = optimal_clique
data['optimal_clique_size'] = len(optimal_clique)

print("bronkerbosch2")
bronkerbosch_results = []
bron_kerbosch2([], nodes, [], g, vertex_dict, bronkerbosch_results)

data['bronkerbosch_optimal_clique'] = bronkerbosch_results[np.argmax(list(map(len, bronkerbosch_results)))]
data['bronkerbosch_optimal_clique_size'] = len(data['bronkerbosch_optimal_clique'])

with open('results_{}_{}_{}.json'.format(args.file.replace("Datasets/", ""), args.walk_length, args.initial_temperature), 'w') as f:
	f.write(json.dumps(data, indent=4, sort_keys=True))
