# Write your MySQL query statement below
with cte as (select s1.id-1 as id,s1.student from Seat s1 where s1.id%2=0
union 
select s2.id+1 as id,s2.student from Seat s2 where s2.id%2=1
)

select case when (select max(id) from Seat)+1=s3.id then s3.id-1
else s3.id end as id,s3.student
from cte as s3
order by id asc