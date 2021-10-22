import numpy as np
import pandas as pd

df = pd.read_csv("../DATA/salaries.csv")
print(df["Age"] > 30)

print(df)

print(df["Age"].unique())
print(df["Age"].nunique())

print(df.index)

mat = np.arange(60).reshape(10,6)

print(mat)

df = pd.DataFrame(data=mat)
print(df)