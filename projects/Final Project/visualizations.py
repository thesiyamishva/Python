import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\Python\projects\Final Project\WHR_2025.csv", encoding="latin1")

top10 = df.nlargest(10, 'Ladder score')
plt.figure(figsize=(10,6))
sns.barplot(x='Ladder score', y='Country name', data=top10, palette='viridis')
plt.title("Top 10 Happiest Countries")
plt.xlabel("Happiness Score")
plt.ylabel("Country")
plt.show()

plt.figure(figsize=(10,8))
sns.scatterplot(
    x='Explained by: Log GDP per capita',
    y='Ladder score',
    data=df,
    hue='Country name',   
    palette='Set2'
)
plt.title("GDP vs Happiness by Country")
plt.xlabel("Log GDP per Capita")
plt.ylabel("Happiness Score")
plt.legend(
    bbox_to_anchor=(1, 1),   
    loc='upper left',          
    borderaxespad=0
)
plt.show()


plt.figure(figsize=(6,6))
sns.boxplot(y='Ladder score', data=df)
plt.title("Distribution of Happiness Scores")
plt.ylabel("Happiness Score")
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Happiness Factors")
plt.show()
