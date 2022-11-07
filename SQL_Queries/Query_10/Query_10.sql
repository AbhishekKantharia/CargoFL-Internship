# Give the name of the 'peace' winners since the year 2000, including 2000.

SELECT winner FROM nobel WHERE subject = 'Peace' AND yr >= 2000;