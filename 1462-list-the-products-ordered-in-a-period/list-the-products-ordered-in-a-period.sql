-- WITH cte AS(
--     SELECT * 
--     FROM Orders o
--     WHERE MONTH(o.order_date)=2
-- )

SELECT p.product_name, SUM(o.unit) as unit
FROM Orders o
JOIN Products p
ON p.product_id=o.product_id
WHERE o.order_date >= '2020-02-01' 
  AND o.order_date <= '2020-02-29'
GROUP BY p.product_name
HAVING unit>99