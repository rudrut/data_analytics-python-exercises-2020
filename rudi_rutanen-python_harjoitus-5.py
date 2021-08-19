import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st

n = 10 # Amount of entries in each column.

# Initializing arrays with random values in given ranges
genderArray = np.random.randint(0, 2, n)
heightArray = np.round_(np.random.uniform(140,210, n), 1)
weightArray = np.round_(np.random.uniform(45,150, n), 1)

# Creating a dictionary 'data' of which keys are column names and values are NumPy arrays of numbers.
data = {
    "Gender": genderArray,
    "Height": heightArray,
    "Weight": weightArray
}

# Creating a dataframe based on earlier variable 'data'.
df = pd.DataFrame(data, columns=["Gender", "Height", "Weight"])

# Uncomment following line if you want to see dataframe values.
# print(df)

# a)
plt.figure()
plt.title("Distribution of genders")
plt.legend(title="0 = Female, 1 = Male")
fig = sns.countplot(x=df.Gender)
fig.figure
plt.show()

# b)
print("Average of heights in centimeters: " + str(round(st.mean(df.Height),1)) + "cm")

# c)
print("Average of weights in kilograms: " + str(round(st.mean(df.Weight),2)) + "kg")