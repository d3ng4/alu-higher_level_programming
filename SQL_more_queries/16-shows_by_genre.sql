-- t lists all shows, and all genres linked to that show, from the database
SELECT s.title, g.name
FROM tv_shows 
LEFT JOIN tv_show_genres m ON s.id = m.show_id
LEFT JOIN tv_genres g ON m.genre_id = g.id
ORDER BY s.title ASC;
