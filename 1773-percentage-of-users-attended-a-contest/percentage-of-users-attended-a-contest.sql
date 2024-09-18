with cte as ( select count(*) as total from Users)

select r.contest_id,
round((count(distinct r.user_id)/c.total)*100,2) as percentage

from Register r
cross join cte c
group by r.contest_id
order by percentage desc,r.contest_id asc