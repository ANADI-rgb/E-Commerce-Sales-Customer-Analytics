import pandas as pd
import mysql.connector
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# CSV files
customers_file = DATA_DIR / "customers.csv"
products_file = DATA_DIR / "products.csv"
orders_file = DATA_DIR / "cleaned_orders.csv"

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditya@2004",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")

# Load CSV files
customers = pd.read_csv(customers_file)
products = pd.read_csv(products_file)
orders = pd.read_csv(orders_file)

print(f"Customers loaded from CSV: {len(customers):,}")
print(f"Products loaded from CSV : {len(products):,}")
print(f"Orders loaded from CSV   : {len(orders):,}")

# ---------------------------------------------------
# Insert customers
# ---------------------------------------------------

customer_query = """
INSERT INTO customers
(customer_id, customer_name, email, city, state, region)
VALUES (%s, %s, %s, %s, %s, %s)
"""

customer_data = [
    tuple(row)
    for row in customers[
        [
            "customer_id",
            "customer_name",
            "email",
            "city",
            "state",
            "region"
        ]
    ].itertuples(index=False, name=None)
]

cursor.executemany(customer_query, customer_data)
connection.commit()

print(f"Inserted customers: {cursor.rowcount:,}")

# ---------------------------------------------------
# Insert products
# ---------------------------------------------------

product_query = """
INSERT INTO products
(product_id, product_name, category, sub_category,
 cost_price, selling_price)
VALUES (%s, %s, %s, %s, %s, %s)
"""

product_data = [
    tuple(row)
    for row in products[
        [
            "product_id",
            "product_name",
            "category",
            "sub_category",
            "cost_price",
            "selling_price"
        ]
    ].itertuples(index=False, name=None)
]

cursor.executemany(product_query, product_data)
connection.commit()

print(f"Inserted products: {cursor.rowcount:,}")

# ---------------------------------------------------
# Insert orders
# ---------------------------------------------------

order_query = """
INSERT INTO orders
(
    order_id,
    order_date,
    customer_id,
    product_id,
    quantity,
    selling_price,
    discount,
    returned,
    product_name,
    category,
    sub_category,
    cost_price,
    customer_name,
    city,
    state,
    region,
    revenue,
    cost,
    profit,
    profit_margin,
    order_year,
    order_month,
    month_name,
    order_quarter,
    return_flag,
    customer_type
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
)
"""

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
).dt.date

order_columns = [
    "order_id",
    "order_date",
    "customer_id",
    "product_id",
    "quantity",
    "selling_price",
    "discount",
    "returned",
    "product_name",
    "category",
    "sub_category",
    "cost_price",
    "customer_name",
    "city",
    "state",
    "region",
    "revenue",
    "cost",
    "profit",
    "profit_margin",
    "order_year",
    "order_month",
    "month_name",
    "order_quarter",
    "return_flag",
    "customer_type"
]

order_data = [
    tuple(row)
    for row in orders[order_columns].itertuples(
        index=False,
        name=None
    )
]

# Insert in batches
batch_size = 5000

for i in range(0, len(order_data), batch_size):
    batch = order_data[i:i + batch_size]

    cursor.executemany(order_query, batch)
    connection.commit()

    print(
        f"Inserted orders: "
        f"{min(i + batch_size, len(order_data)):,}/"
        f"{len(order_data):,}"
    )

print("\nDatabase import completed successfully!")

cursor.close()
connection.close()

print("MySQL connection closed.")