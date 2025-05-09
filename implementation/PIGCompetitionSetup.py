# Import packages
import random
import numpy as np
import math
from numpy.typing import NDArray
from typing import List, Callable
import pickle

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

    n = len(scores) # number of players
    player_nums = [i+1 for i in range(n)] # labels for each player
    return player_nums[np.nonzero(scores>=target)[0][0]] # player number (indexed from 1 to n)


    
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
        return math.floor(random.uniform(0, nplayers-1))
    


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
        turn = (p1 - 1) % nplayers

    while not check_winner(target, scores):
        # Start the score for the current player's turn
        # print("Turn:", turn+1, scores)
        turn_score = 0
        strat = strats[turn]

        # Check if the player wants to stick or roll
        if not strat(die_size, target, turn_score, np.delete(scores, turn), scores[turn]):
            continue 
        
        rolled_num = die_size
        while rolled_num > 1:
            if not strat(die_size, target, turn_score, np.delete(scores, turn), scores[turn]):
                # If stick, update score and end player's turn
                scores[turn] += turn_score
                break

            # If player wants to roll
            rolled_num = roll_die(die_size)

            if rolled_num == 1: # End turn of player
                break

            else: # Update turn score and see if this lets the player win
                turn_score += rolled_num
                forecast_scores = scores 
                forecast_scores[turn] = scores[turn] + turn_score # potential score if player stops playing here
                if check_winner(target, forecast_scores):   # If player wins with this roll, update scores and end the loop
                    scores = forecast_scores
                    break

        turn = choose_player(nplayers, turn) # Choose the next player in the list of players
    
    winner = find_winner(target, scores) # Find winner and the score of the winner
    return winner, scores[winner - 1]


def optimal_PIG_strategy(die_size: int, target: int, turn_score: int, op_score: NDArray[np.int_], player_score: int) -> bool:
    i, j, k = int(player_score), int(max(op_score)), int(turn_score)
    if i + k >= target:
        i, j, k = "Win", "Lose", 0
    optimal_results = pickle.load(open(f'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'rb'))
    optimal_policy = optimal_results["optimal_policy"]
    
    return optimal_policy[(i, j, k)] == "roll"


def hold_at_20_strategy(die_size: int, target: int, turn_score: int, op_score: NDArray[np.int_], player_score: int) -> bool:
    return turn_score <= 20

