from graph_tool.all import *

def find_clique (g, current_node):
	# we run a BFS starting at the current_node searching for 
	# cliques with 3 or more nodes
	dist   = 0
	neighbors = current_node.out_neighbors()