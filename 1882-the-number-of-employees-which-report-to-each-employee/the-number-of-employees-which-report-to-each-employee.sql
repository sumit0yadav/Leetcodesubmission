# Write your MySQL query statement below
SELECT e1.employee_id,e1.name,
COUNT(e2.employee_id) as reports_count,
ROUND(AVG(e2.age)) as average_age


FROM Employees e1,Employees e2
WHERE e2.reports_to=e1.employee_id
GROUP BY e1.employee_id
HAVING reports_count>0
ORDER by e1.employee_id