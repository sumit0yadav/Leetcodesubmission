# Write your MySQL query statement below
SELECT e1.employee_id
FROM Employees e1
WHERE e1.salary<30000 and e1.manager_id not in
(SELECT employee_id from Employees)
ORDER BY e1.employee_id