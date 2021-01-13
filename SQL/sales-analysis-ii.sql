# Write your MySQL query statement below

WITH CTE AS (SELECT DISTINCT s.buyer_id
             FROM Sales s
             JOIN Product p 
             ON s.product_id = p.product_id
             WHERE product_name = 'iPhone'
             GROUP BY s.buyer_id)
             
SELECT buyer_id
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
WHERE product_name = 'S8'
GROUP BY buyer_id 
Having buyer_id NOT IN (SELECT buyer_id FROM CTE)


             
SELECT buyer_id
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
GROUP BY buyer_id 
Having SUM(p.product_name= 'S8') > 0 AND SUM(p.product_name ='iPhone') = 0 
