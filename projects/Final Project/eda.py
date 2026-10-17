import pandas as pd

df = pd.read_csv(r"D:\Python\projects\Final Project\WHR_2025.csv", encoding="latin1")

print("Top 10 Happiest Countries:")
print(df[['Country name','Ladder score']].head(10))

print("\nBottom 10 Countries:")
print(df[['Country name','Ladder score']].tail(10))

avg_score = df['Ladder score'].mean()
print("\nAverage Happiness Score:", avg_score)

max_country = df.loc[df['Ladder score'].idxmax()]
min_country = df.loc[df['Ladder score'].idxmin()]
print("\nHighest:", max_country['Country name'], max_country['Ladder score'])
print("Lowest:", min_country['Country name'], min_country['Ladder score'])

print("\nStatistical Summary:")
print(df['Ladder score'].describe())
