# 🌍 Global Happiness Report Analysis

## 📌 Project Overview

The **Global Happiness Report Analysis** is a Python-based data analysis and visualization project that explores happiness scores across countries using the World Happiness Report 2025 dataset.

The project uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn to clean, analyze, summarize, and visualize the dataset. It examines the relationship between happiness scores and important factors such as GDP per capita, social support, healthy life expectancy, and freedom to make life choices.

## 🎯 Project Objectives

- Analyze happiness scores across different countries.
- Identify the happiest and least happy countries in the dataset.
- Calculate the average happiness score and statistical summaries.
- Study correlations between happiness scores and contributing factors.
- Visualize country rankings and relationships using charts.
- Understand patterns and trends in global happiness data.

## 📂 Dataset Information

**Dataset:** World Happiness Report 2025

The dataset includes country-level happiness scores and several explanatory factors.

Important columns used in this project:

- `Country name`
- `Ladder score`
- `upperwhisker`
- `lowerwhisker`
- `Explained by: Log GDP per capita`
- `Explained by: Social support`
- `Explained by: Healthy life expectancy`
- `Explained by: Freedom to make life choices`
- `Explained by: Generosity`
- `Explained by: Perceptions of corruption`
- `Dystopia + residual`

The dataset is stored in CSV format and loaded into Python using Pandas.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data loading, cleaning, and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical charts and heatmaps |
| CSV | Dataset storage |

## ✨ Project Features

### 1. Data Loading

- Loads the happiness dataset from a CSV file.
- Displays the dataset columns and structure.

### 2. Data Cleaning

- Removes duplicate records.
- Handles missing values in numeric columns using mean values.
- Converts happiness scores to numeric format where necessary.

### 3. Exploratory Data Analysis (EDA)

- Displays the top 10 happiest countries.
- Displays the bottom 10 countries by happiness score.
- Calculates the average happiness score.
- Identifies the country with the highest and lowest happiness scores.
- Generates descriptive statistical summaries.

### 4. Correlation Analysis

- Calculates correlations between happiness scores and selected explanatory factors.
- Examines relationships between GDP per capita, social support, healthy life expectancy, freedom, and happiness.

### 5. Data Visualization

The project generates the following visualizations:

- **Bar Chart:** Top 10 Happiest Countries
- **Scatter Plot:** GDP per Capita vs. Happiness Score
- **Box Plot:** Distribution of Happiness Scores
- **Correlation Heatmap:** Relationships among numeric variables

## 📊 Visualizations

### Top 10 Happiest Countries

Displays the 10 countries with the highest happiness scores.

### GDP vs Happiness

Shows the relationship between GDP per capita and happiness scores across countries.

### Happiness Score Distribution

Uses a box plot to summarize the distribution of happiness scores and highlight potential outliers.

### Correlation Heatmap

Displays correlation coefficients between numeric variables to help identify positive and negative relationships.

## 📸 Output Screenshot

### 1. Output 1
![Output 1](screenshot/output.1.png)

### 2. Output 2
![Output 2](screenshot/output.2.png)

### 3. Output 3
![Output 3](screenshot/output.3.png)

### 4. Output 4
![Output 4](screenshot/output.4.png)

## 📁 Project Structure

```text
Final Project/
│
├── WHR_2025.csv
├── analysis.py
├── data_cleaning.py
├── eda.py
├── visualizations.py
├── README.md
│
screenshot/
    ├── output.1.png
    ├── output.2.png
    ├── output.3.png
    └── output.4.png
