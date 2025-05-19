# Import packages and scripts
from PIGCompetitionSetup import *
import random
import numpy as np
import matplotlib.pyplot as plt

seed = 123
target = 100
die_size = 6
n_rounds = 100000
hold_at_20_strategy = hold_strat_func(20)

################### Hold at 20 #############################
print("---- Hold at 20 ----")
# ---------- Optimal vs hold at 20 player (Optimal player plays first:) -----------
print("Optimal player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_opt = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_20_strategy, first_player=0)
    np.save(fr'implementation\Results\optimal_vs_h20_{n_rounds}_seed{seed}.npy', winners_results_opt) 

# Load tournament results and calculate % of wins for first player
winners_results_opt = np.load(fr"implementation\Results\optimal_vs_h20_{n_rounds}_seed{seed}.npy")
win_percent_opt = sum(winners_results_opt == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_opt = derive_CI(winners_results_opt, n_rounds, alpha=0.01)
CI_95_opt = derive_CI(winners_results_opt, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_opt*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt[0]*100:.3f}, {CI_95_opt[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt[0]*100:.3f}, {CI_99_opt[1]*100:.3f}) \n")



# ---------- Hold at 20 vs optimal player (Hold at ) -player plays ----------
print("Hold at 20 player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_h20 = tournament(n_rounds, target, die_size, hold_at_20_strategy, optimal_PIG_strategy, first_player=0)
    np.save(fr'implementation\Results\h20_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h20) 

# Load tournament results and calculate % of wins for first player
winners_results_h20 = np.load(fr"implementation\Results\h20_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h20 = sum(winners_results_h20 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_h20 = derive_CI(winners_results_h20, n_rounds, alpha=0.01)
CI_95_h20 = derive_CI(winners_results_h20, n_rounds, alpha=0.05)

# Print results
print(f"Hold at 20 player wins {win_percent_h20*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h20[0]*100:.3f}, {CI_95_h20[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h20[0]*100:.3f}, {CI_99_h20[1]*100:.3f}) \n")



# ---------- Hold at 20 vs optimal player (Random first player:) -----------
print("Random first player:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_r20 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_20_strategy, first_player=None)
    np.save(fr'implementation\Results\opt_r_h20_{n_rounds}_seed{seed}.npy', winners_results_r20) 

# Load tournament results and calculate % of wins for first player
winners_results_r20 = np.load(fr"implementation\Results\opt_r_h20_{n_rounds}_seed{seed}.npy")
win_percent_r20 = sum(winners_results_r20 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_r20 = derive_CI(winners_results_r20, n_rounds, alpha=0.01)
CI_95_r20 = derive_CI(winners_results_r20, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_r20*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r20[0]*100:.3f}, {CI_95_r20[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r20[0]*100:.3f}, {CI_99_r20[1]*100:.3f}) \n")



################### Hold at 21 #############################
hold_at_21_strategy = hold_strat_func(21)
print("---- Hold at 21 ----")

# ---------- Optimal vs hold at 21 player (Optimal player plays first:) -----------
print("Optimal player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_opt21 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_21_strategy, first_player=0)
    np.save(fr'implementation\Results\optimal_vs_h21_{n_rounds}_seed{seed}.npy', winners_results_opt21) 

# Load tournament results and calculate % of wins for first player
winners_results_opt21 = np.load(fr"implementation\Results\optimal_vs_h21_{n_rounds}_seed{seed}.npy")
win_percent_opt21 = sum(winners_results_opt21 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_opt21 = derive_CI(winners_results_opt21, n_rounds, alpha=0.01)
CI_95_opt21 = derive_CI(winners_results_opt21, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_opt21*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt21[0]*100:.3f}, {CI_95_opt21[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt21[0]*100:.3f}, {CI_99_opt21[1]*100:.3f}) \n")



# ---------- Hold at 21 vs optimal player (h21 first) -----------
print("Hold at 21 player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_h21 = tournament(n_rounds, target, die_size, hold_at_21_strategy, optimal_PIG_strategy, first_player=0)
    np.save(fr'implementation\Results\h21_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h21) 

# Load tournament results and calculate % of wins for first player
winners_results_h21 = np.load(fr"implementation\Results\h21_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h21 = sum(winners_results_h21 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_h21 = derive_CI(winners_results_h21, n_rounds, alpha=0.01)
CI_95_h21 = derive_CI(winners_results_h21, n_rounds, alpha=0.05)

# Print results
print(f"Hold at 21 player wins {win_percent_h21*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h21[0]*100:.3f}, {CI_95_h21[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h21[0]*100:.3f}, {CI_99_h21[1]*100:.3f}) \n")




# ---------- Hold at 21 vs optimal player (Random first player:) -----------
print("Random first player:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_r21 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_21_strategy, first_player=None)
    np.save(fr'implementation\Results\opt_r_h21_{n_rounds}_seed{seed}.npy', winners_results_r21) 

# Load tournament results and calculate % of wins for first player
winners_results_r21 = np.load(fr"implementation\Results\opt_r_h21_{n_rounds}_seed{seed}.npy")
win_percent_r21 = sum(winners_results_r21 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_r21 = derive_CI(winners_results_r21, n_rounds, alpha=0.01)
CI_95_r21 = derive_CI(winners_results_r21, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_r21*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r21[0]*100:.3f}, {CI_95_r21[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r21[0]*100:.3f}, {CI_99_r21[1]*100:.3f}) \n")






################### Hold at 22 #############################
hold_at_22_strategy = hold_strat_func(22)
print("---- Hold at 22 ----")

# ---------- Optimal vs hold at 22 player (Optimal player plays first:) -----------
print("Optimal player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_opt22 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_22_strategy, first_player=0)
    np.save(fr'implementation\Results\optimal_vs_h22_{n_rounds}_seed{seed}.npy', winners_results_opt22) 

# Load tournament results and calculate % of wins for first player
winners_results_opt22 = np.load(fr"implementation\Results\optimal_vs_h22_{n_rounds}_seed{seed}.npy")
win_percent_opt22 = sum(winners_results_opt22 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_opt22 = derive_CI(winners_results_opt22, n_rounds, alpha=0.01)
CI_95_opt22 = derive_CI(winners_results_opt22, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_opt22*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt22[0]*100:.3f}, {CI_95_opt22[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt22[0]*100:.3f}, {CI_99_opt22[1]*100:.3f}) \n")



# ---------- Hold at 22 vs optimal player (h22 first) -----------
print("Hold at 22 player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_h22 = tournament(n_rounds, target, die_size, hold_at_22_strategy, optimal_PIG_strategy, first_player=0)
    np.save(fr'implementation\Results\h22_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h22) 

# Load tournament results and calculate % of wins for first player
winners_results_h22 = np.load(fr"implementation\Results\h22_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h22 = sum(winners_results_h22 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_h22 = derive_CI(winners_results_h22, n_rounds, alpha=0.01)
CI_95_h22 = derive_CI(winners_results_h22, n_rounds, alpha=0.05)

# Print results
print(f"Hold at 22 player wins {win_percent_h22*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h22[0]*100:.3f}, {CI_95_h22[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h22[0]*100:.3f}, {CI_99_h22[1]*100:.3f}) \n")



# ---------- Hold at 22 vs optimal player (Random first player:) -----------
print("Random first player:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_r22 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_22_strategy, first_player=None)
    np.save(fr'implementation\Results\opt_r_h22_{n_rounds}_seed{seed}.npy', winners_results_r22) 

# Load tournament results and calculate % of wins for first player
winners_results_r22 = np.load(fr"implementation\Results\opt_r_h22_{n_rounds}_seed{seed}.npy")
win_percent_r22 = sum(winners_results_r22 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_r22 = derive_CI(winners_results_r22, n_rounds, alpha=0.01)
CI_95_r22 = derive_CI(winners_results_r22, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_r22*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r22[0]*100:.3f}, {CI_95_r22[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r22[0]*100:.3f}, {CI_99_r22[1]*100:.3f}) \n")






################### Hold at 23 #############################
hold_at_23_strategy = hold_strat_func(23)
print("---- Hold at 23 ----")

# ---------- Optimal vs hold at 23 player (Optimal player plays first:) -----------
print("Optimal player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_opt23 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_23_strategy, first_player=0)
    np.save(fr'implementation\Results\optimal_vs_h23_{n_rounds}_seed{seed}.npy', winners_results_opt23) 

# Load tournament results and calculate % of wins for first player
winners_results_opt23 = np.load(fr"implementation\Results\optimal_vs_h23_{n_rounds}_seed{seed}.npy")
win_percent_opt23 = sum(winners_results_opt23 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_opt23 = derive_CI(winners_results_opt23, n_rounds, alpha=0.01)
CI_95_opt23 = derive_CI(winners_results_opt23, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_opt23*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt23[0]*100:.3f}, {CI_95_opt23[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt23[0]*100:.3f}, {CI_99_opt23[1]*100:.3f}) \n")



# ---------- Hold at 23 vs optimal player (h23 first) -----------
print("Hold at 23 player plays first:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_h23 = tournament(n_rounds, target, die_size, hold_at_23_strategy, optimal_PIG_strategy, first_player=0)
    np.save(fr'implementation\Results\h23_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h23) 

# Load tournament results and calculate % of wins for first player
winners_results_h23 = np.load(fr"implementation\Results\h23_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h23 = sum(winners_results_h23 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_h23 = derive_CI(winners_results_h23, n_rounds, alpha=0.01)
CI_95_h23 = derive_CI(winners_results_h23, n_rounds, alpha=0.05)

# Print results
print(f"Hold at 23 player wins {win_percent_h23*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h23[0]*100:.3f}, {CI_95_h23[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h23[0]*100:.3f}, {CI_99_h23[1]*100:.3f}) \n")



# ---------- Hold at 23 vs optimal player (Random first player:) -----------
print("Random first player:")
perform_competition=False        # Set True if simulation required
if perform_competition:
    random.seed(seed)
    winners_results_r23 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_23_strategy, first_player=None)
    np.save(fr'implementation\Results\opt_r_h23_{n_rounds}_seed{seed}.npy', winners_results_r23) 

# Load tournament results and calculate % of wins for first player
winners_results_r23 = np.load(fr"implementation\Results\opt_r_h23_{n_rounds}_seed{seed}.npy")
win_percent_r23 = sum(winners_results_r23 == 0)/n_rounds

# Confidence intervals (99% and 95%)
CI_99_r23 = derive_CI(winners_results_r23, n_rounds, alpha=0.01)
CI_95_r23 = derive_CI(winners_results_r23, n_rounds, alpha=0.05)

# Print results
print(f"Optimal player wins {win_percent_r23*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r23[0]*100:.3f}, {CI_95_r23[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r23[0]*100:.3f}, {CI_99_r23[1]*100:.3f}) \n")




############### CI Plots ##########################

# Function to generate the confidence interval plot
def CI_plots(paper_win, mean_list, CI_95_list, CI_99_list, strategy_label="optimal", figtitle=None):
    opp_strategy = ["Hold at 20", "Hold at 21", "Hold at 22", "Hold at 23"]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(opp_strategy, [m*100 for m in mean_list], label=fr"$\%$ of {strategy_label} strategy wins")
    ax.axhline(y=paper_win, linestyle="--", label=r"$\%$ claimed by Neller and Presser")
    ax.fill_between(opp_strategy,
                    [ci[0]*100 for ci in CI_95_list],
                    [ci[1]*100 for ci in CI_95_list],
                    color='blue', alpha=0.1, label='95% Confidence Interval')
    ax.fill_between(opp_strategy,
                    [ci[0]*100 for ci in CI_99_list],
                    [ci[1]*100 for ci in CI_99_list],
                    color='blue', alpha=0.1, label='99% Confidence Interval')
    ax.set_ylabel(r"$\%$ wins")
    ax.set_xlabel("Opponent strategy")
    ax.set_title(figtitle)
    leg = ax.legend()
    leg.legend_handles[2].set_alpha(0.2)

    return fig

# Results for optimal player vs hold at n for n = 20, 21, 22, 23 stored in lists
## Optimal player plays first
opt_mean = [win_percent_opt, win_percent_opt21, win_percent_opt22, win_percent_opt23]
opt_95_CI = [CI_95_opt, CI_95_opt21, CI_95_opt22, CI_95_opt23]
opt_99_CI = [CI_99_opt, CI_99_opt21, CI_99_opt22, CI_99_opt23]

## Optimal player plays second
hn_mean = [win_percent_h20, win_percent_h21, win_percent_h22, win_percent_h23]
hn_95_CI = [CI_95_h20, CI_95_h21, CI_95_h22, CI_95_h23]
hn_99_CI = [CI_99_h20, CI_99_h21, CI_99_h22, CI_99_h23]

## Random player plays first
r_mean = [win_percent_r20, win_percent_r21, win_percent_r22, win_percent_r23]
r_95_CI = [CI_95_r20, CI_95_r21, CI_95_r22, CI_95_r23]
r_99_CI = [CI_99_r20, CI_99_r21, CI_99_r22, CI_99_r23]


optimal_player_first_fig = CI_plots(58.74, mean_list=opt_mean, 
                                    CI_95_list=opt_95_CI, CI_99_list=opt_99_CI, 
                                    figtitle=r"$\%$ of optimal player wins when optimal player goes first")
plt.savefig(fr'implementation\Results\Figures\CI_plot_optimal_p1.png', dpi=300)
plt.close(optimal_player_first_fig)


optimal_player_second_fig = CI_plots(47.76, mean_list=hn_mean, 
                                     CI_95_list=hn_95_CI, CI_99_list=hn_99_CI, strategy_label=r"hold at $n$",
                                     figtitle=r"$\%$ of hold at $n$ player wins when optimal player goes second")
plt.savefig(fr'implementation\Results\Figures\CI_plot_optimal_p2.png', dpi=300)
plt.close(optimal_player_second_fig)


random_player_first_fig = CI_plots(55.49, mean_list=r_mean, 
                                     CI_95_list=r_95_CI, CI_99_list=r_99_CI,
                                     figtitle=r"$\%$ of optimal player wins when random player goes first")
plt.savefig(fr'implementation\Results\Figures\CI_plot_random_p1.png', dpi=300)
plt.close(random_player_first_fig)
