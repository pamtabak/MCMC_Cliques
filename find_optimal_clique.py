from graph_tool.all import *
import numpy as np
from get_neighboring_cliques import *
import ast

def update_chain (chain_adjacency_dict, current_state, explored_cliques, g, vertex_dict):
    neighboring_cliques = []
    if (str(current_state) not in explored_cliques):
        if (str(current_state) not in chain_adjacency_dict):
            chain_adjacency_dict[str(current_state)] = []
        neighboring_cliques = get_closest_maximal_cliques(g, vertex_dict, current_state)
        for neighboring_clique in neighboring_cliques:
            if (neighboring_clique not in chain_adjacency_dict[str(current_state)]):
                chain_adjacency_dict[str(current_state)].append(neighboring_clique)   
            if (str(neighboring_clique) not in explored_cliques):
                if (str(neighboring_clique) not in chain_adjacency_dict):
                    chain_adjacency_dict[str(neighboring_clique)] = []
                if (str(current_state) not in chain_adjacency_dict[str(neighboring_clique)]):
                    chain_adjacency_dict[str(neighboring_clique)].append(current_state)

def find_optimal_clique(g, vertex_dict, initial_clique, L, T_0, annealing_func, annealing_params_dict):
    optimal_clique = initial_clique # what we're looking for
    chain_adjacency_dict = {} # stores, for each clique, its list of neighbors in the markov chain.
                              # dictionary keys are string representations of the lists that represents the cliques,
                              # because lists cannot be hashed
    explored_cliques = {}

    state = initial_clique
    for t in range(L):
        print('Iteration: {}'.format(t))
        print('State: {}'.format(state))
        print('Optimal clique: {}'.format(optimal_clique))
        print('Optimal clique size: {}'.format(len(optimal_clique)))

        # update annealing value for this iteration
        T = annealing_func(T_0, t, annealing_params_dict)
        print('T: {}'.format(T))

        # find states (cliques) that are neighbors of current state in the markov chain
        update_chain(chain_adjacency_dict, state, explored_cliques, g, vertex_dict)
        explored_cliques[str(state)] = True
        neighboring_cliques = chain_adjacency_dict[str(state)]

        transitions = []
        transition_probabilities = []
        for neighboring_clique in neighboring_cliques:
            if str(neighboring_clique) not in explored_cliques: # ignore cliques that have already been seen
                # check if newly found clique is bigger than our current optimal clique
                if len(neighboring_clique) > len(optimal_clique):
                    optimal_clique = neighboring_clique
                # find neighbors of this clique, so that we know its out degree
                update_chain(chain_adjacency_dict, neighboring_clique, explored_cliques, g, vertex_dict)
                explored_cliques[str(neighboring_clique)] = True
                neighboring_cliques_2 = chain_adjacency_dict[str(neighboring_clique)]

            # build list of transitions and list of respective probabilities (using simulated annealing)
            transitions.append(str(neighboring_clique))
            accept_prob = get_accept_probability(state, neighboring_clique, chain_adjacency_dict, T)
            transition_probabilities.append( accept_prob / (len(chain_adjacency_dict[str(state)]) + 1) )

        # calculate self-loop probability
        self_prob = 1 - np.sum(transition_probabilities)

        # update transitions and probabilities adding self loop
        transitions = transitions + [str(state)]
        transition_probabilities.append(self_prob)
        #print(transition_probabilities)

        # choose neighbor to transition to according to calculated probabilities
        # ast.literal_eval transforms the string representation of a list into the original list
        state = ast.literal_eval(np.random.choice(transitions, p=transition_probabilities))

        print()

def get_accept_probability(state, neighbor, chain_adjacency_dict, T):
    # boltzman distribution
    exp = np.power(np.e, (len(neighbor) - len(state)) / float(T))

    # metropolis-hasting
    prod = exp * (len(chain_adjacency_dict[str(state)]) + 1) / (len(chain_adjacency_dict[str(neighbor)]) + 1)
    return np.min([1, prod])
