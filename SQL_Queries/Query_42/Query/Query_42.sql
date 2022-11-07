SELECT teacher.name, dept.name
FROM teacher
RIGHT OUTER JOIN dept
ON teacher.dept = dept.id;