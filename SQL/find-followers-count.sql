# Write your MySQL query statement below


SELECT f1.user_id, COUNT(1) aS followers_count
FROM Followers f1
GROUP BY f1.user_id
ORDER BY f1.user_id
