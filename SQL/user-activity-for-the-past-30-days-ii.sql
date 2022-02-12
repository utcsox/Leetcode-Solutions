WITH CTE AS (SELECT user_id, COUNT(DISTINCT session_id) as dsd
             FROM Activity
             WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
             GROUP BY user_id)

SELECT IFNULL(ROUND(SUM(dsd) / COUNT(user_id), 2), 0.00) AS average_sessions_per_user
FROM CTE
