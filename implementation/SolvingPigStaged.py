from PIG import value_iteration, pig_value_func, generate_PIG_states
import pickle
import time

# Problem parameters
target=100                            # target score
die_size=6                            # die size
S = generate_PIG_states(target)       # state space
A = {"roll", "hold"}                  # set of actions
bellman_pig = pig_value_func(target, die_size)      # value update equation
V_init = dict([(s, 0) for s in S])    # initial probability of winning at all states is 0
V_init[("Win", "Lose", 0)] = 1        # probability of winning at win state is 1

# Dictionary to store converged values at each staged
P_win = V_init.copy()

# Dictionary to store optimal policy at each stage
optimal_policy = dict([(s, 0) for s in S])
optimal_policy[("Win", "Lose", 0)], optimal_policy[("Lose", "Win", 0)] = "hold", "hold"   # always hold at terminal states


# Apply value iteration in stages
start_time = time.perf_counter() # start time to calculate total run time
for score_sum in range(2*(target-1), -1, -1): # For each score_sum 0 <= i+j <= 198
    # Subset of states for the score sum
    subset = {s for s in S if s[0] + s[1] == score_sum and s[2] < target-s[0]}
    
    # Perform value iteration on subset of states
    subset_results = value_iteration(S=subset, A=A, P=None, R=None, 
                          gamma=1, max_iterations=100, 
                          V_init=P_win, bellman_eq=bellman_pig)
    
    # Update policy and converged value for subset of states
    for s in subset:
        P_win[s] = subset_results["value_function"][s]
        optimal_policy[s] = subset_results["optimal_policy"][s]

PIG_staged_solve_time = time.perf_counter() - start_time # total run time
print("PIG_staged time taken: ", PIG_staged_solve_time)

results = {"optimal_policy": optimal_policy, "value_function": P_win} # results after value iteration


# Store PIG results
# # Uncomment if new results need to be stored
# pickle.dump(results, open(fr'implementation\Results\PIG_staged_results_target_{target}_diesize_{die_size}.pkl', 'wb'))


# Load PIG results
results_loaded = pickle.load(open(fr'implementation\Results\PIG_staged_results_target_{target}_diesize_{die_size}.pkl', 'rb'))
