with cte as (
    select visited_on, sum(amount) as total_amount
    from Customer
    group by visited_on
    
), cte2 as(select visited_on, sum(total_amount) over (order by visited_on rows 
between 6 preceding and current row) as amount,
round(avg(total_amount) over (order by visited_on rows 
between 6 preceding and current row),2) as average_amount,
row_number() over (order by visited_on) as row_numb

from cte)


select visited_on,amount,average_amount
from cte2
where row_numb>=7