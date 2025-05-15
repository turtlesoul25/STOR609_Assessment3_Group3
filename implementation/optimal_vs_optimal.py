from PIGCompetitionSetup import PIG_competition, optimal_PIG_strategy, hold_at_20_strategy
import random
import numpy as np
from scipy.stats import norm


random.seed(123)
target = 100
die_size = 6

# Optimal player vs optimal player
n_rounds = 100000
# winners_opt1 = np.zeros(n_rounds)
# for i in range(n_rounds):
#     print(f"Round: {i+1}")
#     winners_opt1[i] = PIG_competition(target, die_size, 
#                                       strats=[optimal_PIG_strategy, optimal_PIG_strategy],
#                                       nplayers=2, p1=0)[0]
    

# print(winners_opt1)
# print(sum(winners_opt1==0)/n_rounds)

# np.save(f'implementation\Results\optimal_vs_optimal_{n_rounds}.npy', winners_opt1) 
winners_opt1 = np.load(f"implementation\Results\optimal_vs_optimal_{n_rounds}.npy")
print(sum(winners_opt1 == 0)/n_rounds)

# Confidence interval
sample_mean = sum(winners_opt1==0)/n_rounds
st_error = np.std(winners_opt1)/np.sqrt(n_rounds)
quantile = norm.ppf(0.995) # 95% CI 
lower_ci = sample_mean - st_error*quantile
upper_ci = sample_mean + st_error*quantile
print(f"[{lower_ci:.5f}, {upper_ci:.5f}]")



