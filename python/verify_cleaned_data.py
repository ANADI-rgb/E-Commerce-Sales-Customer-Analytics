import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

df = pd.read_csv(
    DATA_DIR / "cleaned_orders.csv"
)

print("\n========== DATASET INFO ==========")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n========== FIRST 5 ROWS ==========")

print(df.head())

print("\n========== DATA TYPES ==========")

print(df.dtypes)

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())

print("\n========== DUPLICATES ==========")

print(
    "Duplicate rows:",
    df.duplicated().sum()
)

print("\n========== FINANCIAL SUMMARY ==========")

print(
    df[
        [
            "revenue",
            "cost",
            "profit",
            "profit_margin"
        ]
    ].describe()
)

print("\n========== CATEGORIES ==========")

print(
    df["category"].value_counts()
)

print("\n========== REGIONS ==========")

print(
    df["region"].value_counts()
)

print("\n========== CUSTOMER TYPES ==========")

print(
    df["customer_type"].value_counts()
)

print("\n================================")
print(" VERIFICATION COMPLETE")
print("================================")