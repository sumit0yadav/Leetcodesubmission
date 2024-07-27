WITH ed AS (SELECT 

d.id as id,
d.name as dep,
e.name as name,
e.salary as Salary,
DENSE_RANK() OVER (PARTITION BY d.id ORDER BY salary DESC) as rnk

FROM Employee e
JOIN Department d
ON e.departmentId = d.id
)
SELECT dep as Department, name as Employee, Salary
FROM ed
WHERE rnk<=3
