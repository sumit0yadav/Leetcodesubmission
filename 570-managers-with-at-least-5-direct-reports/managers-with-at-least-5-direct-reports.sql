# Write your MySQL query statement below
WITH CTE AS (select managerId,count(managerId) as count from Employee
WHERE managerId is not NULL
GROUP BY managerId
having count(managerId)>4)

select e.name as name
FROM CTE c
JOIN Employee e
ON c.managerId=e.id
-- WHERE e.name is not NULL
-- WITH CTE AS (
--     SELECT managerId, COUNT(managerId) AS count 
--     FROM Employee
--     WHERE managerId IS NOT NULL
--     GROUP BY managerId
--     HAVING COUNT(managerId) > 4
-- )
-- SELECT e.name AS name
-- FROM CTE c
-- JOIN Employee e ON c.managerId = e.id;
