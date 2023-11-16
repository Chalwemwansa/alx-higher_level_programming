-- shows the genres
-- also shows the number of shows linke
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_shows ts INNER JOIN tv_show_genres tsg INNER JOIN tv_genres tg
ON tsg.show_id = ts.id AND tsg.genre_id = tg.id
GROUP BY(tg.name)
ORDER BY number_of_shows DESC;
