# Write your MySQL query statement below
SELECT SchoolA.student_name AS member_A, SchoolB.student_name AS member_B, SchoolC.student_name AS member_C
FROM SchoolA, SchoolB, SchoolC
WHERE SchoolA.student_id != SchoolB.student_id
AND SchoolA.student_id != SchoolC.student_id
AND SchoolB.student_id != SchoolC.student_id
AND SchoolA.student_name != SchoolB.student_name
AND SchoolA.student_name != SchoolC.student_name
AND SchoolB.student_name != SchoolC.student_name


# Write your MySQL query statement below
SELECT SchoolA.student_name AS member_A, SchoolB.student_name AS member_B, SchoolC.student_name AS member_C
FROM SchoolA CROSS JOIN SchoolB CROSS JOIN SchoolC
WHERE SchoolA.student_id != SchoolB.student_id
AND SchoolA.student_id != SchoolC.student_id
AND SchoolB.student_id != SchoolC.student_id
AND SchoolA.student_name != SchoolB.student_name
AND SchoolA.student_name != SchoolC.student_name
AND SchoolB.student_name != SchoolC.student_name
