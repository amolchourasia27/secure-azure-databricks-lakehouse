from datetime import date, timedelta
from pathlib import Path
import logging
import random

import pandas as pd
from faker import Faker

RANDOM_SEED = 42
CUSTOMER_COUNT = 500
PRODUCT_COUNT = 80
ORDER_COUNT = 5_000
OUTPUT_DIRECTORY = Path("data/raw")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

fake = Faker("en_IN")
Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)


def generate_customers() -> pd.DataFrame:
    """Create synthetic retail customer records."""
    records = []

    for customer_id in range(1, CUSTOMER_COUNT + 1):
        created_at = fake.date_between(start_date="-2y", end_date="today")
        records.append(
            {
                "customer_id": customer_id,
                "customer_name": fake.name(),
                "email": fake.unique.email(),
                "city": fake.city(),
                "state": fake.state(),
                "created_at": created_at,
            }
        )

    return pd.DataFrame(records)


def generate_products() -> pd.DataFrame:
    """Create synthetic retail product records."""
    categories = {
        "Electronics": ["Wireless Headphones", "Smart Watch", "USB Hub"],
        "Home": ["Desk Lamp", "Storage Box", "Water Bottle"],
        "Fashion": ["Cotton Shirt", "Travel Backpack", "Running Shoes"],
        "Sports": ["Yoga Mat", "Cricket Bat", "Fitness Band"],
        "Books": ["Data Engineering Guide", "Cloud Fundamentals", "SQL Handbook"],
    }

    records = []

    for product_id in range(1, PRODUCT_COUNT + 1):
        category = random.choice(list(categories))
        product_name = random.choice(categories[category])

        records.append(
            {
                "product_id": product_id,
                "product_name": f"{product_name} {product_id}",
                "category": category,
                "unit_price": round(random.uniform(199.00, 9_999.00), 2),
            }
        )

    return pd.DataFrame(records)


def generate_orders(
    customers: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:
    """Create synthetic retail order records."""
    records = []
    start_date = date.today() - timedelta(days=365)

    for order_id in range(1, ORDER_COUNT + 1):
        product = products.sample(n=1, random_state=RANDOM_SEED + order_id).iloc[0]

        records.append(
            {
                "order_id": order_id,
                "customer_id": random.choice(customers["customer_id"].tolist()),
                "product_id": int(product["product_id"]),
                "order_date": start_date + timedelta(days=random.randint(0, 365)),
                "quantity": random.randint(1, 5),
                "unit_price": product["unit_price"],
                "order_status": random.choices(
                    population=["completed", "cancelled", "returned"],
                    weights=[0.85, 0.10, 0.05],
                    k=1,
                )[0],
            }
        )

    return pd.DataFrame(records)


def save_data(dataframe: pd.DataFrame, file_name: str) -> None:
    """Save a generated dataset as CSV."""
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIRECTORY / file_name
    dataframe.to_csv(output_path, index=False)
    logger.info("Created %s with %s rows", output_path, len(dataframe))


def main() -> None:
    """Generate all synthetic source datasets."""
    customers = generate_customers()
    products = generate_products()
    orders = generate_orders(customers, products)

    save_data(customers, "customers.csv")
    save_data(products, "products.csv")
    save_data(orders, "orders.csv")

    logger.info("Synthetic retail data generation completed successfully.")


if __name__ == "__main__":
    main()