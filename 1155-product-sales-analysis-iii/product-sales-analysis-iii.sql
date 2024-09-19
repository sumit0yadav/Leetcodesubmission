# Write your MySQL query statement below
with cte as (select product_id,min(year) as min_year
from Sales
group by product_id)

select p2.product_id,p2.year as first_year,p2.quantity,p2.price from cte p1
-- select * from cte p1
left join Sales p2

on p2.year=p1.min_year and p1.product_id=p2.product_id