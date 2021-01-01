# Write your MySQL query statement below

SELECT ROUND(100*SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1
            ELSE 0 END)/COUNT(1), 2) AS 'immediate_percentage'
FROM Delivery 

WITH cte AS
    (
    SELECT CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1
                ELSE 0 END AS immediate_or_scheduled
    FROM Delivery AS d)
    
Select ROUND(100*SUM(immediate_or_scheduled)/COUNT(immediate_or_scheduled), 2) AS immediate_percentage
from cte
