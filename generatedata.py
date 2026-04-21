import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

dates = pd.date_range(start="2024-01-01", end="2024-12-31")

products = {
    "Laptop": ("Electronics", 900),
    "Smartphone": ("Electronics", 700),
    "Tablet": ("Electronics", 400),
    "Headphones": ("Accessories", 150),
    "Smartwatch": ("Accessories", 250),
    "Monitor": ("Electronics", 300),
    "Keyboard": ("Accessories", 50),
    "Mouse": ("Accessories", 30),
    "Printer": ("Electronics", 200),
    "Speaker": ("Accessories", 120),
    "Camera": ("Electronics", 600),
    "External Hard Drive": ("Storage", 100),
    "USB Drive": ("Storage", 20),
    "Router": ("Networking", 80),
    "Microphone": ("Accessories", 110)
}

regions = ["North", "South", "East", "West"]
channels = ["Online", "Retail Store"]
customer_types = ["New", "Returning"]

data = []

for i in range(rows):

    product = np.random.choice(list(products.keys()))
    category, price = products[product]

    quantity = np.random.randint(1, 15)
    discount = np.random.choice([0, 0.05, 0.10, 0.15])

    revenue = quantity * price * (1 - discount)

    data.append([
        np.random.choice(dates),
        product,
        category,
        quantity,
        price,
        discount,
        revenue,
        np.random.choice(regions),
        np.random.choice(channels),
        np.random.choice(customer_types)
    ])

df = pd.DataFrame(data, columns=[
    "Date",
    "Product",
    "Category",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Revenue",
    "Region",
    "Sales_Channel",
    "Customer_Type"
])

# Introduce missing values
for col in df.columns:
    df.loc[df.sample(30).index, col] = np.nan

df.to_csv("sales_dataset_1000_rows.csv", index=False)

print("Dataset created successfully!")