import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Python\projects\Final Project\WHR_2025.csv", encoding="latin1")

df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)
df['Ladder score'] = df['Ladder score'].astype(float)

print(df.info())
print(df.describe())
