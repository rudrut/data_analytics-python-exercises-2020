import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Data = pd.read_csv(r"C:\Users\rudir\Desktop\Koulu\TAMK\Data-Analytiikka\Harkat\BMI_2.csv", sep=';')

# b) Frekvenssitaulukko lihavuusluokituksista
luokitukset = Data['Kuntoluokitus'].values
print(luokitukset)

freq = {}
for item in luokitukset: 
   if (item in freq): 
       freq[item] += 1
   else: 
       freq[item] = 1

for key, value in freq.items(): 
    print("\n", key, ":\t", value)

# c) Pylväskaavio lihavuusluokittain
plt.figure()
plt.title("Lihavuusluokittelu")
#plt.legend(title="0 = Female, 1 = Male")
fig = sns.countplot(y=luokitukset)
fig.figure
plt.show()



