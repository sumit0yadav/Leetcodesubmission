# Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.customer_id) as count_no_trans
-- SELECT v.customer_id,v.visit_id,t.transaction_id
FROM Visits v
LEFT JOIN Transactions t
ON t.visit_id=v.visit_id
WHERE t.transaction_id is NULL
GROUP BY v.customer_id

