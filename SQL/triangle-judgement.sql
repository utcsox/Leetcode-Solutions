# Write your MySQL query statement below

SELECT t.x, t.y, t.z,
       CASE WHEN (x + y > z) AND (y + z > x) AND (x + z > y) THEN "Yes"
            ELSE "No" END AS triangle
FROM triangle AS t
