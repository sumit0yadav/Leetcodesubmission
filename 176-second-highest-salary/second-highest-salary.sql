# Write your MySQL query statement below
select max(e1.salary) as SecondHighestSalary
-- select *
from employee e1 join employee e2 on e1.salary < e2.salary;