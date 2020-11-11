# Write your MySQL query statement below

Select Users.name, SUM(Transactions.amount) AS Balance
FROM Users
JOIN Transactions
ON Users.account = Transactions.account
GROUP BY Users.account
Having Balance > 10000
