# Write your MySQL query statement below

SELECT DISTINCT(v.author_id) AS id
FROM Views v
WHERE v.author_id = V.viewer_id
ORDER BY id ASC
