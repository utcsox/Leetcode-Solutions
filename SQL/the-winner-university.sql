WITH NYU AS (
    SELECT COUNT(student_id) AS student_count
    FROM NewYork
    Where score >= 90
), CAU AS (
    SELECT COUNT(student_id) AS student_count
    FROM California
    WHERE score >= 90
)

SELECT (
CASE WHEN n.student_count > c.student_count THEN 'New York University'
     WHEN n.student_count < c.student_count THEN 'California University'
     ELSE 'No Winner'
END) winner
FROM NYU n, CAU c
