-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT shows.title, tv_g.name
  FROM tv_shows AS shows
	 LEFT JOIN tv_show_genres AS show_genres
	     ON shows.id = show_genres.show_id
