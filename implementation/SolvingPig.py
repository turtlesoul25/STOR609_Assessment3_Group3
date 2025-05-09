from PIG import value_iteration, pig_value_func, piglet_value_func, generate_PIG_states, generate_PIGLET_states
import matplotlib.pyplot as plt
import numpy as np
import pickle


# Problem parameters
target=100                            # target score
die_size=6                            # die size
S = generate_PIG_states(target)       # state space
A = {"roll", "hold"}                  # set of actions
bellman_PIG = pig_value_func(target=target, die_size=die_size)    # value update equation
V_init = dict([(s, 0) for s in S])    # initial values
V_init[("Win", "Lose", 0)] = 1

# Uncomment if new results need to be stored
# Apply value iteration
results = value_iteration(S=S, A=A, P=None, R=None,
                          gamma=1, max_iterations=100,
                          bellman_eq=bellman_PIG, V_init=V_init)
PIG_optimal_policy = results["optimal_policy"]
PIG_optimal_prob_winning = results["value_function"]

print("Pig converged!")

# Store PIG results
# # Uncomment if new results need to be stored
# pickle.dump(results, open(f'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'wb'))

# Load PIG results
results_loaded = pickle.load(open(f'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'rb'))

