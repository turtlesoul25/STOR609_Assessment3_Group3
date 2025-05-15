from PIGCompetitionSetup import *
import random
import numpy as np

seed = 123
target = 100
die_size = 6
n_rounds = 100000
hold_at_20_strategy = hold_strat_func(20)

################### Hold at 20 #############################
print("Hold at 20")
# ---------- Optimal vs hold at 20 player (opt first) -----------
print("opt first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_opt = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_20_strategy, first_player=0)
    np.save(f'implementation\Results\optimal_vs_h20_{n_rounds}_seed{seed}.npy', winners_results_opt) 


winners_results_opt = np.load(f"implementation\Results\optimal_vs_h20_{n_rounds}_seed{seed}.npy")
win_percent_opt = sum(winners_results_opt == 0)/n_rounds

# Confidence interval
CI_99_opt = derive_CI(winners_results_opt, n_rounds, alpha=0.01)
CI_95_opt = derive_CI(winners_results_opt, n_rounds, alpha=0.05)

print(f"Optimal player wins {win_percent_opt*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt[0]*100:.3f}, {CI_95_opt[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt[0]*100:.3f}, {CI_99_opt[1]*100:.3f})")



# ---------- Hold at 20 vs optimal player (h20 first) -----------
print("h20 first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_h20 = tournament(n_rounds, target, die_size, hold_at_20_strategy, optimal_PIG_strategy, first_player=0)
    np.save(f'implementation\Results\h20_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h20) 


winners_results_h20 = np.load(f"implementation\Results\h20_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h20 = sum(winners_results_h20 == 0)/n_rounds

# Confidence interval
CI_99_h20 = derive_CI(winners_results_h20, n_rounds, alpha=0.01)
CI_95_h20 = derive_CI(winners_results_h20, n_rounds, alpha=0.05)

print(f"Hold at 20 player wins {win_percent_h20*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h20[0]*100:.3f}, {CI_95_h20[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h20[0]*100:.3f}, {CI_99_h20[1]*100:.3f})")



# ---------- Hold at 20 vs optimal player (random start) -----------
print("random start")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_r20 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_20_strategy, first_player=None)
    np.save(f'implementation\Results\opt_r_h20_{n_rounds}_seed{seed}.npy', winners_results_r20) 


winners_results_r20 = np.load(f"implementation\Results\opt_r_h20_{n_rounds}_seed{seed}.npy")
win_percent_r20 = sum(winners_results_r20 == 0)/n_rounds

# Confidence interval
CI_99_r20 = derive_CI(winners_results_r20, n_rounds, alpha=0.01)
CI_95_r20 = derive_CI(winners_results_r20, n_rounds, alpha=0.05)

print(f"Opt player wins {win_percent_r20*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r20[0]*100:.3f}, {CI_95_r20[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r20[0]*100:.3f}, {CI_99_r20[1]*100:.3f})")



################### Hold at 21 #############################
hold_at_21_strategy = hold_strat_func(21)
print("Hold at 21")

# ---------- Optimal vs hold at 21 player (opt first) -----------
print("opt first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_opt21 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_21_strategy, first_player=0)
    np.save(f'implementation\Results\optimal_vs_h21_{n_rounds}_seed{seed}.npy', winners_results_opt21) 


winners_results_opt21 = np.load(f"implementation\Results\optimal_vs_h21_{n_rounds}_seed{seed}.npy")
win_percent_opt21 = sum(winners_results_opt21 == 0)/n_rounds

# Confidence interval
CI_99_opt21 = derive_CI(winners_results_opt21, n_rounds, alpha=0.01)
CI_95_opt21 = derive_CI(winners_results_opt21, n_rounds, alpha=0.05)

print(f"Optimal player wins {win_percent_opt21*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt21[0]*100:.3f}, {CI_95_opt21[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt21[0]*100:.3f}, {CI_99_opt21[1]*100:.3f})")



# ---------- Hold at 21 vs optimal player (h21 first) -----------
print("h21 first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_h21 = tournament(n_rounds, target, die_size, hold_at_21_strategy, optimal_PIG_strategy, first_player=0)
    np.save(f'implementation\Results\h21_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h21) 


winners_results_h21 = np.load(f"implementation\Results\h21_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h21 = sum(winners_results_h21 == 0)/n_rounds

# Confidence interval
CI_99_h21 = derive_CI(winners_results_h21, n_rounds, alpha=0.01)
CI_95_h21 = derive_CI(winners_results_h21, n_rounds, alpha=0.05)

print(f"Hold at 21 player wins {win_percent_h21*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h21[0]*100:.3f}, {CI_95_h21[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h21[0]*100:.3f}, {CI_99_h21[1]*100:.3f})")




# ---------- Hold at 21 vs optimal player (random start) -----------
print("random start")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_r21 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_21_strategy, first_player=None)
    np.save(f'implementation\Results\opt_r_h21_{n_rounds}_seed{seed}.npy', winners_results_r21) 


winners_results_r21 = np.load(f"implementation\Results\opt_r_h21_{n_rounds}_seed{seed}.npy")
win_percent_r21 = sum(winners_results_r21 == 0)/n_rounds

# Confidence interval
CI_99_r21 = derive_CI(winners_results_r21, n_rounds, alpha=0.01)
CI_95_r21 = derive_CI(winners_results_r21, n_rounds, alpha=0.05)

print(f"Opt player wins {win_percent_r21*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r21[0]*100:.3f}, {CI_95_r21[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r21[0]*100:.3f}, {CI_99_r21[1]*100:.3f})")






################### Hold at 22 #############################
hold_at_22_strategy = hold_strat_func(22)
print("Hold at 22")

# ---------- Optimal vs hold at 22 player (opt first) -----------
print("opt first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_opt22 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_22_strategy, first_player=0)
    np.save(f'implementation\Results\optimal_vs_h22_{n_rounds}_seed{seed}.npy', winners_results_opt22) 


winners_results_opt22 = np.load(f"implementation\Results\optimal_vs_h22_{n_rounds}_seed{seed}.npy")
win_percent_opt22 = sum(winners_results_opt22 == 0)/n_rounds

# Confidence interval
CI_99_opt22 = derive_CI(winners_results_opt22, n_rounds, alpha=0.01)
CI_95_opt22 = derive_CI(winners_results_opt22, n_rounds, alpha=0.05)

print(f"Optimal player wins {win_percent_opt22*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt22[0]*100:.3f}, {CI_95_opt22[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt22[0]*100:.3f}, {CI_99_opt22[1]*100:.3f})")



# ---------- Hold at 22 vs optimal player (h22 first) -----------
print("h22 first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_h22 = tournament(n_rounds, target, die_size, hold_at_22_strategy, optimal_PIG_strategy, first_player=0)
    np.save(f'implementation\Results\h22_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h22) 


winners_results_h22 = np.load(f"implementation\Results\h22_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h22 = sum(winners_results_h22 == 0)/n_rounds

# Confidence interval
CI_99_h22 = derive_CI(winners_results_h22, n_rounds, alpha=0.01)
CI_95_h22 = derive_CI(winners_results_h22, n_rounds, alpha=0.05)

print(f"Hold at 22 player wins {win_percent_h22*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h22[0]*100:.3f}, {CI_95_h22[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h22[0]*100:.3f}, {CI_99_h22[1]*100:.3f})")



# ---------- Hold at 22 vs optimal player (random start) -----------
print("random start")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_r22 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_22_strategy, first_player=None)
    np.save(f'implementation\Results\opt_r_h22_{n_rounds}_seed{seed}.npy', winners_results_r22) 


winners_results_r22 = np.load(f"implementation\Results\opt_r_h22_{n_rounds}_seed{seed}.npy")
win_percent_r22 = sum(winners_results_r22 == 0)/n_rounds

# Confidence interval
CI_99_r22 = derive_CI(winners_results_r22, n_rounds, alpha=0.01)
CI_95_r22 = derive_CI(winners_results_r22, n_rounds, alpha=0.05)

print(f"Opt player wins {win_percent_r22*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r22[0]*100:.3f}, {CI_95_r22[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r22[0]*100:.3f}, {CI_99_r22[1]*100:.3f})")






################### Hold at 23 #############################
hold_at_23_strategy = hold_strat_func(23)
print("Hold at 23")

# ---------- Optimal vs hold at 23 player (opt first) -----------
print("opt first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_opt23 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_23_strategy, first_player=0)
    np.save(f'implementation\Results\optimal_vs_h23_{n_rounds}_seed{seed}.npy', winners_results_opt23) 


winners_results_opt23 = np.load(f"implementation\Results\optimal_vs_h23_{n_rounds}_seed{seed}.npy")
win_percent_opt23 = sum(winners_results_opt23 == 0)/n_rounds

# Confidence interval
CI_99_opt23 = derive_CI(winners_results_opt23, n_rounds, alpha=0.01)
CI_95_opt23 = derive_CI(winners_results_opt23, n_rounds, alpha=0.05)

print(f"Optimal player wins {win_percent_opt23*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_opt23[0]*100:.3f}, {CI_95_opt23[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_opt23[0]*100:.3f}, {CI_99_opt23[1]*100:.3f})")



# ---------- Hold at 23 vs optimal player (h23 first) -----------
print("h23 first")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_h23 = tournament(n_rounds, target, die_size, hold_at_23_strategy, optimal_PIG_strategy, first_player=0)
    np.save(f'implementation\Results\h23_vs_optimal_{n_rounds}_seed{seed}.npy', winners_results_h23) 


winners_results_h23 = np.load(f"implementation\Results\h23_vs_optimal_{n_rounds}_seed{seed}.npy")
win_percent_h23 = sum(winners_results_h23 == 0)/n_rounds

# Confidence interval
CI_99_h23 = derive_CI(winners_results_h23, n_rounds, alpha=0.01)
CI_95_h23 = derive_CI(winners_results_h23, n_rounds, alpha=0.05)

print(f"Hold at 23 player wins {win_percent_h23*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_h23[0]*100:.3f}, {CI_95_h23[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_h23[0]*100:.3f}, {CI_99_h23[1]*100:.3f})")



# ---------- Hold at 23 vs optimal player (random start) -----------
print("random start")
perform_competition=False
if perform_competition:
    random.seed(seed)
    winners_results_r23 = tournament(n_rounds, target, die_size, optimal_PIG_strategy, hold_at_23_strategy, first_player=None)
    np.save(f'implementation\Results\opt_r_h23_{n_rounds}_seed{seed}.npy', winners_results_r23) 


winners_results_r23 = np.load(f"implementation\Results\opt_r_h23_{n_rounds}_seed{seed}.npy")
win_percent_r23 = sum(winners_results_r23 == 0)/n_rounds

# Confidence interval
CI_99_r23 = derive_CI(winners_results_r23, n_rounds, alpha=0.01)
CI_95_r23 = derive_CI(winners_results_r23, n_rounds, alpha=0.05)

print(f"Opt player wins {win_percent_r23*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95_r23[0]*100:.3f}, {CI_95_r23[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99_r23[0]*100:.3f}, {CI_99_r23[1]*100:.3f})")