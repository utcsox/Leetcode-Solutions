Select Customers.Name AS Customers
From Customers LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE CustomerId IS NULL

SELECT Name AS Customers
FROM Customers
WHERE Id NOT in
(Select CustomerId From Orders)
