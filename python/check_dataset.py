import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")

print("\n========== CUSTOMERS ==========")
print(customers.head())
print("\nShape:", customers.shape)

print("\n========== PRODUCTS ==========")
print(products.head())
print("\nShape:", products.shape)

print("\n========== ORDERS ==========")
print(orders.head())
print("\nShape:", orders.shape)

print("\n========== MISSING VALUES ==========")

print("\nCustomers:")
print(customers.isnull().sum())

print("\nProducts:")
print(products.isnull().sum())

print("\nOrders:")
print(orders.isnull().sum())

print("\n========== DUPLICATES ==========")

print("Customer duplicates:", customers.duplicated().sum())
print("Product duplicates:", products.duplicated().sum())
print("Order duplicates:", orders.duplicated().sum())