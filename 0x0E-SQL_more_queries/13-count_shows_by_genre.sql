-- shows the genres
-- also shows the number of shows linke
-- Shows the genres and the number of shows linked to each genre
SELECT tg.name, COUNT(ts.id) AS number_of_shows
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id, , tv_genres tg
GROUP BY tg.name;
