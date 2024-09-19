with cte as (select e.id,e.name,e.salary,e.departmentId,d.name as dept_name
from Employee e left join Department d
on e.departmentId=d.id),
cte2 as(

select dept_name as Department, name as Employee, salary as Salary,
DENSE_RANK() OVER (
    PARTITION BY dept_name
    ORDER BY salary desc
) as rankk
from cte
)

select a.Department,a.Employee,a.Salary
from cte2 a
where a.rankk<=3
