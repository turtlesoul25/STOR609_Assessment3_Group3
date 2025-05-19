# Import packages
from typing import Set, Callable, Dict
import numpy as np
import plotly.graph_objects as go



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
    V_next = Vk.copy()

    # Dictionary to store optimal policy for each state
    policy = dict([(s, 0) for s in list(V_init.keys())])

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



def generate_PIGLET_states(target: int) -> Set:
    '''
    Function to generate states (terminal and non-terminal) of Piglet for a given target score.
    '''

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


def piglet_value_func(target: int) -> Callable:
    '''Function to generate the value update function of Piglet for a given target score.'''

    def bellman_piglet(s, A: Set, P: Callable, R: Callable, V: Dict, target: int = target) -> Dict:
        '''
        Computes the flip and hold values at state s for Piglet.
        
        Arguments
        -----------
        s: state at which we need to update the value.
        A: set of possible actions at the state.
        P: function which calculates the probability of transitioning from state s
            to state s' under action a.
        R: function which calculates the reward obtained when transitioning from 
            state s to state s' under action a.
        target: target score of Piglet game.
        
        Output
        -----------
        values: dictionary containing value at state s if action a is taken for 
                all actions in set A.
        '''

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
                
        return values # return value update for holding and flipping
    
    return bellman_piglet # return the update function for a given target score


def generate_PIG_states(target: int) -> Set:
    '''
    Function to generate states of Pig for a given target score.
    '''

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

def pig_value_func(target: int, die_size: int) -> Callable:
    '''Function to generate the value update function of Piglet for a given target score.'''

    def bellman_PIG(s, A: Set, P: Callable, R: Callable, V: Dict, target: int = target, die_size: int = die_size) -> Dict:
        '''
        Computes the roll and hold values at state s for Pig.
        
        Arguments
        -----------
        s: state at which we need to update the value.
        A: set of possible actions at the state.
        P: function which calculates the probability of transitioning from state s
            to state s' under action a.
        R: function which calculates the reward obtained when transitioning from 
            state s to state s' under action a.
        target: target score of Pig game.
        die_size: number of sides in the die of Pig game.

        Output
        -----------
        values: dictionary containing value at state s if action a is taken for 
                all actions in set A.
        '''

        values = dict((a, 0) for a in A) # value function at s for each action
        i, j, k = s

        if i == "Win": # If at terminal win state, always hold
            values["hold"] = 1
            return values
        
        elif i == "Lose": # If at terminal lose state, always hold, prob of winning is 0
            return values
        
        for a in A: # calculate value for each action at s
            if a == "roll": 
                V_good_roll = [V[(i, j, k+r)] if i + k + r < target 
                               else V[("Win", "Lose", 0)] for r in range(2,7)]  # not rolling a 1
                values[a] = (1 - V[(j, i, 0)] + sum(V_good_roll))/die_size
            elif a == "hold":
                values[a] = 1 - V[(j, i+k, 0)]

        return values # return value update for holding and rolling
    
    return bellman_PIG # return the update function for a given target score


def generate_surface_plot(target: int, set_of_states: Set, figtitle: str = None) -> go.Figure:
    '''
    Function to generate plots of 3D surfaces containing a given set of states.

    Arguments
    -----------
    target: target score of Pig game
    set_of_states: set of states in/below the surface
    figtitle: (Optional) figure title

    Output
    -----------
    fig: Plotly object showing 3D surface.
    '''

    # Define the grid bounds to be 0 to target for all three axes
    grid_x = target
    grid_y = target
    grid_z = target

    # Create a 3D array (grid) of zeros
    value = np.zeros((grid_x, grid_y, grid_z))

    # For all states that should be plotted, give a value of 1
    for (i, j, k) in set_of_states:
        value[i, j, k] = 1

    # Grid indices
    x, y, z = np.indices(value.shape)

    # Plot the 3D isosurface at states with value 1
    fig= go.Figure(data=go.Isosurface(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        value=value.flatten(),
        isomin=0.5,   # nothing less than 1 to be plotted
        isomax=1,
        surface_count=1, # Plot only one surface for simplicity
        colorscale=[(0, 'darkgrey'), (1, 'grey')],  # custom grayscale to match paper's colours
        showscale=False, # remove colorbar

    ))

    # Add axis labels and other formatting such as default aspect
    fig.update_layout(
        scene=dict(
        xaxis=dict(
            title='Player 1 Score (i)',
            backgroundcolor="white",
            gridcolor='lightgrey',
            zeroline=False,
            showline=True,
            linecolor='black',  # Black border
            ticks='outside',    # Show ticks outside the axis
            tickcolor='black'
        ),
        yaxis=dict(
            title='Player 2 Score (j)',
            backgroundcolor="white",
            gridcolor='lightgrey',
            zeroline=False,
            showline=True,
            linecolor='black',  # Black border
            ticks='outside',
            tickcolor='black'
        ),
        zaxis=dict(
            title='Turn Total (k)',
            backgroundcolor="white",
            gridcolor='lightgrey',
            zeroline=False,
            showline=True,
            linecolor='black',  # Black border
            ticks='outside',
            tickcolor='black'
        ),
            aspectmode='cube',  # Ensures the plot is not distorted
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)  # Zoom out to view full 3D plot
            )
        ),
        margin=dict(l=0, r=0, b=0, t=50),  # Set margins
        height=550,      # Plot height
        # width=1000,    # Plot width
        title=figtitle,  # Figure title (if any)
        )  

    return fig 