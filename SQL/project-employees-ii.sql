# Write your MySQL query statement below

WITH CTE AS (SELECT p.project_id, COUNT(p.employee_id) AS employees_count
             FROM Project p
             GROUP BY p.project_id)
             
SELECT p.project_id
FROM Project p
GROUP BY p.project_id
HAVING COUNT(p.employee_id) = (SELECT MAX(employees_count)
                            FROM CTE)
                            
WITH CTE AS (SELECT p.project_id, COUNT(p.employee_id) AS employees_count
             FROM Project p
             GROUP BY p.project_id)
             
SELECT c.project_id
FROM CTE c
WHERE c.employees_count = (SELECT MAX(employees_count)
                            FROM CTE)
