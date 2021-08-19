import random as rand
import numpy as np

my_array = np.full(12, 0)

for i in range(my_array.size):
    my_array[i] = rand.randint(51,101)

# a)
print("A NumPy array of 12 integers in ascending order: " + str(np.sort(my_array)))

# b)
print("A NumPy array of 12 integers in descending order: " + str(np.sort(my_array)[::-1]))

# c)
print("The average of integers in NumPy array: " + str(np.average(my_array)))
print("The median of integers in NumPy array: " + str(np.median(my_array)))