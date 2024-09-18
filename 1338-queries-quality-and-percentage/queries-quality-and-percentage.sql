-- # Write your MySQL query statement below

with cte as (SELECT query_name, 
       COUNT(CASE WHEN rating < 3 THEN 1 ELSE NULL END) AS lesser
FROM Queries
GROUP BY query_name
)

select q.query_name, ROUND(sum(q.rating/q.position)/count(q.query_name),2) as quality, ROUND((c.lesser/count(q.query_name))*100,2) as poor_query_percentage
-- SELECT *
from Queries q
cross join cte c
on c.query_name=q.query_name
group by q.query_name
