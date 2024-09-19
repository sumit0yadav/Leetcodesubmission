# Write your MySQL query statement below
select e1.employee_id
from Employees e1

left join Employees e2
on e2.employee_id=e1.manager_id
where e1.salary<30000 and e2.employee_id is NULL and e1.manager_id is not NULL
order by e1.employee_id asc
