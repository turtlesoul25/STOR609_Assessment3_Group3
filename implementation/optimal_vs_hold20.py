# import PIGCompetitionSetup.py 
from PIGCompetitionSetup import PIG_competition, optimal_PIG_strategy, hold_at_20_strategy
import random
import numpy as np


random.seed(123)
target = 100
die_size = 6

# 
n_rounds = 50
winners_opt2 = np.zeros(n_rounds)
for i in range(n_rounds):
    print(f"Round: {i+1}")
    winners_opt2[i] = PIG_competition(target, die_size, 
                                      strats=[hold_at_20_strategy, optimal_PIG_strategy],
                                      nplayers=2, p1=2)[0]
    

print(winners_opt2)
print(sum(winners_opt2==2)/n_rounds)


winners_opt1 = np.zeros(n_rounds)
for i in range(n_rounds):
    print(f"Round: {i+1}")
    winners_opt1[i] = PIG_competition(target, die_size, 
                                      strats=[optimal_PIG_strategy, hold_at_20_strategy],
                                      nplayers=2, p1=2)[0]
    

print(winners_opt1)
print(sum(winners_opt1==1)/n_rounds)

