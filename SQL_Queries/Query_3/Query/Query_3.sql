# Which countries are not too small and not too big? Modify it to show the country and the area for countries with an area between 200,000 and 250,000.

  SELECT name, area FROM world
    WHERE area BETWEEN 200000 AND 250000