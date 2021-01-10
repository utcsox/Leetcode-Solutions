# Write your MySQL query statement below

SELECT a.extra AS report_reason, COUNT(DISTINCT(a.post_id)) AS report_count
FROM Actions a
WHERE a.action_date = '2019-07-04' and action = 'report'
GROUP BY a.extra
