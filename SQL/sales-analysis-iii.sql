# Write your MySQL query statement below

WITH CTE AS (SELECT s.product_id
             FROM Sales AS s
             JOIN Product AS p
             ON s.product_id = p.product_id
             WHERE s.sale_date < '2019-01-01' OR s.sale_date > '2019-03-31')
             
SELECT DISTINCT(s.product_id), p.product_name 
FROM Sales AS s
JOIN Product AS p
ON s.product_id = p.product_id
WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31' AND s.product_id NOT IN (SELECT CTE.product_id FROM CTE)
ORDER BY s.product_id
