import numpy as np
import random as rand

# a)
tas = np.random.rand()
print("A random float number from a uniform distribution 'tas' between 0 and 1: " + str(tas))

# b)
tasd = np.full(20, 0)

for i in range(tasd.size):
    tasd[i] = np.random.randint(101,201)

print("A NumPy array of 20 random integers from discrete distribution 'tasd' between 101 and 200: " + str(tasd))

# c)
c = rand.normalvariate(178,30)
print("A random float number from normal distribution 'c': " + str(c))

# d)
d = np.full(15,0)

for i in range(d.size):
    d[i] = rand.normalvariate(166,28)

print("A NumPy array of 15 random numbers from normal distribution 'd': " + str(d))