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

#Uncomment following lines if you wish to see the bar plot from previous program.
#plt.figure()
#plt.title("Distribution of genders")
#plt.legend(title="0 = Female, 1 = Male")
#fig = sns.countplot(x=df.Gender)
#fig.figure
#plt.show()

# Uncomment following lines if you wish to see averages.
#print("Average of heights in centimeters: " + str(round(st.mean(df.Height),1)) + "cm")
#print("Average of weights in kilograms: " + str(round(st.mean(df.Weight),2)) + "kg")

plt.scatter(df.Weight, df.Height)
m, b = np.polyfit(df.Weight, df.Height, 1)
plt.plot(df.Weight, m*df.Weight + b, color='red')
plt.xlabel("Weight in kilograms")
plt.ylabel("Height in centimeters")
plt.title("Scatter plot & regression line")
plt.show()