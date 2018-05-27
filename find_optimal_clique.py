from graph_tool.all import *
import numpy as np
from get_neighboring_cliques import *
import ast

def find_optimal_clique(g, vertex_dict, initial_clique, L, T_0, beta):
    optimal_clique = initial_clique # what we're looking for
    chain_adjacency_dict = {} # stores, for each clique, its list of neighbors in the markov chain.
                              # dictionary keys are string representations of the lists that represents the cliques,
                              # because lists cannot be hashed

    state = initial_clique
    for t in range(L):
        print('Iteration: {}'.format(t))
        print('State: {}'.format(state))
        print('Optimal clique: {}'.format(optimal_clique))

        # update annealing value for this iteration
        T = T_0 * np.power(beta, t)
        print('T: {}'.format(T))

        # find states (cliques) that are neighbors of current state in the markov chain
        neighboring_cliques = get_neighboring_cliques(g, vertex_dict, state)
        chain_adjacency_dict[str(state)] = neighboring_cliques

        transitions = []
        transition_probabilities = []
        for neighboring_clique in neighboring_cliques:
            if str(neighboring_clique) not in chain_adjacency_dict: # ignore cliques that have already been seen
                # check if newly found clique is bigger than our current optimal clique
                if len(neighboring_clique) > len(optimal_clique):
                    optimal_clique = neighboring_clique
                # find neighbors of this clique, so that we know its out degree
                neighboring_cliques_2 = get_neighboring_cliques(g, vertex_dict, neighboring_clique)
                chain_adjacency_dict[str(neighboring_clique)] = neighboring_cliques_2

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