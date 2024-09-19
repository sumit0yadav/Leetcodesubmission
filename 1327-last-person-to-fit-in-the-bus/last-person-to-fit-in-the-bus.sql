with cte as (# Write your MySQL query statement below
select *,sum(weight) over (order by turn) as cum_sum from Queue
order by turn asc
)

select person_name from cte 
where cum_sum<=1000
order by turn desc
limit 1