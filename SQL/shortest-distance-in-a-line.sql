# Write your MySQL query statement below

SELECT MIN(ABS(p1.x-p2.x)) AS shortest
From point p1
CROSS JOIN point p2
WHERE p1.x <> p2.x
