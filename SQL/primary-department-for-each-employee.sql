SELECT employee_id, department_id
FROM EMPLOYEE
WHERE primary_flag = 'Y'
UNION
SELECT employee_id, department_id
FROM EMPLOYEE
GROUP BY employee_id
HAVING COUNT(employee_id) = 1
