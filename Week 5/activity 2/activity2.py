"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""

import numpy as np
arr = np.zeros(100)
print(arr)
arr = np.random.rand(100)
print(arr)