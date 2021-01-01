# Write your MySQL query statement below

SELECT e1.employee_id, e2.team_size
FROM Employee AS e1
JOIN (SELECT team_id, COUNT(team_id) AS team_size
      FROM Employee 
      GROUP BY team_id) AS e2
WHERE e1.team_id = e2.team_id


SELECT employee_id, COUNT(employee_id) OVER (PARTITION BY team_id AS team_size
FROM Employee
