-- lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`
SELECT DISTINCT title
  FROM tv_shows AS shows
	 LEFT JOIN tv_show_genres AS show_genres
	     ON show_genres.show_id = shows.id
	ORDER BY title;
