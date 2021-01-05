SELECT DISTINCT s.seller_id
FROM Sales AS s
GROUP BY s.seller_id
HAVING SUM(s.price) = (SELECT SUM(price) AS max_price
                       FROM Sales
                       GROUP BY seller_id
                       ORDER BY max_price DESC
                       LIMIT 1)

