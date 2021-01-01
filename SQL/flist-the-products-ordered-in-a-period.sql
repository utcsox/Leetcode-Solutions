# Write your MySQL query statement below

SELECT CTE.product_name, CTE.units as unit
FROM (SELECT p.product_name, sum(o.unit) as units, o.order_date
    FROM Orders o
    JOIN Products p
    ON p.product_id = o.product_id
    WHERE LEFT(o.order_date, 7) = '2020-02'
    GROUP BY p.product_name) AS CTE
WHERE CTE.units >= 100 
