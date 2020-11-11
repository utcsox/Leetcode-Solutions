# Write your MySQL query statement below

SELECT Visits.customer_id, COUNT(Visits.visit_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id is NULL
GrOUP BY Visits.customer_id
