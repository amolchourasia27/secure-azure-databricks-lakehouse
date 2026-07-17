-- Revenue by product category
SELECT
    p.category,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue,
    SUM(o.quantity) AS units_sold
FROM retail.orders o
JOIN retail.products
    ON o.product_id = p.product_id
WHERE o.order_status = 'completed'
GROUP BY p.category
ORDER BY total_revenue DESC;

-- Top customers by completed-order revenue
SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS lifetime_value
FROM retail.orders o
JOIN retail.customers c
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'completed'
GROUP BY c.customer_id, c.customer_name
ORDER BY lifetime_value DESC
LIMIT 10;

-- Monthly revenue trend
SELECT
    DATE_TRUNC('month', o.order_date)::date AS order_month,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue
FROM retail.orders o
WHERE o.order_status = 'completed'
GROUP BY DATE_TRUNC('month', o.order_date)::date
ORDER BY order_month;