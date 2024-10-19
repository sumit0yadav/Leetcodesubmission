
with cte as (select s1.id-1 as id,s1.student as student from Seat s1 where s1.id%2=0
union
select s1.id+1 as id,s1.student as student from Seat s1 where s1.id%2=1 
order by id asc
)

select case when s.id=(select max(id) from Seat)+1 then s.id-1 else s.id end as id ,s.student
from cte s
