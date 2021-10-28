# %%
import numpy as np
import pandas as pd

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
