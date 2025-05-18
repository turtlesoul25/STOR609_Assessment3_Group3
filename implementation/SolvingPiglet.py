from PIG import value_iteration, pig_value_func, piglet_value_func, generate_PIG_states, generate_PIGLET_states
import matplotlib.pyplot as plt
import numpy as np
import pickle

target = 2
S = generate_PIGLET_states(target)
A = {"flip", "hold"}
bellman_piglet = piglet_value_func(target)
V_init = dict([(s, 0) for s in S])
V_init[("Win", "Lose", 0)] = 1

results = value_iteration(S=S, A=A, P=None, R=None, 
                          gamma=1, max_iterations=100, 
                          V_init=V_init, bellman_eq=bellman_piglet)

pickle.dump(results, open(fr'implementation\Results\PIGLET_results_target_{target}.pkl', 'wb'))
results_loaded = pickle.load(open(fr'implementation\Results\PIGLET_results_target_{target}.pkl', 'rb'))

piglet_optimal_policy = results_loaded["optimal_policy"]
piglet_optimal_prob_winning = results_loaded["value_function"]
for s in S:
    print(f"P(winning at {s}) if {piglet_optimal_policy[s]}: {piglet_optimal_prob_winning[s]:.4f}")

# # Uncomment only if new results needed
# with open(fr'implementation\Results\PIGLET_results_target_{target}.pkl', 'wb') as f:
#     pickle.dump(results, f)


# Produce convergence plot for PIGLET
piglet_prob_winning = dict((s, []) for s in S)
for its in range(25):
    value_function = value_iteration(S=S, A=A, P=None, R=None, 
                          gamma=1, max_iterations=its, 
                          V_init=V_init, bellman_eq=bellman_piglet)["value_function"]
    for key, value in piglet_prob_winning.items():
        piglet_prob_winning[key].append(value_function[key])


fig, ax = plt.subplots()
for state, probs in piglet_prob_winning.items():
    if state not in [("Win", "Lose", 0), ("Lose", "Win", 0)]:
        plt.plot(probs, label=rf"P{str(state)}")
plt.legend()
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel("Iteration")
plt.ylabel("Win Probability")
plt.title("Value iteration with Piglet (goal points = 2)")
plt.grid()
plt.savefig(fr"implementation\Results\Figures\PIGLET_convergence.png", dpi=300)



