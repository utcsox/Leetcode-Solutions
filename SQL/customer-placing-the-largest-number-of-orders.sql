SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
Limit 1
