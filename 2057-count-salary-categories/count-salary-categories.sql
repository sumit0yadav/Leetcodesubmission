# Write your MySQL query statement below
(SELECT "Low Salary" as category,
(SELECT count(*) 
FROM Accounts 
WHERE income<20000) as accounts_count)
UNION
(SELECT "Average Salary" as category,
(SELECT count(*) 
FROM Accounts 
WHERE income>=20000 AND income<=50000) as accounts_count)
UNION
(SELECT "High Salary" as category,
(SELECT count(*) 
FROM Accounts 
WHERE income>50000) as accounts_count)