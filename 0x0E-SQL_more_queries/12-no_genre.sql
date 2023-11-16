-- script selects shows that have atlease one genre
-- from a dump file
SELECT ts.title, tsg.genre_id
FROM tv_shows ts LEFT OUTER JOIN tv_show_genres tsg
ON tsg.show_id = ts.id
where tsg.show_id IS NULL
ORDER BY ts.title;
