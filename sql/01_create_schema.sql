DROP SCHEMA IF EXISTS retail CASCADE;
CREATE SCHEMA retail;

CREATE TABLE retail.customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT,
    state TEXT,
    created_at DATE
);

CREATE TABLE retail.products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL
);

CREATE TABLE retail.orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES retail.customers(customer_id),
    product_id INTEGER NOT NULL REFERENCES retail.products(product_id),
    order_date DATE NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL CHECK (unit_price >= 0),
    order_status TEXT NOT NULL
);

CREATE INDEX idx_orders_customer_id ON retail.orders(customer_id);
CREATE INDEX idx_orders_product_id ON retail.orders(product_id);
CREATE INDEX idx_orders_order_date ON retail.orders(order_date);