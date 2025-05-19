# Import packages
from PIG import value_iteration, pig_value_func, generate_PIG_states
import pickle
import time


# Problem parameters
target=100                            # target score
die_size=6                            # die size
S = generate_PIG_states(target)       # state space
A = {"roll", "hold"}                  # set of actions
bellman_PIG = pig_value_func(target=target, die_size=die_size)    # value update equation
V_init = dict([(s, 0) for s in S])    # initial probability of winning at all states is 0
V_init[("Win", "Lose", 0)] = 1        # probability of winning at win state is 1

# Apply value iteration
start_time = time.perf_counter() # start time to calculate total run time
results = value_iteration(S=S, A=A, P=None, R=None,
                          gamma=1, max_iterations=100,
                          bellman_eq=bellman_PIG, V_init=V_init)
PIG_solve_time = time.perf_counter() - start_time    # total run time
print(f"PIG_direct time taken: {PIG_solve_time:.2f}")

PIG_optimal_policy = results["optimal_policy"]
PIG_optimal_prob_winning = results["value_function"]


# Store PIG results
# # Uncomment if new results need to be stored
# pickle.dump(results, open(fr'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'wb'))

# Load PIG results
results_loaded = pickle.load(open(fr'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'rb'))


