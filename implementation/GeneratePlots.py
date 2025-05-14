# Import packages
from PIG import value_iteration, pig_value_func, piglet_value_func, generate_PIG_states, generate_PIGLET_states, generate_surface_plot
import numpy as np
import pickle
import plotly.graph_objects as go
from queue import Queue
import matplotlib.pyplot as plt

# ---------- Load results -------------------
# Load results for value iteration and staged value iteration to plot surfaces
target = 100
die_size = 6
results_PIG = pickle.load(open(f'implementation\Results\PIG_results_target_{target}_diesize_{die_size}.pkl', 'rb'))
results_staged_PIG = pickle.load(open(f'implementation\Results\PIG_staged_results_target_{target}_diesize_{die_size}.pkl', 'rb'))

# Probability of winning from each method
PIG_prob_winning = results_PIG["value_function"]
PIG_staged_prob_winning = results_PIG["value_function"]

# Optimal Policy from each method
PIG_opt_pol = results_PIG["optimal_policy"]
PIG_staged_opt_pol = results_staged_PIG["optimal_policy"]

# Set of roll states from each method
PIG_roll_states = set()
PIG_staged_roll_states = set()

# Add roll states
for (i, j, k), action in PIG_opt_pol.items():
    if action == "roll":
        PIG_roll_states.add((i, j, k))

for (i, j, k), action in PIG_staged_opt_pol.items():
    if action == "roll":
        PIG_staged_roll_states.add((i, j, k))


# ------------ Roll/hold boundary plots ---------------
# Produce figures for roll/hold boundaries using both methods
PIG_roll_fig = generate_surface_plot(target, set_of_states=PIG_roll_states,
                                     figtitle="3D plot of roll/hold boundary for optimal Pig play policy")

PIG_staged_roll_fig = generate_surface_plot(target, set_of_states=PIG_staged_roll_states,
                                            figtitle="3D plot of roll/hold boundary for optimal Pig play policy")
# Save figures
PIG_roll_fig.write_html(f"implementation\Results\Figures\Roll_boundary_PIG_target_{target}_d{die_size}.html")
PIG_staged_roll_fig.write_html(f"implementation\Results\Figures\Roll_boundary_staged_PIG_target_{target}_d{die_size}.html")


# ------------ Reachable states plots -----------------
# Find reachable states
def get_reachable_states(target, policy):
    qu = Queue(maxsize = 0)
    qu.put((0,0,0)) # Initial queue for BFS
    
    visited = set() # Set of reachable states
    
    while not qu.empty(): # while there are states in the queue
        (i, j, k) = qu.get()
        if (i, j, k) not in visited:  # add reachable states if not in set
            visited.add((i, j, k))
            if policy[(i, j, k)] == "hold":  # reachable states if player holds
                if i + k < target: 
                    qu.put((i+k, j, 0))  # non winning reachable state
                    for t in range(2, 100-j):
                        qu.put((i+k, j+t, 0))  # possible states when opponent plays after player holds
            else:
                for r in range(2,7):  # reachable state if we roll
                    if i + k + r < target: 
                        qu.put((i, j, k+r))  # nonwinning reachable state
                for t in range(2, 100-j):
                        qu.put((i, j+t, 0))    # possible states when opponent plays after player holds
    
    return visited
 

# Reachable states
PIG_reachable_states = get_reachable_states(target, PIG_opt_pol)
PIG_staged_reachable_states = get_reachable_states(target, PIG_staged_opt_pol)


# Produce figures for reachable states
PIG_reachable_fig = generate_surface_plot(target, set_of_states=PIG_reachable_states,
                                     figtitle="3D plot of reachable states by an optimal Pig player")

PIG_staged_reachable_fig = generate_surface_plot(target, set_of_states=PIG_staged_reachable_states,
                                            figtitle="3D plot of reachable states by an optimal Pig player")
# Save figures
PIG_reachable_fig.write_html(f"implementation\Results\Figures\Reachable_states_PIG_target_{target}_d{die_size}.html")
PIG_staged_reachable_fig.write_html(f"implementation\Results\Figures\Reachable_states_staged_PIG_target_{target}_d{die_size}.html")



## ------ Cross-section of reachable states (Figure 4)
def plot_reachable_states_cross_section(target, policy, reachable_states, opponent_score=30):
    
    # Filter the reachable states for j = opponent score
    reachable = set([(i, k) for (i, j, k) in reachable_states if j == opponent_score])
    # reachable_set = set(reachable)
    
    # Determine optimal boundary: points (i, k) where the player should hold
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
    
    # Plot shaded reachable area
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
    ax.set_title(f"Cross-section of the roll/hold boundary, opponent's score = {opponent_score}")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.legend()
    ax.grid(False)
    
    # Return the figure object
    return fig

# Cross-section plots for both methods where opponent score = 30
cross_sec_PIG_fig = plot_reachable_states_cross_section(target, policy=PIG_opt_pol, 
                                    reachable_states=PIG_reachable_states)
plt.savefig(f"implementation\Results\Figures\cross_sec_reachable_PIG_target_{target}_d{die_size}.png", dpi=300)

cross_sec_staged_PIG_fig = plot_reachable_states_cross_section(target, policy=PIG_opt_pol, 
                                    reachable_states=PIG_staged_reachable_states)
plt.savefig(f"implementation\Results\Figures\cross_sec_reachable_staged_PIG_target_{target}_d{die_size}.png", dpi=300)


# ---------- Contour plots for win probabilities ------------
def plot_win_prob_contours(target, prob_winning, target_probs = [0.03, 0.09, 0.27, 0.81]):
    P = np.zeros((target, target, target))
    
    for (i, j, k), value in prob_winning.items():
        if (i, j, k) not in [("Win","Lose",0), ("Lose", "Win", 0)]: # and cont - tolerance <= prob_winning[(i,j,k)] and cont + tolerance >= prob_winning[(i,j,k)]:
            P[i, j, k] = value
    
    x, y, z = np.meshgrid(
        np.arange(P.shape[0]),
        np.arange(P.shape[1]),
        np.arange(P.shape[2]),
        indexing='ij'
    )

    tolerances = [0.002, 0.005, 0.01, 0.02]  # controls the sharpness
    
    # Start with an all-False mask
    mask = np.full(P.shape, False)
    
    # Combine all target masks
    for (t, tol) in list(zip(target_probs,tolerances)):
        mask |= np.abs(P - t) < tol
    
    # Create volume render
    fig = go.Figure(data=go.Volume(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        value=mask.flatten(),
        opacity=1,  # Low opacity
        surface_count=1,
        isomin=0.5,
        isomax=1.0,
    ))
    
    fig.update_layout(
        scene=dict(
            xaxis_title="Own Score",
            yaxis_title="Opponent Score",
            zaxis_title="Turn Total"
        ),
        title="Win Probability Regions (Volume Mask)"
    )

    return fig

contour_PIG_fig = plot_win_prob_contours(target, PIG_prob_winning)
contour_PIG_fig.write_html(f"implementation\Results\Figures\contours_PIG_target_{target}_d{die_size}.html")

contour_staged_PIG_fig = plot_win_prob_contours(target, PIG_staged_prob_winning)
contour_staged_PIG_fig.write_html(f"implementation\Results\Figures\contours_staged_PIG_target_{target}_d{die_size}.html")
