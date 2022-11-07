SELECT teacher.name, dept.name
FROM teacher
LEFT OUTER JOIN dept
ON teacher.dept = dept.id;