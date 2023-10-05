-- list all genres not linked to the show Dexter
SELECT DISTINCT name
  FROM tv_genres AS genres
	 INNER JOIN tv_show_genres AS show_genres
	     ON genres.id = show_genres.genre_id
	INNER JOIN tv_shows AS shows ON shows.id = show_genres.show_id
WHERE genres.name NOT IN (
	SELECT DISTINCT name FROM tv_genres AS genres
	INNER JOIN tv_show_genres AS show_genres ON show_genres.genre_id = genres.id
	INNER JOIN tv_shows AS shows ON shows.id = show_genres.show_id
	WHERE title = 'Dexter')
ORDER BY name;
