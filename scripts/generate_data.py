from pathlib import Path
from datetime import datetime, timedelta
import random

import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

N_CUSTOMERS = 500
N_PRODUCTS = 80
N_ORDERS = 5000

customers = pd.DataFrame(
    [
        {
            "customer_id": customer_id,
            "customer_name": fake.name(),
            "email": fake.email(),
            "city": fake.city(),
            "state": fake.state(),
            "created_at": fake.date_between(start_date="-2y", end_date="today"),
        }
        for customer_id in range(1, N_CUSTOMERS + 1)
    ]
)

categories = ["Electronics", "Home", "Fashion", "Sports", "Books"]
products = pd.DataFrame(
    [
        {
            "product_id": product_id,
            "product_name": fake.word().title() + " Product",
            "category": random.choice(categories),
            "unit_price": round(random.uniform(200, 5000), 2),
        }
        for product_id in range(1, N_PRODUCTS + 1)
    ]
)

orders = []
for order_id in range(1, N_ORDERS + 1):
    product = products.sample(1, random_state=order_id).iloc[0]
    quantity = random.randint(1, 5)
    order_date = datetime.now() - timedelta(days=random.randint(0, 365))
    orders.append(
        {
            "order_id": order_id,
            "customer_id": random.randint(1, N_CUSTOMERS),
            "product_id": int(product["product_id"]),
            "order_date": order_date.date(),
            "quantity": quantity,
            "unit_price": float(product["unit_price"]),
            "order_status": random.choice(["completed", "completed", "completed", "cancelled"]),
        }
    )

pd.DataFrame(orders).to_csv(OUTPUT_DIR / "orders.csv", index=False)
customers.to_csv(OUTPUT_DIR / "customers.csv", index=False)
products.to_csv(OUTPUT_DIR / "products.csv", index=False)

print("Created customers.csv, products.csv, and orders.csv")