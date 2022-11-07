# Show the player, teamid, stadium and mdate for every German goal.

SELECT player, teamid, mdate
FROM game
JOIN goal ON (game.id = goal.matchid)
WHERE teamid = 'GER'