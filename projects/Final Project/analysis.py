import pandas as pd

df = pd.read_csv(r"D:\Python\projects\Final Project\WHR_2025.csv", encoding="latin1")

corr = df[['Ladder score',
           'Explained by: Log GDP per capita',
           'Explained by: Social support',
           'Explained by: Healthy life expectancy',
           'Explained by: Freedom to make life choices']].corr()

print("Correlation Matrix:")
print(corr)
print(df.columns)
