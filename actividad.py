# %%
import numpy as np
import pandas as pd
import seaborn 
import matplotlib.pyplot as plt

df = pd.read_csv("ulabox.csv")

# printing data frame
# print(df)

# printing min values
# print("Rango inferior\n")
# print(df.min())

# printing max values
# print("Rango superior\n")
# print(df.max())

print(df.describe())


# %% 
# Realizar gráfico de caja
plt.figure(figsize=(10, 4))
seaborn.boxplot(x="total_items",
                data=df,
                showmeans=True,
                meanprops={"marker":"o",
                       "markerfacecolor":"white", 
                       "markeredgecolor":"black",
                      "markersize":"10"})
# %%
