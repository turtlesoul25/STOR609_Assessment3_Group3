# Import packages
import random
import numpy as np
import math
from numpy.typing import NDArray
from typing import List, Callable
import pickle
from scipy.stats import norm

def roll_die(die_size: int) -> int:
    ''' 
    Generates a random number to simulate a fair die roll with die_size sides
    
    Arguments
    ----------
    die_size: number of sides on the die

    Returns
    ----------
    int: a random number between 1 and die_size (inclusive)
    '''

    return random.randint(1, die_size)

def check_winner(target: int, scores: NDArray[np.int_]) -> bool:
    ''' 
    Checks scores of all players to see if any player has reached the target score to win the game
    
    Arguments
    ----------
    target: target score to declare a winner
    scores: current scores of all players

    Returns
    ----------
    bool: True if there is a winner, False otherwise
    '''

    if np.any(scores >= target): # winner
        return True
    else: # no winner yet
        return False
    
def find_winner(target: int, scores: NDArray[np.int_]) -> int:
    ''' 
    Checks scores of all players to find which player has won the game. 
    Assumes that a winner has been found using check_winner()
    
    Arguments
    ----------
    target: target score to declare a winner
    scores: current scores of all players

    Returns
    ----------
    int: player number (numbered from 1 to n for n players)
    '''

    return np.nonzero(scores>=target)[0][0] # player number (indexed from 1 to n)


    
def choose_player(nplayers: int, previous_player:int = None) -> int:
    ''' 
    Chooses a player to play for the current turn given the most recent player (if any).
    Players are indexed from 0 to nplayers-1.
    If no previous player, uniformly choose a random player.

    Arguments
    ----------
    nplayers: number of players in the game
    previous_player: player who played the most recent turn (if any)

    Returns
    ----------
    int: player number (numbered from 0 to nplayers-1)
    '''

    if previous_player != None: # known previous player
        return (previous_player + 1) % nplayers
    else: # choose first player
        return random.randint(0, nplayers-1)
    


def PIG_competition(target: int, die_size: int, 
                    strats: list[Callable[[int, int, int, NDArray[np.int_], int], bool]], 
                    nplayers:int = 2, p1:int = None) -> List[int]:
    ''' 
    Simulates the PIG competition for n players who each use their own strategy
    for a target score with a given number of sides on the die.

    Arguments
    ----------
    target: target score for the game
    die_size: number of sides on the die
    strats: list of strategies for each player
    nplayers: number of players in the game
    p1: player number for the first player

    Returns
    ----------
    winner: player number of the winner (numbered from 0 to nplayers-1)
    winner_score: score of the winning player
    '''

    # Set initial scores as 0
    scores = np.zeros(nplayers)

    # Choose the first player
    if p1 == None:
        turn = choose_player(nplayers)
    else:
        turn = (p1) % nplayers

    while not np.any(scores >= target):
        # Start the score for the current player's turn
        # print("Turn:", turn+1, scores)
        turn_score = 0
        strat = strats[turn]

        # Check if the player wants to stick or roll
        if not strat(die_size, target, turn_score, np.delete(scores, turn), scores[turn]):
            scores[turn] += turn_score
            turn = choose_player(nplayers, turn)
            continue 
        
        rolled_num = die_size
        while rolled_num > 1:
            if not strat(die_size, target, turn_score, np.delete(scores, turn), scores[turn]):
                # If stick, update score and end player's turn
                scores[turn] += turn_score
                break

            # If player wants to roll
            rolled_num = random.randint(1, die_size)

            if rolled_num == 1: # End turn of player
                break

            else: # Update turn score and see if this lets the player win
                turn_score += rolled_num
                forecast_scores = scores.copy() 
                forecast_scores[turn] = scores[turn] + turn_score # potential score if player stops playing here
                if np.any(forecast_scores >= target):   # If player wins with this roll, update scores and end the loop
                    scores = forecast_scores
                    break

        turn = choose_player(nplayers, turn) # Choose the next player in the list of players
    
    winner = find_winner(target, scores) # Find winner and the score of the winner
    return winner, scores[winner]

target = 100
die_size = 6
optimal_results = pickle.load(open(f'implementation\Results\PIG_staged_results_target_{target}_diesize_{die_size}.pkl', 'rb'))

def optimal_PIG_strategy(die_size: int, target: int, turn_score: int, op_score: NDArray[np.int_], player_score: int) -> bool:
    '''
    For a given state of the Pig game, return whether optimal policy rolls as a Boolean
    '''

    i, j, k = int(player_score), int(max(op_score)), int(turn_score)
    if i + k >= target:
        i, j, k = "Win", "Lose", 0
    optimal_policy = optimal_results["optimal_policy"]
    
    return optimal_policy[(i, j, k)] == "roll"


def hold_strat_func(n):
    '''
    For a given state of the Pig game, return whether "hold at n" policy rolls as a Boolean
    '''

    def hold_at_n_strategy(die_size: int, target: int, turn_score: int, op_score: NDArray[np.int_], player_score: int) -> bool:
        return turn_score < n
    return hold_at_n_strategy


def derive_CI(comp_results: NDArray[np.int_], n_rounds: int, alpha: float) -> List:
    ''' 
    Requires the results (which player won) of a complete simulation of the Pig game for a given number of rounds.
    Computes confidence interval for probability that Player 1 won the game. up to a significance level of alpha.

    Arguments
    ----------
    comp_results: numpy array of competition results (0 or 1, to indicate Player 1 or 2 won, respectively)
    n_rounds: number of rounds (== length of comp_results)
    alpha: desired significance level of CI (e.g. 0.05 for 95% CI)

    Returns
    ----------
    [lower_ci, upper_ci]: confidence interval, where:
    lower_ci: lower endpoint of CI
    upper_ci: upper endpoint of CI
    '''

    mean_win_percent = sum(comp_results == 0)/n_rounds  # estimate of p (probability P1 won)
    std_err = np.std(comp_results)/np.sqrt(n_rounds)    # standard error
    quant = norm.ppf(1-alpha/2)                       # normal quantile
    lower_ci = mean_win_percent - (std_err*quant)
    upper_ci = mean_win_percent + (std_err*quant)
    return [lower_ci, upper_ci]


def tournament(n_rounds, target, die_size, p1strat, p2strat, first_player=0) -> NDArray[np.int_]:
    ''' 
    Runs a tournament of Pig for a given number of rounds, target score, die size, and starting player.
    Both players are assumed to be using the same policy in each round.

    Arguments
    ----------
    n_rounds: number of rounds
    target: target score of the game
    die_size: number of sides on the die
    p1strat: policy of Player 1 in the tournament
    p2strat: policy of Player 2 in the tournament
    first_player: starting player in each round (if no argument given, can be randomised)

    Returns
    ----------
    comp_results: numpy array containing tournament results (0 if Player 1 won a round, 1 if Player 2 won a round)
    '''
    
    comp_results = np.zeros(n_rounds)
    for i in range(n_rounds):
        comp_results[i] = PIG_competition(target, die_size, 
                                             strats=[p1strat, p2strat],
                                             nplayers=2, p1=first_player)[0]
    
    return comp_results