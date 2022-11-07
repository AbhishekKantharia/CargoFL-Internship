# Show the year, subject, and name of winners for 1980 excluding chemistry and medicine

SELECT * FROM nobel WHERE yr = 1980 AND subject NOT IN ('Chemistry', 'Medicine');