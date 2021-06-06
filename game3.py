# !pip install nashpy

# Matching pennies using nashpy and numpy

import nashpy as nash
import numpy as np

Alice = np.array([[1, -1], [-1, 1]])
Bob = np.array([[-1, 1], [1, -1]])

missing_pennies= nash.Game(Alice, Bob)
print(missing_pennies)

#calculate utilities
Alice_sigma = np.array([1, 0])
Bob_sigma = np.array([1, 0])
print(missing_pennies[Alice_sigma, Bob_sigma])

# Calculate Nash equilibrium
for eq in missing_pennies.support_enumeration():
  print(eq)
