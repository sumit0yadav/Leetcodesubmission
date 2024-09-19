-- # Write your MySQL query statement below
-- select employee_id, case when count(employee_id)=1 then department_id case when primary_flag='Y' then department_id
-- from Employee

select employee_id,department_id from Employee
group by employee_id
having count(employee_id)=1
union
select employee_id,department_id from Employee
where primary_flag='Y'
