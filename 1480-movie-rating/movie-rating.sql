(Select u.name as results 
from MovieRating as m, Users as u 
where u.user_id = m.user_id
Group By m.user_id 
Order by count(m.user_id) desc, u.name
LIMIT 1)

UNION ALL

(Select u.title as results 

from MovieRating as m, Movies as u 
where u.movie_id = m.movie_id
and m.created_at like "2020-02-%"
Group By m.movie_id 

Order by AVG(m.rating) desc, u.title
LIMIT 1)
