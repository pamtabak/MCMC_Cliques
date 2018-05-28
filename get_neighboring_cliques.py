from graph_tool.all import *
import numpy as np
from get_closest_maximal_cliques import *

def get_neighboring_cliques(g, vertex_dict, clique):
    neighboring_cliques = []
    # for v_label in clique:
    maximal_cliques = get_closest_maximal_cliques(g, vertex_dict, clique[0], clique)
    for maximal_clique in maximal_cliques:
        if maximal_clique not in neighboring_cliques:
            neighboring_cliques.append(maximal_clique)
    return neighboring_cliques
