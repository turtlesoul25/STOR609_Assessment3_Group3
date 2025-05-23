# Import packages
from PIGCompetitionSetup import *
import random
import numpy as np

# Parameters for competition simulation
target = 100        # target score
die_size = 6        # number of sides in die
n_rounds = 100000   # number of competitions in the tournament

# Optimal player vs optimal player
perform_competition = False      # Set to True if simulation needed
if perform_competition:
    random.seed(123) # set seed at start of tournament
    winners_results = tournament(n_rounds, target, die_size, optimal_PIG_strategy, optimal_PIG_strategy, first_player=0)
    np.save(fr'implementation\Results\optimal_vs_optimal_{n_rounds}.npy', winners_results)  # save results from tournament

# Load tournament results
winners_results = np.load(f"implementation\Results\optimal_vs_optimal_{n_rounds}.npy")
win_percent = sum(winners_results == 0)/n_rounds  # percent of times that first optimal player wins

# Confidence interval (99% and 95%)
CI_99 = derive_CI(winners_results, n_rounds, alpha=0.01)
CI_95 = derive_CI(winners_results, n_rounds, alpha=0.05)

# Print results for report
print(f"Optimal player wins {win_percent*100:.3f}% of the time.")
print(f"95% Confidence Interval: ({CI_95[0]*100:.3f}, {CI_95[1]*100:.3f})")
print(f"99% Confidence Interval: ({CI_99[0]*100:.3f}, {CI_99[1]*100:.3f})")