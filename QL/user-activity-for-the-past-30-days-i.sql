# Write your MySQL query statement below

SELECT a.activity_date AS day, COUNT(DISTINCT a.user_id) AS active_users
FROM Activity a
WHERE a.activity_date BETWEEN DATE_ADD('2019-07-27', INTERVAL -29 DAY) AND '2019-07-27'
GROUP BY a.activity_date 
Having active_users> 0


SELECT a.activity_date AS day, COUNT(DISTINCT a.user_id) AS active_users
FROM Activity a
WHERE DATEDIFF('2019-07-27', a.activity_date ) < 30
GROUP BY a.activity_date 
Having active_users> 0
