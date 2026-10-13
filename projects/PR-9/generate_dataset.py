import pandas as pd
import numpy as np

def generate_sales_data(filename="sales_data.csv", rows=50):
    np.random.seed(42)  # for reproducibility
    
    products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
    regions = ["North", "South", "East", "West", "Central"]
    years = [2021, 2022, 2023]
    
    data = {
        "SalesID": np.arange(101, 101 + rows),
        "Product": np.random.choice(products, rows),
        "Region": np.random.choice(regions, rows),
        "Sales": np.random.randint(400, 1000, rows),
        "Profit": np.random.randint(50, 300, rows),
        "Year": np.random.choice(years, rows)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Sample dataset '{filename}' created successfully!")

generate_sales_data()
