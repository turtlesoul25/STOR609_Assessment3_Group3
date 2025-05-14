# import PIGCompetitionSetup.py 
from PIGCompetitionSetup import PIG_competition, optimal_PIG_strategy, hold_at_20_strategy
import random
import numpy as np

seed=123
target = 100
die_size = 6
n_rounds = 100000

# -------- h20 vs optimal ---------------------
random.seed(seed)
winners_opt2 = np.zeros(n_rounds)
for i in range(n_rounds):
    print(f"Round: {i+1}")
    winners_opt2[i] = PIG_competition(target, die_size, 
                                      strats=[hold_at_20_strategy, optimal_PIG_strategy],
                                      nplayers=2, p1=0)[0]
    

print(winners_opt2)
print(sum(winners_opt2==0)/n_rounds)

# np.save(f'implementation\Results\h20_vs_optimal_{n_rounds}_seed{seed}.npy', winners_opt2) 
# winners_results = np.load(f"implementation\Results\h20_vs_optimal_{n_rounds}_seed{seed}.npy")
# print(sum(winners_results == 0)/n_rounds)

# ------------- optimal vs h20 ----------------
random.seed(seed)
winners_opt1 = np.zeros(n_rounds)
for i in range(n_rounds):
    print(f"Round: {i+1}")
    winners_opt1[i] = PIG_competition(target, die_size, 
                                      strats=[optimal_PIG_strategy, hold_at_20_strategy],
                                      nplayers=2, p1=0)[0]
    

print(winners_opt1)
print(sum(winners_opt1==0)/n_rounds)

# np.save(f'implementation\Results\optimal_vs_h20_{n_rounds}_seed{seed}.npy', winners_opt1) 
# winners_results = np.load(f"implementation\Results\optimal_vs_h20_{n_rounds}_seed{seed}.npy")
# print(sum(winners_results == 0)/n_rounds)

