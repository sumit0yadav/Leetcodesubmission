SELECT r.contest_id,
       ROUND(COUNT(DISTINCT r.user_id) * 100 / (SELECT COUNT(DISTINCT user_id) FROM Users), 2) AS percentage
FROM Register r
LEFT JOIN Users u ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY Percentage DESC, r.contest_id ASC;
