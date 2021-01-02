# Write your MySQL query statement below

SELECT c.customer_id, c.name
FROM Customers AS c
JOIN Orders AS o
ON c.customer_id = o.customer_id
JOIN Product AS p
ON o.product_id = p.product_id
GROUP BY c.customer_id
Having
    (sum(case when month(o.order_date) = 6 then (o.quantity * p.price) else 0 end) >= 100) AND
    (sum(case when month(o.order_date) = 7 then (o.quantity * p.price) else 0 end) >= 100)
