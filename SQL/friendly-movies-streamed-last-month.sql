# Write your MySQL query statement below

SELECT DISTINCT c.title
FROM TVProgram t
LEFT JOIN Content c
ON t.content_id = c.content_id
WHERE c.kids_content = 'Y' AND LEFT(t.program_date, 7) = '2020-06' AND c.content_type = 'Movies'
