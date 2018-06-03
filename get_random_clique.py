from graph_tool.all import *
import numpy as np
from get_closest_maximal_cliques import *

def get_random_clique(g, vertex_dict):
    while (True):
        v = g.vp.labels[np.random.choice(list(g.vertices()))]
        cliques = get_closest_maximal_cliques(g, vertex_dict, [v])
        if (len(cliques) == 0):
             continue
        i = np.random.choice(len(cliques))
        return cliques[i]
