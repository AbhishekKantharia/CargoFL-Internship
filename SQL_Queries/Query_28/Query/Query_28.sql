# What is the total population of ('Estonia', 'Latvia', 'Lithuania').

SELECT SUM(population)
FROM world
WHERE name IN ('Estonia', 'Latvia', 'Lithuania');