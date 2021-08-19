import random as rand
import numpy as np

# a)
entries = int(input("How many random numbers? "))

# b)
randomMin = int(input("Determine minimum: "))
randomMax = int(input("Determine maximum: "))

amountOfRandoms = np.full(entries, 0)

# c)
for i in range(0, amountOfRandoms.size):
    amountOfRandoms[i] = rand.randrange(randomMin, randomMax)

sorted_array = np.sort(amountOfRandoms)

reverse_array = sorted_array[::-1]

# d)
print("Numbers in ascending order: " + str(sorted_array)) 

# e)
print("Numbers in descending order: " + str(reverse_array)) 