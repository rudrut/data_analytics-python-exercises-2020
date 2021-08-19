import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
from scipy import stats
from sklearn.linear_model import LinearRegression

Data = pd.read_csv(r"C:\Users\rudir\Desktop\Koulu\TAMK\Data-Analytiikka\Harkat\BMI.csv")

# a) Korrelaatiomatriisi
df = pd.DataFrame(Data)
corrMatrix = df.corr()
print("Korrelaatiomatriisi: ")
print(corrMatrix)

# b) Regressioanalyysi

# Initializing two new arrays because reshape() method demands it.
pituudet = Data['Pituus'].values
painot = Data['Paino'].values


x = pituudet
x = x.reshape(-1, 1)

y = painot
y = y.reshape(-1, 1)

# Initializing model for linear regression
model = LinearRegression()
model.fit(x,y)

# Predicted value
y_pred = model.predict(x)

# Determination coefficient
r_square = model.score(x,y)

# Creating a tuple to store Pearson correlation coefficient and p-value AKA sig.
pearson_info = stats.pearsonr(pituudet, painot)
p_corr_coeff = pearson_info[0]
p_sig = pearson_info[1]

print()

print("Regressioanalyysin tulokset:")
print("Coefficient of determination, R-square is ", r_square)

print("Intercept, constant is: ", float(model.intercept_))
print("Slope, coefficient is: ", float(model.coef_))
print("Sig. is: ", p_sig)

plt.plot(x, y, 'ro', markerfacecolor = "lightblue", label = "Observed Values")
plt.plot(x, y_pred, 'g-', linewidth = 2, label = "Regression Line")
plt.title("Regression analysis: Heights & Weights")
plt.show()