# !pip install nashpy

# Battle of sexes using nashpy and numpy

import nashpy as nash
import numpy as np

Alice = np.array([[2, 1], [1, 2]])
Bob = np.array([[3, 1], [1, 3]])

battle_sexes= nash.Game(Alice, Bob)
print(battle_sexes)

#calculate utilities
Alice_sigma = np.array([1, 0])
Bob_sigma = np.array([1, 0])
print(battle_sexes[Alice_sigma, Bob_sigma])

# Calculate Nash equilibrium
for eq in battle_sexes.support_enumeration():
  print(eq)
