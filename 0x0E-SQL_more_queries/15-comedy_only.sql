-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT tv_shows.title
  FROM tv_shows
  JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  JOIN tv_genres
  ON tv_genres.id = tv_show_genres.genre_id
  WHERE tv_genres.name = "Comedy"
  ORDER BY tv_shows.title ASC;
