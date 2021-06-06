# !pip install nashpy 

#Rock-paper-scissors game using nashpy and numpy

import nashpy as nash
import numpy as np

Alice = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
Bob = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])

rock_paper_scissors = nash.Game(Alice, Bob)
print(rock_paper_scissors)

#calculate utilities
Alice_sigma = np.array([0, 0, 1])
Bob_sigma = np.array([0, 1, 0])

#calculate Nash equilibrium
for eq in rock_paper_scissors.support_enumeration():
  print(eq)
