-- shows the genres for the title DEXTER
-- demonstrating the use of the SELECT and the join operations
SELECT tg.name
FROM tv_shows ts INNER JOIN tv_show_genres tsg INNER JOIN tv_genres tg
ON tsg.show_id = ts.id AND tsg.genre_id = tg.id AND ts.title = 'Dexter';
