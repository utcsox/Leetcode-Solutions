# 1.  IN + Subquery
SELECT id, name
FROM Students
WHERE department_id NOT IN (
    SELECT id
    FROM Departments
)
# 2.  LEFT JOIN + Filter
SELECT Students.id, Students.name
FROM Students
LEFT JOIN Departments
ON students.department_id = Departments.id
WHERE Departments.id is NULL
