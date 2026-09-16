import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


# ==========================================
# LOAD DATA
# ==========================================

print("\nLoading datasets...")

customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")


print("Customers loaded:", customers.shape)
print("Products loaded :", products.shape)
print("Orders loaded   :", orders.shape)


# ==========================================
# BASIC DATA CLEANING
# ==========================================

print("\nPerforming basic cleaning...")


# Remove duplicate records
customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()


# Convert order date
orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)


# Remove rows with invalid dates
orders = orders.dropna(
    subset=["order_date"]
)


# Convert numeric columns
orders["quantity"] = pd.to_numeric(
    orders["quantity"],
    errors="coerce"
)

orders["selling_price"] = pd.to_numeric(
    orders["selling_price"],
    errors="coerce"
)

orders["discount"] = pd.to_numeric(
    orders["discount"],
    errors="coerce"
)


# Remove invalid quantities
orders = orders[
    orders["quantity"] > 0
]


# Remove invalid prices
orders = orders[
    orders["selling_price"] > 0
]


# ==========================================
# MERGE ORDERS + PRODUCTS
# ==========================================

print("\nMerging orders with product information...")

orders = orders.merge(
    products[
        [
            "product_id",
            "product_name",
            "category",
            "sub_category",
            "cost_price"
        ]
    ],
    on="product_id",
    how="left"
)


# ==========================================
# MERGE ORDERS + CUSTOMERS
# ==========================================

print("Merging customer information...")

orders = orders.merge(
    customers[
        [
            "customer_id",
            "customer_name",
            "city",
            "state",
            "region"
        ]
    ],
    on="customer_id",
    how="left"
)


# ==========================================
# HANDLE MISSING VALUES
# ==========================================

print("\nChecking missing values...")

print(
    orders.isnull().sum()
)


# Remove records where product/customer
# information could not be matched
orders = orders.dropna(
    subset=[
        "product_name",
        "customer_name"
    ]
)


# ==========================================
# REVENUE CALCULATION
# ==========================================

orders["revenue"] = (
    orders["quantity"]
    * orders["selling_price"]
    * (1 - orders["discount"])
)


# ==========================================
# COST CALCULATION
# ==========================================

orders["cost"] = (
    orders["quantity"]
    * orders["cost_price"]
)


# ==========================================
# PROFIT CALCULATION
# ==========================================

orders["profit"] = (
    orders["revenue"]
    - orders["cost"]
)


# ==========================================
# PROFIT MARGIN
# ==========================================

orders["profit_margin"] = np.where(
    orders["revenue"] != 0,
    (orders["profit"] / orders["revenue"]) * 100,
    0
)


# ==========================================
# DATE FEATURES
# ==========================================

orders["order_year"] = (
    orders["order_date"].dt.year
)

orders["order_month"] = (
    orders["order_date"].dt.month
)

orders["month_name"] = (
    orders["order_date"].dt.strftime("%B")
)

orders["order_quarter"] = (
    "Q"
    + orders["order_date"].dt.quarter.astype(str)
)


# ==========================================
# RETURN FLAG
# ==========================================

orders["return_flag"] = np.where(
    orders["returned"] == "Yes",
    1,
    0
)


# ==========================================
# CUSTOMER TYPE
# ==========================================

customer_order_count = (
    orders.groupby("customer_id")["order_id"]
    .transform("count")
)

orders["customer_type"] = np.where(
    customer_order_count == 1,
    "New Customer",
    "Returning Customer"
)


# ==========================================
# ROUND FINANCIAL VALUES
# ==========================================

orders["revenue"] = orders["revenue"].round(2)

orders["cost"] = orders["cost"].round(2)

orders["profit"] = orders["profit"].round(2)

orders["profit_margin"] = (
    orders["profit_margin"].round(2)
)


# ==========================================
# SAVE CLEANED DATA
# ==========================================

output_file = DATA_DIR / "cleaned_orders.csv"

orders.to_csv(
    output_file,
    index=False
)


# ==========================================
# FINAL REPORT
# ==========================================

print("\n======================================")
print(" DATA CLEANING COMPLETED")
print("======================================")

print("\nFinal dataset shape:")
print(orders.shape)

print("\nColumns:")
print(orders.columns.tolist())

print("\nTotal Revenue:")
print(f"₹{orders['revenue'].sum():,.2f}")

print("\nTotal Cost:")
print(f"₹{orders['cost'].sum():,.2f}")

print("\nTotal Profit:")
print(f"₹{orders['profit'].sum():,.2f}")

print("\nAverage Profit Margin:")
print(
    f"{orders['profit_margin'].mean():.2f}%"
)

print("\nReturned Orders:")
print(
    orders["return_flag"].sum()
)

print("\nCustomer Types:")
print(
    orders["customer_type"].value_counts()
)

print("\nSaved file:")
print(output_file)

print("\n======================================")
print(" READY FOR SQL ANALYSIS")
print("======================================")
