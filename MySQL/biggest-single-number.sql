
WITH CTE AS (SELECT num
             FROM myNumbers
             GROUP BY num
             Having COUNT(num) = 1)
             
SELECT MAX(num) AS num
FROM CTE
