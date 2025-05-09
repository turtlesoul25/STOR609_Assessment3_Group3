# import PIGCompetitionSetup.py 
from PIGCompetitionSetup import PIG_competition, optimal_PIG_strategy, hold_at_20_strategy
import random
import numpy as np

def PIG_strat_always_roll(die_size: int, target: int, my_score: int, op_score, my_previous_score: int) -> bool:
    '''
    Implements a PIG strategy of always rolling. 
    
    Arguments
    ----------
    die_size: number of sides on the die
    target: target score to win PIG
    my_score: score for the current player in the current turn
    op_score: saved score(s) for opponent(s)
    my_previous_score: saved score so far for the current player

    Returns
    ----------
    bool: True or False for the decision to "roll" or "stick" the
        dice in the turn, respectively
    '''
    return True



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

