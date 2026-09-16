import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# -----------------------------
# SETTINGS
# -----------------------------

np.random.seed(42)
random.seed(42)

NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 500
NUM_ORDERS = 50000

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------
# CUSTOMER DATA
# -----------------------------

first_names = [
    "Aarav", "Aditya", "Arjun", "Rahul", "Rohan",
    "Vikash", "Karan", "Aman", "Ankit", "Sahil",
    "Priya", "Ananya", "Neha", "Pooja", "Sneha",
    "Kavya", "Isha", "Riya", "Simran", "Aditi"
]

last_names = [
    "Sharma", "Singh", "Kumar", "Verma", "Gupta",
    "Patel", "Rajput", "Yadav", "Mishra", "Agarwal"
]

locations = [
    ("Delhi", "Delhi", "North"),
    ("Jaipur", "Rajasthan", "North"),
    ("Lucknow", "Uttar Pradesh", "North"),
    ("Kanpur", "Uttar Pradesh", "North"),
    ("Chandigarh", "Chandigarh", "North"),
    ("Mumbai", "Maharashtra", "West"),
    ("Pune", "Maharashtra", "West"),
    ("Ahmedabad", "Gujarat", "West"),
    ("Surat", "Gujarat", "West"),
    ("Bengaluru", "Karnataka", "South"),
    ("Chennai", "Tamil Nadu", "South"),
    ("Hyderabad", "Telangana", "South"),
    ("Kochi", "Kerala", "South"),
    ("Kolkata", "West Bengal", "East"),
    ("Bhubaneswar", "Odisha", "East"),
    ("Patna", "Bihar", "East")
]

customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    first = random.choice(first_names)
    last = random.choice(last_names)

    city, state, region = random.choice(locations)

    customers.append({
        "customer_id": f"C{i:05d}",
        "customer_name": f"{first} {last}",
        "email": f"{first.lower()}.{last.lower()}{i}@example.com",
        "city": city,
        "state": state,
        "region": region
    })

customers_df = pd.DataFrame(customers)


# -----------------------------
# PRODUCT DATA
# -----------------------------

categories = {
    "Electronics": [
        "Wireless Mouse",
        "Keyboard",
        "Headphones",
        "Bluetooth Speaker",
        "Power Bank",
        "Smart Watch",
        "USB Cable",
        "Webcam",
        "Monitor",
        "Laptop Stand"
    ],
    "Home & Kitchen": [
        "Mixer Grinder",
        "Electric Kettle",
        "Cookware Set",
        "Air Fryer",
        "Water Bottle",
        "Coffee Maker",
        "Dinner Set",
        "Storage Box",
        "Vacuum Cleaner",
        "Kitchen Scale"
    ],
    "Fashion": [
        "T-Shirt",
        "Jeans",
        "Hoodie",
        "Sneakers",
        "Formal Shirt",
        "Jacket",
        "Kurta",
        "Dress",
        "Track Pants",
        "Backpack"
    ],
    "Beauty": [
        "Face Wash",
        "Moisturizer",
        "Shampoo",
        "Perfume",
        "Face Serum",
        "Sunscreen",
        "Lip Balm",
        "Hair Oil",
        "Body Lotion",
        "Makeup Kit"
    ],
    "Sports": [
        "Cricket Bat",
        "Football",
        "Badminton Racket",
        "Yoga Mat",
        "Skipping Rope",
        "Gym Gloves",
        "Tennis Ball",
        "Sports Shoes",
        "Dumbbells",
        "Resistance Band"
    ],
    "Books": [
        "Python Programming",
        "Data Science Handbook",
        "Machine Learning Guide",
        "SQL Complete Guide",
        "Business Analytics",
        "Digital Marketing",
        "Web Development",
        "Finance Basics",
        "Leadership Skills",
        "Fiction Novel"
    ],
    "Furniture": [
        "Office Chair",
        "Study Table",
        "Bookshelf",
        "Sofa",
        "Coffee Table",
        "Bedside Table",
        "Dining Chair",
        "Computer Desk",
        "Wardrobe",
        "TV Unit"
    ]
}

products = []

for i in range(1, NUM_PRODUCTS + 1):

    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])

    # Add unique number so product names don't all duplicate
    product_name = f"{product_name} {i}"

    sub_categories = {
        "Electronics": "Gadgets",
        "Home & Kitchen": "Kitchen & Home",
        "Fashion": "Clothing",
        "Beauty": "Personal Care",
        "Sports": "Fitness",
        "Books": "Books",
        "Furniture": "Home Furniture"
    }

    cost_price = round(random.uniform(200, 15000), 2)

    # Selling price generally higher than cost
    selling_price = round(
        cost_price * random.uniform(1.15, 1.60),
        2
    )

    products.append({
        "product_id": f"P{i:04d}",
        "product_name": product_name,
        "category": category,
        "sub_category": sub_categories[category],
        "cost_price": cost_price,
        "selling_price": selling_price
    })

products_df = pd.DataFrame(products)


# -----------------------------
# ORDER DATA
# -----------------------------

customer_ids = customers_df["customer_id"].tolist()
product_ids = products_df["product_id"].tolist()

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

orders = []

for i in range(1, NUM_ORDERS + 1):

    customer_id = random.choice(customer_ids)
    product_id = random.choice(product_ids)

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    order_date = start_date + timedelta(days=random_days)

    quantity = random.choices(
        [1, 2, 3, 4, 5],
        weights=[50, 25, 15, 7, 3]
    )[0]

    product_row = products_df[
        products_df["product_id"] == product_id
    ].iloc[0]

    selling_price = product_row["selling_price"]

    discount = random.choice([
        0,
        0.05,
        0.10,
        0.15,
        0.20,
        0.25
    ])

    returned = random.choices(
        ["No", "Yes"],
        weights=[92, 8]
    )[0]

    orders.append({
        "order_id": f"O{i:06d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "selling_price": selling_price,
        "discount": discount,
        "returned": returned
    })

orders_df = pd.DataFrame(orders)


# -----------------------------
# SAVE DATA
# -----------------------------

customers_df.to_csv(
    OUTPUT_DIR / "customers.csv",
    index=False
)

products_df.to_csv(
    OUTPUT_DIR / "products.csv",
    index=False
)

orders_df.to_csv(
    OUTPUT_DIR / "orders.csv",
    index=False
)


# -----------------------------
# DISPLAY SUMMARY
# -----------------------------

print("\n===================================")
print(" E-COMMERCE DATASET GENERATED")
print("===================================")

print(f"Customers : {len(customers_df):,}")
print(f"Products  : {len(products_df):,}")
print(f"Orders    : {len(orders_df):,}")

print("\nFiles created:")

print("data/customers.csv")
print("data/products.csv")
print("data/orders.csv")

print("\nDataset generation completed successfully!")
