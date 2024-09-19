with cte as (select player_id, min(event_date) as md from Activity
group by player_id)
-- select p1.player_id,p1.event_date,p2.md from Activity p1
select ROUND(sum(case when DATE_SUB(p1.event_date, INTERVAL 1 DAY) = p2.md
 then 1 else 0 end)/count(distinct p1.player_id),2) as fraction from Activity p1

left join cte p2
on p1.player_id=p2.player_id
