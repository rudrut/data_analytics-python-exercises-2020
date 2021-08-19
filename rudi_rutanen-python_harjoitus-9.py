import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# .csv-tiedoston lukeminen
Data = pd.read_csv(r"C:\Users\rudir\Desktop\Koulu\TAMK\Data-Analytiikka\Harkat\Deca.csv")

# Muuttujien alustaminen
yhteispisteet = Data['pisteet'].values
pituushyppy = Data['pituus'].values
kuula = Data['kuula'].values
kiekko = Data['kiekko'].values

# a) Korrelaatiomatriisi em. muuttujista
df = pd.DataFrame(Data, columns=["pisteet", "pituus", "kuula", "kiekko"])
corrMatrix = df.corr()
print(corrMatrix)

# b) Pisteparvi ja trendiviiva pituushypystä ja yhteispisteistä

plt.scatter(df.pisteet, df.pituus)
m, b = np.polyfit(df.pisteet, df.pituus, 1)
plt.plot(df.pisteet, m*df.pisteet + b, color='red')
plt.xlabel("Yhteispisteet")
plt.ylabel("Pituushypyn pisteet")
plt.title("Pisteparvi ja trendiviiva")
plt.show()