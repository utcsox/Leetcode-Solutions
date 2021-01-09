# Write your MySQL query statement below

SELECT DISTINCT(a.seat_id)
FROM cinema a
CROSS JOIN cinema b
WHERE ABS(a.seat_id-b.seat_id) = 1 AND a.free = True AND b.free = True
ORDER BY a.seat_id
