# `PIG`
- [**A Python package for optimal play of the game of Pig**](#)
- [Installation](#installation)
- [License](#license)
- [GitHub Repository](#github-repository)
    - [Outline of Repository](#outline-of-repository)
- [Authors](#authors)
- [References](#references)


## A Python package implementing value iteration for the game of Pig

This package implements a value iteration algorithm to create an optimal policy for playing the game Pig, and contains functions for reproducing results from (Neller and Presser, 2024).

## Installation

#### Install from GitHub with pip
    python -m pip install "git+https://github.com/turtlesoul25/STOR609_Assessment3_Group3#subdirectory=package"


## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.txt>.


## GitHub Repository

This is an open source public repository at the following site <https://github.com/turtlesoul25/STOR609_Assessment3_Group3>

### Outline of Repository
#### Report.ipynb
This Jupyter notebook is a report on our findings from a replication exercise of Neller and Presser (2004) to find an optimal policy for playing Pig and Piglet.

#### package
The package folder contains the Python package PIG which contains functions to help set up the games Pig and Piglet, a function for a general value iteration implementation and a plotting function to help generate 3D surface plots such as Figures 3, 5, and 6 in Neller and Presser (2004).

#### implementation
The implementation folder contains:
- `SolvingPiglet.py`: Implementation of value iteration to solve Piglet
- `SolvingPig.py`: Implementation of direct value iteration to solve Pig
- `SolvingPigStaged.oy`: Implementation of staged value iteration to solve Pig
- `GeneratePlots.py`: Python script which generates all Figures (3-7) for Pig results
- `PIGCompetitionSetup.py`: Python script containing code to set up player strategies (optimal and hold at $n$), Pig competition simulation, and Pig tournament simulation.
- `optimal_vs_optimal.py`: Implementation of a tournament of 100,000 trials of Pig between two optimal players.
- `opt_hold_n.py`: Implementation of tournaments of 100,000 trials of Pig between an optimal player and a hold at $n$ player for $n \in \{20, 21, 22, 23}$ with a tournament each where optimal player, hold at $n$ player and a random player plays first.
- `Results`: The results folder contains 
    - .pkl files: for results of probability of winning and optimal policy at each state for Piglet and Pig (via direct and staged value iteration).
    - .npy files: a file `p1_vs_p2_nrounds_seed123.npy` for results from each tournament of `nrounds` of the Pig competition between $p_1$ and $p_2$ where $p_1$ plays first and a seed `123` is set at the start of the round. For files `p1_r_p2_nrounds_seed123.npy`, the first player is chosen randomly using a fair coin.
    - `Figures`: Plots replicating Figures 2-7 in Neller and Presser (2004).
        - Figure 2: Piglet_convergence.png
        - Figure 3: .html files with file name beginning `Roll_boundary`
        - Figure 4: .png files with file name beginning `cross_sec_reachable` 
        - Figure 5, 6: .html files beginning `Reachable_states`
        - Figure 7: .html files beginning `contours`
        - CI plots (not in paper): .png files with file name beginning `CI_plot` - plots to compare $\%$ wins for player 1 when player 1 is optimal or otherwise for different opponent strategies


## Authors

Group 3: Vlad Bercovici, Malcolm Connolly, Rebekah Fearnhead, Niharika Peddinenikalva

- Vlad Bercovici: [email](mailto:v.bercovici@lancaster.ac.uk) (**Author**)
- Malcolm Connolly: [email](mailto:m.connolly4@lancaster.ac.uk) (**Author**)
- Rebekah Fearnhead: [email](mailto:r.fearnhead1@lancaster.ac.uk) (**Author**)
- Niharika Peddinenikalva: [email](mailto:n.peddinenikalva@lancaster.ac.uk) (**Author**)


## References
Neller, Todd W. and Clifton G.M. Presser. (2004) "Optimal Play of the Dice Game Pig," The UMAP Journal 25.1 , 25-47.

