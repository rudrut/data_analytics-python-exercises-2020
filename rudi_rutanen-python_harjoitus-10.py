# All variables are converted to centimeters!
import numpy as np
import pandas as pd

male_netherlands_mean_height =  183.3
male_netherlands_SD = 7.1

female_netherlands_mean_height = 170.7
female_netherlands_SD = 6.3

n = 1000

#Initializing arrays
maleHeightArray = np.round_(np.random.normal(male_netherlands_mean_height, male_netherlands_SD, n),decimals=1)
femaleHeightArray = np.round_(np.random.normal(female_netherlands_mean_height, female_netherlands_SD, n),decimals=1)

Data = {
    "maleHeight" : maleHeightArray,
    "femaleHeight" : femaleHeightArray
}

#Initializing DataFrame
netherlandsHeightDistribution = pd.DataFrame(data = Data)

#Change path as necessary when saving
netherlandsHeightDistribution.to_csv(r"C:\Users\rudir\Desktop\Koulu\TAMK\Data-Analytiikka\Harkat\netherlandsHeightDistribution.csv")

print("file saved!")

