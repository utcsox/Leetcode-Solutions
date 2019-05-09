SELECT e1.Name as Employee
FROM Employee AS e1 
LEFT JOIN Employee AS e2
on e1.ManagerId = e2.Id
where e1.Salary > e2.Salary;
