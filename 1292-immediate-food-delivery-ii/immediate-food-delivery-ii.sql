with cte as (select *, 
rank() over (partition by customer_id order by order_date) as order_number,

case when order_date=customer_pref_delivery_date 
then 'imm' else 'sch' end as order_type
from delivery)


select ROUND(sum(case when order_type='imm' then 1 else 0 end)*100/count(*),2) as immediate_percentage
from cte 
where order_number=1