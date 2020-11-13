# Write your MySQL query statement below
SELECT Warehouse.name AS warehouse_name, SUM(Warehouse.units * Products.Width * Products.Length *Products.Height) as volume
FROM Warehouse
LEFT JOIN Products
ON Warehouse.product_id = Products.product_id
GROUP BY Warehouse.name
