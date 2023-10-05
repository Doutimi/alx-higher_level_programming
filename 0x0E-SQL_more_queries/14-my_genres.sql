-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
  FROM tv_genres AS tv_genres
	 INNER JOIN tv_show_genres AS tv_show_genres
	     ON tv_genres.id = tv_show_genres.genre_id
