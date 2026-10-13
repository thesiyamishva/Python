import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        print("Cleaning up resources...")

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    def explore_data(self):
        if self.data is not None:
            print(self.data.head())
            print(self.data.info())
            print(self.data.describe())
        else:
            print("No data loaded.")

    def clean_data(self):
        if self.data is not None:
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            self.data.dropna(inplace=True)
            print("Data cleaned successfully!")
        else:
            print("No data to clean.")

    def mathematical_operations(self):
        if self.data is not None:
            print("Total Sales:", self.data['Sales'].sum())
            print("Average Sales:", self.data['Sales'].mean())
        else:
            print("No data available.")

    def combine_data(self, other_dataframe):
        if self.data is not None:
            self.data = pd.concat([self.data, other_dataframe], ignore_index=True)
            print("Data combined successfully!")
        else:
            print("No base data to combine with.")

    def split_data(self, column='Region'):
        if self.data is not None and column in self.data.columns:
            groups = dict(tuple(self.data.groupby(column)))
            return groups
        else:
            print("Column not found or no data.")
            return None

    def search_sort_filter(self):
        if self.data is not None:
            print("Filtered Data (Sales > 600):")
            print(self.data[self.data['Sales'] > 600])
            print("\nSorted Data by Profit:")
            if 'Profit' in self.data.columns:
                print(self.data.sort_values(by='Profit', ascending=False))
        else:
            print("No data available.")

    def aggregate_functions(self):
        if self.data is not None:
            print(self.data.agg({'Sales': ['sum', 'mean', 'max']}))
        else:
            print("No data available.")

    def statistical_analysis(self):
        if self.data is not None:
            print("Standard Deviation:", self.data['Sales'].std())
            print("Variance:", self.data['Sales'].var())
            print("Quantiles:", self.data['Sales'].quantile([0.25, 0.5, 0.75]))
        else:
            print("No data available.")

    def create_pivot_table(self):
        if self.data is not None:
            pivot = pd.pivot_table(self.data, values='Sales', index='Region', columns='Product', aggfunc='sum')
            print(pivot)
        else:
            print("No data available.")

    def visualize_data(self):
        if self.data is not None:
            plt.figure(figsize=(10,6))
            sns.barplot(x='Product', y='Sales', data=self.data)
            plt.title("Sales by Product")
            plt.show()

            plt.figure(figsize=(10,6))
            sns.lineplot(x='Year', y='Sales', data=self.data)
            plt.title("Sales Trend Over Years")
            plt.show()

            plt.figure(figsize=(10,6))
            sns.scatterplot(x='Sales', y='Profit', data=self.data)
            plt.title("Sales vs Profit")
            plt.show()
        else:
            print("No data available.")

if __name__ == "__main__":
    analyzer = SalesDataAnalyzer("sales_data.csv")
    analyzer.explore_data()
    analyzer.clean_data()
    analyzer.mathematical_operations()
    analyzer.aggregate_functions()
    analyzer.statistical_analysis()
    analyzer.create_pivot_table()
    analyzer.visualize_data()
