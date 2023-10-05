-- list all genres not linked to the show Dexter
SELECT DISTINCT name
  FROM tv_genres AS genres
	 INNER JOIN tv_show_genres AS show_genres
	     ON genres.id = show_genres.genre_id
