from pathlib import Path
import os

import pandas as pd
from sqlalchemy import create_engine

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "retail_source")
DB_USER = os.getenv("DB_USER", "portfolio_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "portfolio_password")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

data_dir = Path("data/raw")

for table_name in ["customers", "products", "orders"]:
    dataframe = pd.read_csv(data_dir / f"{table_name}.csv")
    dataframe.to_sql(
        table_name,
        engine,
        schema="retail",
        if_exists="append",
        index=False,
        method="multi",
    )
    print(f"Loaded {len(dataframe)} records into retail.{table_name}")