# import packages
from PIG import value_iteration, piglet_value_func, generate_PIGLET_states
import matplotlib.pyplot as plt
import numpy as np
import pickle

# Initialise problem data
target = 2                           # target score
S = generate_PIGLET_states(target)   # set of states
A = {"flip", "hold"}                 # set of actions
bellman_piglet = piglet_value_func(target)     # value update equation
V_init = dict([(s, 0) for s in S])   # initialise probability of winning for all states to 0
V_init[("Win", "Lose", 0)] = 1       # initialise probability of winning at win state to 1

# Apply value iteration
results = value_iteration(S=S, A=A, P=None, R=None, 
                          gamma=1, max_iterations=100, 
                          V_init=V_init, bellman_eq=bellman_piglet)

# # Uncomment only if new results needed
# # Store results
# pickle.dump(results, open(fr'implementation\Results\PIGLET_results_target_{target}.pkl', 'wb'))

# Load results
results_loaded = pickle.load(open(fr'implementation\Results\PIGLET_results_target_{target}.pkl', 'rb'))

piglet_optimal_policy = results_loaded["optimal_policy"]
piglet_optimal_prob_winning = results_loaded["value_function"]
for s in S:
    print(f"P(winning at {s}) if {piglet_optimal_policy[s]}: {piglet_optimal_prob_winning[s]:.4f}")


# Produce convergence plot for PIGLET
piglet_prob_winning = dict((s, []) for s in S) # dictionary to store P(s) at each iteration for each state s
for its in range(25): # 25 iterations to replicate Figure 2 in Neller and Presser (2004)
    value_function = value_iteration(S=S, A=A, P=None, R=None, 
                          gamma=1, max_iterations=its, 
                          V_init=V_init, bellman_eq=bellman_piglet)["value_function"]
    for key, value in piglet_prob_winning.items():
        piglet_prob_winning[key].append(value_function[key]) # P(s) at iteration its for each s

# Plot
fig, ax = plt.subplots()
for state, probs in piglet_prob_winning.items():
    if state not in [("Win", "Lose", 0), ("Lose", "Win", 0)]: # plot only non-terminal states
        plt.plot(probs, label=rf"P{str(state)}")
plt.yticks(np.arange(0, 1.1, 0.1)) # display win probabilities
plt.xlabel("Iteration")
plt.ylabel("Win Probability")
plt.title("Figure 2: Value iteration with Piglet (goal points = 2)")
plt.legend()
plt.grid()
plt.savefig(fr"implementation\Results\Figures\PIGLET_convergence.png", dpi=300) # save figure to report



