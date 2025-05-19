# Import packages
from PIG import generate_surface_plot
import numpy as np
import pickle
import plotly.graph_objects as go
from queue import Queue
import matplotlib.pyplot as plt
from typing import Set, Dict, List

# ---------- Load results -------------------
# Load results for value iteration and staged value iteration to plot surfaces
target = 100
die_size = 6
# Direct value iteration results for Pig
results_PIG = pickle.load(open(fr'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'rb'))
# Staged value iteration results for Pig
results_staged_PIG = pickle.load(open(fr'implementation\Results\PIG_staged_results_target_{target}_diesize_{die_size}.pkl', 'rb'))

# Probability of winning from each method
PIG_prob_winning = results_PIG["value_function"]
PIG_staged_prob_winning = results_PIG["value_function"]

# Optimal Policy from each method
PIG_opt_pol = results_PIG["optimal_policy"]
PIG_staged_opt_pol = results_staged_PIG["optimal_policy"]

# Set of roll states from each method
PIG_roll_states = set()
PIG_staged_roll_states = set()

# Add states where rolling is optimal for each method
for (i, j, k), action in PIG_opt_pol.items():
    if action == "roll":
        PIG_roll_states.add((i, j, k))

for (i, j, k), action in PIG_staged_opt_pol.items():
    if action == "roll":
        PIG_staged_roll_states.add((i, j, k))


# ------------ Figure 3: Roll/hold boundary plots ---------------
# Produce figures for roll/hold boundaries using both methods (Figure 3)
PIG_roll_fig = generate_surface_plot(target, set_of_states=PIG_roll_states,
                                     figtitle="Figure 3: 3D plot of roll/hold boundary for optimal Pig play policy")

PIG_staged_roll_fig = generate_surface_plot(target, set_of_states=PIG_staged_roll_states,
                                            figtitle="Figure 3: 3D plot of roll/hold boundary for optimal Pig play policy")
# Save figures
PIG_roll_fig.write_html(fr"implementation\Results\Figures\Roll_boundary_PIG_target_{target}_d{die_size}.html")
PIG_staged_roll_fig.write_html(fr"implementation\Results\Figures\Roll_boundary_staged_PIG_target_{target}_d{die_size}.html")


# ------------ Figure 4, 5, 6: Reachable states plots -----------------
# Find reachable states
def get_reachable_states(target: int, policy: Dict) -> Set:
    '''
    Computes all states that could ever be reached in a game of Pig with a certain target score, using a breadth-first search-like algorithm.
    Player 1 uses a given policy, but Player 2 is free to use any policy.

    Arguments
    -----------
    target: target score of Pig game
    policy: Dictionary containing the policy that Player 1 would use

    Output
    -----------
    visited: Set containing the reachable states
    '''

    qu = Queue(maxsize = 0)
    qu.put((0,0,0)) # Initial queue for BFS
    
    visited = set() # Set of reachable states, initially empty
    
    while not qu.empty(): # while there are states in the queue
        (i, j, k) = qu.get()
        if (i, j, k) not in visited:  # add reachable states if not in set
            visited.add((i, j, k))
            if policy[(i, j, k)] == "hold":  # explore next states if Player 1 holds
                if i + k < target: 
                    qu.put((i+k, j, 0))  # nonwinning reachable state
                    for t in range(2, 100-j):
                        qu.put((i+k, j+t, 0))  # possible states when opponent plays after Player 1 holds
            else:
                for r in range(2,7):  # explore next states if Player 1 rolls
                    if i + k + r < target: 
                        qu.put((i, j, k+r))  # nonwinning reachable state
                for t in range(2, 100-j):
                        qu.put((i, j+t, 0))    # possible states when opponent plays after Player 1 rolls a 1
    
    return visited
 

# Reachable states for each method
PIG_reachable_states = get_reachable_states(target, PIG_opt_pol)
PIG_staged_reachable_states = get_reachable_states(target, PIG_staged_opt_pol)


# Produce figures for reachable states for each method
PIG_reachable_fig = generate_surface_plot(target, set_of_states=PIG_reachable_states,
                                     figtitle="Figure 5: 3D plot of reachable states by an optimal Pig player")

PIG_staged_reachable_fig = generate_surface_plot(target, set_of_states=PIG_staged_reachable_states,
                                            figtitle="Figure 5: 3D plot of reachable states by an optimal Pig player")
# Save figures
PIG_reachable_fig.write_html(fr"implementation\Results\Figures\Reachable_states_PIG_target_{target}_d{die_size}.html")
PIG_staged_reachable_fig.write_html(fr"implementation\Results\Figures\Reachable_states_staged_PIG_target_{target}_d{die_size}.html")



## ------ Cross-section of reachable states (Figure 4)
def plot_reachable_states_cross_section(target: int, policy: Dict, reachable_states: Set, opponent_score: int = 30):
    '''
    Function to plot cross-section of roll/hold boundary including reachable region, at a given opponent's score (Figure 4).

    Arguments
    -----------
    target: target score of Pig game
    policy: Dictionary containing the policy that Player 1 would use
    reachable_states: Set containing reachable states in the Pig game
    opponent_score: score of Player 2 at which to perform cross-section

    Output
    -----------
    fig: plt object of cross-section of roll/hold boundary
    '''
    
    # Filter the reachable states for j = opponent score
    reachable = set([(i, k) for (i, j, k) in reachable_states if j == opponent_score])
    # reachable_set = set(reachable)
    
    # Determine optimal boundary between points (i, k) where the player should roll or hold, as per policy
    hold_points = []
    
    for i in range(target):
        for k in range(target):
            if i + k < target and policy[(i, opponent_score, k)] == 'roll' and ((i + k + 1 == target or policy[(i, opponent_score, k+1)] == 'hold') or (i > 0 and policy[(i - 1, opponent_score, k)] == 'hold')):  
                hold_points.append((i, k))
    
    # Split for plotting
    hold_i = [i for (i, k) in hold_points]
    hold_k = [k for (i, k) in hold_points]
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot shaded reachable region
    for i in range(101):
        ks = [k for (ii, k) in reachable if ii == i]
        if ks:
            ax.fill_between([i - 0.5, i + 0.5], min(ks), max(ks), color='lightgrey', step='mid', alpha=0.7)
    
    # Plot optimal boundary
    ax.scatter(hold_i, hold_k, color='black', s=2, label='Optimal Boundary')

    
    # Plot hold-at-20 reference line
    ax.axhline(20, color='gray', linestyle='--', label='Hold at 20')
    
    # Labels and limits
    ax.set_xlabel('Player 1 Score (i)')
    ax.set_ylabel('Turn Total (k)')
    ax.set_title(fr"Figure 4: Cross-section of the roll/hold boundary, opponent's score = {opponent_score}")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.legend()
    ax.grid(False)
    
    # Return the figure object
    return fig

# Cross-section plots for both methods where opponent score = 30
cross_sec_PIG_fig = plot_reachable_states_cross_section(target, policy=PIG_opt_pol, 
                                    reachable_states=PIG_reachable_states)
plt.savefig(fr"implementation\Results\Figures\cross_sec_reachable_PIG_target_{target}_d{die_size}.png", dpi=300)
plt.close(cross_sec_PIG_fig)

cross_sec_staged_PIG_fig = plot_reachable_states_cross_section(target, policy=PIG_opt_pol, 
                                    reachable_states=PIG_staged_reachable_states)
plt.savefig(fr"implementation\Results\Figures\cross_sec_reachable_staged_PIG_target_{target}_d{die_size}.png", dpi=300)
plt.close(cross_sec_staged_PIG_fig)

# ---------- Figure 7: Contour plots for win probabilities ------------
def plot_win_prob_contours(target: int, prob_winning: Dict, target_probs: List, tolerances: List, colour_list: List):
    '''
    Function to generate win probability contours for a list of given target probabilities, tolerances and colour palettes (Figure 7).

    Arguments
    -----------
    target: target score of Pig game
    prob_winning: Dictionary of win probabilities resulting from optimal play policy and value iteration
    target_probs: List of probabilities for which to plot the contour
    tolerances: List of tolerances, where for n-th target probability t_n, n-th tolerance tol_n implies the contour contains states with win probability [t_n - tol_n, t_n + tol_n]
    colour_list: List of colour palettes, such that each consecutive pair forms a colour scale for each contour.

    Output
    -----------
    fig: Plotly object showing win probability isosurfaces.
    '''

    P = np.ones((target, target, target))
    
    for (i, j, k), value in prob_winning.items():
        if (i, j, k) not in [("Win","Lose",0), ("Lose", "Win", 0)]: # and cont - tolerance <= prob_winning[(i,j,k)] and cont + tolerance >= prob_winning[(i,j,k)]:
            P[i, j, k] = value
    
    x, y, z = np.meshgrid(
        np.arange(P.shape[0]),
        np.arange(P.shape[1]),
        np.arange(P.shape[2]),
        indexing='ij'
    )
    
    isosurfaces = []

    for i in range(len(target_probs)):
        isosurfaces.append(go.Isosurface(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            value=P.flatten(),
            isomin=target_probs[i] - tolerances[i],
            isomax=target_probs[i] + tolerances[i],
            surface_count=1,
            caps=dict(x_show=False, y_show=False, z_show=False),
            showscale=False,
            colorscale=[(0, colour_list[i]), (1, colour_list[i+1])],
            name = fr"{target_probs[i]*100}%"
        ))

    fig = go.Figure(data=isosurfaces)

    fig.update_layout(
        scene=dict(
            xaxis_title="Own Score",
            yaxis_title="Opponent Score",
            zaxis_title="Turn Total"
        ),
        title="Figure 7: Win Probability Contours",
        margin=dict(l=0, r=0, b=0, t=50),   # Set margins
        height=550,                         # Plot height
        showlegend=True,
    )

    return fig

target_probs = [0.03, 0.09, 0.27, 0.81]    # win probabilities for contours
tolerances = [0.001, 0.002, 0.003, 0.004]
colour_list = ['white', 'lightgrey', 'grey', 'darkgrey', 'black']   # list of colour palettes

# Contour plots for each method to be saved
contour_PIG_fig = plot_win_prob_contours(target, PIG_prob_winning, target_probs, tolerances, colour_list)
contour_PIG_fig.write_html(fr"implementation\Results\Figures\contours_PIG_target_{target}_d{die_size}.html")

contour_staged_PIG_fig = plot_win_prob_contours(target, PIG_staged_prob_winning, target_probs, tolerances, colour_list)
contour_staged_PIG_fig.write_html(fr"implementation\Results\Figures\contours_staged_PIG_target_{target}_d{die_size}.html")
