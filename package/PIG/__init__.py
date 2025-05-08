'''
Determines the optimal policy for a problem modelled as a Markov Decision Process (MDP)

Implements the value iteration algorithm to solve a MDP with given set of states and actions,
 transition probabilities, reward function, and discount factor (gamma)

This program is free software: you can redistirbutie it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the license, or (at your option) any other later version.
'''

from .PIG import value_iteration, generate_PIG_states, generate_PIGLET_states, piglet_value_func, pig_value_func

__version__ = "1.0.0"
__author__ = "Niharika Reddy Peddinenikalva"