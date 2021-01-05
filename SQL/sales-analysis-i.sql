SELECT DISTINCT s.seller_id
FROM Sales AS s
GROUP BY s.seller_id
HAVING SUM(s.price) = (SELECT SUM(price) AS max_price
                       FROM Sales
                       GROUP BY seller_id
                       ORDER BY max_price DESC
                       LIMIT 1)

WITH CTE AS (SELECT seller_id, SUM(price) AS price
             FROM Sales
             GROUP BY seller_id)
             

SELECT seller_id
FROM CTE
WHERE price = (SELECT MAX(price)
               FROM CTE)



WITH CTE AS (SELECT seller_id, RANK() OVER (ORDER BY SUM(price) DESC) ranking
             FROM Sales
             GROUP BY seller_id)

SELECT seller_id
FROM CTE
WHERE ranking = 1
