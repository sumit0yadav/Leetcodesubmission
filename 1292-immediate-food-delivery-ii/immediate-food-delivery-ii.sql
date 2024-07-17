WITH FirstOrders AS (
    SELECT
        customer_id,
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
),
FirstOrdersOnly AS (
    SELECT
        customer_id,
        order_date,
        customer_pref_delivery_date
    FROM FirstOrders
    WHERE rn = 1
),
ImmediateFirstOrders AS (
    SELECT
        COUNT(*) AS immediate_count
    FROM FirstOrdersOnly
    WHERE order_date = customer_pref_delivery_date
),
TotalFirstOrders AS (
    SELECT
        COUNT(*) AS total_count
    FROM FirstOrdersOnly
)
SELECT
    ROUND(
        (immediate_count * 100.0 / total_count),
        2
    ) AS immediate_percentage
FROM
    ImmediateFirstOrders,
    TotalFirstOrders;
