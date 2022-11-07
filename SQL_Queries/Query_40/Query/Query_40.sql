SELECT teacher.name, dept.name
FROM teacher
INNER JOIN dept
ON (teacher.dept = dept.id)