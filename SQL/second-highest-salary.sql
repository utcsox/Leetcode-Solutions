Select max(Salary) as SecondHighestSalary
From Employee
Where Salary < (Select max(Salary)
               From Employee)
