# Write your MySQL query statement below
select p1.product_id, ifnull(ROUND(SUM(p1.price*p2.units)/SUM(p2.units),2),0) as average_price
from Prices p1
left join UnitsSold p2
on p1.product_id=p2.product_id

and p2.purchase_date between p1.start_date and p1.end_date
GROUP BY p1.product_id 
