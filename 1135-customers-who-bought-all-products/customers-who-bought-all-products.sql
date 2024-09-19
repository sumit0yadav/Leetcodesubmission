# Write your MySQL query statement below
with cte as(
    select count(distinct product_key) as total from Product
)
select c.customer_id from Customer c
cross join cte cc
group by c.customer_id
having count(distinct c.product_key)=(select cc.total from cte cc)
