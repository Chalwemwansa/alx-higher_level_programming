-- shows the genres for the title DEXTER
-- demonstrating the use of the SELECT and the join operations
SELECT ts.title
FROM tv_shows ts JOIN tv_show_genres tsg JOIN tv_genres tg
ON tsg.show_id = ts.id AND tsg.genre_id = tg.id AND tg.name = 'Comedy'
ORDER BY ts.title;
