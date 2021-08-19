import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st
from scipy import stats
from sklearn.linear_model import LinearRegression

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

# Uncomment following lines if you wish to see a scatter plot and regression line from previous program.
#plt.scatter(df.Weight, df.Height)
#m, b = np.polyfit(df.Weight, df.Height, 1)
#plt.plot(df.Weight, m*df.Weight + b, color='red')
#plt.xlabel("Weight in kilograms")
#plt.ylabel("Height in centimeters")
#plt.title("Scatter plot & regression line")
#plt.show()

# a) A correlation matrix of heights and weights
df_2 = pd.DataFrame(data, columns=["Height", "Weight"])
corrMatrix = df_2.corr()
print(corrMatrix)

# b) Regression analysis from here to EOF (End-Of-File)

# Initializing two new arrays because reshape() method demands it.
x = heightArray
x = x.reshape(-1,1)

y = weightArray
y = y.reshape(-1,1)

# Initializing model for linear regression
model = LinearRegression()
model.fit(x, y)

# Predicted value
y_pred = model.predict(x)

# Determination coefficient
r_square = model.score(x, y)
print()

# Creating a tuple to store Pearson correlation coefficient and p-value AKA sig.
pearson_info = stats.pearsonr(heightArray, weightArray)
p_corr_coeff = pearson_info[0]
p_sig = pearson_info[1]

print("Coefficient of determination, R-square is ", r_square)

print("Intercept, constant is: ", float(model.intercept_))
print("Slope, coefficient is: ", float(model.coef_))
print("Sig. is: ", p_sig)

plt.plot(x, y, 'ro', markerfacecolor = "lightblue", label = "Observed Values")
plt.plot(x, y_pred, 'g-', linewidth = 2, label = "Regression Line")
plt.xlabel("Height in centimeters")
plt.ylabel("Weight in kilograms")
plt.title("Regression analysis: Heights & Weights")
plt.show()
