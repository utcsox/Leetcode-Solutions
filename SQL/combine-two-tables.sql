SELECT p.FirstName as FirstName, p.LastName as LastName, a.City as City, a.State as State
FROM Person p
LEFT JOIN Address  a
on p.PersonID = a.PersonID
