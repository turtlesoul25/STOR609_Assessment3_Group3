# Import packages
from typing import Set, Callable, Dict


# Define the value iteration algorithm as a function
def value_iteration(S: Set, A: Set, P: Callable, R: Callable, gamma: float, max_iterations: int,
                    bellman_eq: Callable, V_init: Dict = None, theta: float = None) -> Dict:
    '''
    Implements the value iteration algorithm to solve a MDP with given
    set of states and actions, transition probabilities, reward function, 
    and discount factor (gamma)

    Arguments
    -----------
    S: Set of states for the MDP.
    A: Set of actions for the MDP.
    P: A function which calculates P(s'|s,a), the probability of transitioning
        to state s' given we are in state s and execute action a.
    R: A function which calculates R(s,a), the reward obtainined if action a is 
        executed while in state s.
    gamma: Discount factor for calculating the next value function in the MDP.
    max_iterations: maximum number of iterations of value function calculations.
    bellman_eq: a function defining the value function update at each iteration.
    V_init: A dictionary to store the initialised values for all states.
    theta: Threshold value to check convergence of the value function 
        to ensure minimum value function update across all states per iteration.

    Output
    -----------
    output_dict: Dictionary containing the optimal policy dictionary and final value function dictionary for all states
    '''

    # Dictionaries containing value function entries for each state
    Vk = dict([(s, 0) for s in S]) if V_init is None else V_init
    V_next = dict([(s, 0) for s in S])

    # Dictionary to store optimal policy for each state
    policy = dict([(s, 0) for s in S])

    k = 0 # iteration counter

    while k < max_iterations: # Iteration termination condition
        # print(Vk)
        delta = 0       # Factor to check convergence of value function
        k = k+1         # Increment iterations
        for s in S:     # Update value function for each state in new iteration
            V_next[s] = max(bellman_eq(s, A, P, R, Vk).values())
            delta = max(delta, abs(V_next[s] - Vk[s]))
        Vk = V_next      # Update penultimate value function for all states for next iteration
        if theta != None and delta < theta: # Convergence (termination) condition for value function (if applicable)
            break

    for s in S: # Store optimal policy for each state
        policy[s] = max(bellman_eq(s, A, P, R, Vk), key = bellman_eq(s, A, P, R, Vk).get)

    return {"optimal_policy": policy, "value_function": V_next}



def generate_PIGLET_states(target):
    S = set()
    for i in range(target):  # player score
        for j in range(target):  # opponent score
            for k in range(target):  # turn score
                if i+k >= target:  # Skip if a player has already won
                    continue
                S.add((i, j, k))
                
    # Add terminal states
    S.add(("Win", "Lose", 0)) 
    S.add(("Lose", "Win", 0)) 

    return S


def piglet_value_func(target):
    def bellman_piglet(s, A, P, R, V, target=target):
        values = dict((a, 0) for a in A) # value function at s for each action
        i, j, k = s

        if i == "Win": # If at terminal win state, always hold
            values["hold"] = 1
            return values
        elif i == "Lose": # If at terminal lose state, always hold, prob of winning is 0
            return values
        
        for a in A: # calculate value for each action at s
            if a == "flip":
                s_heads = ("Win", "Lose", 0) if i + k + 1 >= target else (i, j, k+1) # heads outcome
                values[a] = (1 - V[(j, i, 0)] + V[s_heads])/2
            elif a == "hold":
                values[a] = 1 - V[(j, i+k, 0)]
                
        return values
    
    return bellman_piglet


def generate_PIG_states(target):
    S = set()
    for i in range(target):  # player score
        for j in range(target):  # opponent score
            for k in range(target):  # turn score
                if i+k>= target:   # Skip if player has already won
                    continue
                S.add((i, j, k))

    # Add terminal states
    S.add(("Win", "Lose", 0))
    S.add(("Lose", "Win", 0)) 

    return S

def pig_value_func(target, die_size):
    def bellman_PIG(s, A, P, R, V, target=target, die_size=die_size):
        values = dict((a, 0) for a in A)
        i, j, k = s

        if i == "Win": # If at terminal win state, always hold
            return values
        
        elif i == "Lose": # If at terminal lose state, always hold, prob of winning is 0
            return values
        
        for a in A:
            if a == "roll":
                V_good_roll = [V[(i, j, k+r)] if i + k + r < target 
                               else V[("Win", "Lose", 0)] for r in range(2,7)]
                values[a] = (1 - V[(j, i, 0)] + sum(V_good_roll))/die_size
            elif a == "hold":
                values[a] = 1 - V[(j, i+k, 0)]

        return values
    return bellman_PIG