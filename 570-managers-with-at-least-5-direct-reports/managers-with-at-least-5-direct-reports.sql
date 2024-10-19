select e.name as name from Employee e
RIGHT JOIN Employee e1
ON e.id=e1.managerId
WHERE e.id is not null
group by e.id
having count(e.id)>4