-- shows the genres
-- also shows the number of shows linked to the genre
SELECT tg.name as genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_shows ts INNER JOIN tv_show_genres tsg JOIN tv_genres tg
ON ts.id = tsg.show_id
GROUP BY tg.name;

