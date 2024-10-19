select e.employee_id as employee_id from Employees e
-- select * from Employees e
LEFT JOIN Employees e1
ON e.manager_id=e1.employee_id
where e.manager_id is not NULL and e1.employee_id is NULL and e.salary<30000
order by employee_id asc