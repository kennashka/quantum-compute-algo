#!pip install nashpy


#Prisoner's dilemma using nashpy and numpy

import nashpy as nash
import numpy as np

Alice = np.array([[3, 1], [4, 2]])
Bob = np.array([[3, 4], [1, 2]])

prisoner_dilemma = nash.Game(Alice, Bob)
print(prisoner_dilemma)


#calculate utilities
Alice_sigma = np.array([1, 0])
Bob_sigma = np.array([1, 0])
print(prisoner_dilemma[Alice_sigma, Bob_sigma])

# Calculate Nash equilibrium
for eq in prisoner_dilemma.support_enumeration():
  print(eq)
