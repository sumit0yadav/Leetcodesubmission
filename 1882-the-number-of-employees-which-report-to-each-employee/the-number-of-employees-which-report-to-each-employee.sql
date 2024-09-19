# Write your MySQL query statement below
select e1.employee_id,e1.name ,count(distinct e2.employee_id ) as reports_count, round(avg(e2.age),0) as average_age 
from Employees e1
left join Employees e2
on e2.reports_to=e1.employee_id

group by e1.employee_id
having count(distinct e2.employee_id)!=0