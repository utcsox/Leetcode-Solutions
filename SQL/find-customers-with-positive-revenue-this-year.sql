WITH CTE AS(
    SELECT customer_id, year, revenue
    FROM Customers
    GROUP BY customer_id, year
)

SELECT customer_id
FROM CTE
WHERE year = 2021 and revenue > 0
