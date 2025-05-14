from PIGCompetitionSetup import PIG_competition, optimal_PIG_strategy, hold_at_20_strategy
import random
import numpy as np


random.seed(123)
target = 100
die_size = 6

# Optimal player vs optimal player
n_rounds = 1000
winners_opt1 = np.zeros(n_rounds)
for i in range(n_rounds):
    print(f"Round: {i+1}")
    winners_opt1[i] = PIG_competition(target, die_size, 
                                      strats=[optimal_PIG_strategy, optimal_PIG_strategy],
                                      nplayers=2, p1=1)[0]
    

print(winners_opt1)
print(sum(winners_opt1==1)/n_rounds)

np.save(f'implementation\Results\optimal_vs_optimal_{n_rounds}.npy', winners_opt1) 
# winners_results = np.load("implementation\Results\optimal_vs_optimal.npy")
# print(sum(winners_results == 2)/n_rounds)



