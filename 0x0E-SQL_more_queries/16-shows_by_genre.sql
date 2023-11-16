-- shows the genres for the title DEXTER
-- demonstrating the use of the SELECT and the join operations
SELECT ts.title, tg.name
FROM (tv_shows ts LEFT OUTER JOIN tv_show_genres tsg
ON tsg.show_id = ts.id) 
LEFT OUTER JOIN tv_genres tg
ON tsg.genre_id = tg.id
ORDER BY ts.title, tg.name;
