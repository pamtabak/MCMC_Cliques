from graph_tool.all import *
from read_graph import *
from bronkerbosch2 import *
#from bfs import *
#from find_triangle import *
#from find_closest_triangles import *
#from get_closest_maximal_cliques import *
from get_neighboring_cliques import *
from get_random_clique import *
from find_optimal_clique import *
import annealing_strategies as strats

# g, vertex_dict = read_graph("Datasets/david.col", False)
g, vertex_dict = read_graph("Datasets/games120.txt", False)
print("finished reading graph")

nodes = []
for v in g.vp.labels:
	nodes.append(v)

# print(get_closest_maximal_cliques (g, vertex_dict, nodes[0], ['0', '1', '2']))
#print()
#print(get_closest_maximal_cliques (g, vertex_dict, nodes[0], ['1','3','9']))
#print()
#print(find_closest_triangle (g, vertex_dict, nodes[0], ['0','1','2']))
#print()
#print(find_triangle(g, vertex_dict))
#print()
#print(get_neighboring_cliques(g, vertex_dict, ['0','1','2']))
initial_clique = get_random_clique(g, vertex_dict)
print("already got initial clique, now we are searching for optimal")
find_optimal_clique(g, vertex_dict, initial_clique, 10, 100, strats.exponential, {'beta': 0.99})
print()

# print("bronkerbosch2")
# bron_kerbosch2([], nodes, [], g, vertex_dict)
