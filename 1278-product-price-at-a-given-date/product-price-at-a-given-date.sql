# Write your MySQL query statement below
with cte as (select product_id,new_price,max(change_date) as latest_date from Products
where change_date < '2019-08-17'
group by product_id)

select distinct p1.product_id,p1.new_price as price from cte c
-- select distinct * from Products p1
left join Products p1
on p1.product_id=c.product_id and c.latest_date=p1.change_date

union
select distinct product_id, 10 as price
from Products
group by product_id
having (min(change_date) > "2019-08-16")