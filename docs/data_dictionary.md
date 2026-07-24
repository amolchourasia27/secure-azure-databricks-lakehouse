# Retail Source Data Dictionary

## Data classification

This project uses synthetic data only. The fields below are modelled as if they were retail operational data.

| Table | Column | Data type | Description | Classification |
|---|---|---|---|---|
| customers | customer_id | Integer | Unique customer identifier | Internal |
| customers | customer_name | Text | Synthetic customer name | PII - synthetic |
| customers | email | Text | Synthetic customer email address | PII - synthetic |
| customers | city | Text | Customer city | Internal |
| customers | state | Text | Customer state | Internal |
| customers | created_at | Date | Customer creation date | Internal |
| products | product_id | Integer | Unique product identifier | Internal |
| products | product_name | Text | Product display name | Internal |
| products | category | Text | Product category | Internal |
| products | unit_price | Decimal | Listed product price | Confidential business data - synthetic |
| orders | order_id | Integer | Unique order identifier | Internal |
| orders | customer_id | Integer | Reference to customer | Internal |
| orders | product_id | Integer | Reference to product | Internal |
| orders | order_date | Date | Date the order was placed | Internal |
| orders | quantity | Integer | Number of units ordered | Internal |
| orders | unit_price | Decimal | Item price captured at order time | Confidential business data - synthetic |
| orders | order_status | Text | completed, cancelled, or returned | Internal |

## Planned quality rules

- Primary keys must be unique and non-null.
- Order customer IDs must exist in customers.
- Order product IDs must exist in products.
- Quantity must be greater than zero.
- Unit price must be zero or greater.
- Order status must be one of `completed`, `cancelled`, or `returned`.
- PII fields will be access-restricted in later lakehouse layers.