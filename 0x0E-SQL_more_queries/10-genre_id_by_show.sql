-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows, tv_show_genres
  WHERE tv_show_genres.show_id = tv_shows.id
  GROUP BY tv_shows.title, tv_show_genres.genre_id;
