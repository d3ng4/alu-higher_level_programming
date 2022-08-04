-- Import the database dump from hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_show_genres.show_id = tv_show.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.titles ASC, tv_show_genres.genre_id ASC;
