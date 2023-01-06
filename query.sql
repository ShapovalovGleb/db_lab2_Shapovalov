--6a) Кількість фільмів кожної країни
SELECT production_name, COUNT(shows.show_id) 
FROM (Production JOIN shows ON shows.production_id = Production.production_id) GROUP BY production_name
--6b) Частка фільмів кожного жанру
SELECT genre_name, COUNT(shows.show_id) 
FROM (Genres JOIN shows ON shows.genre_id = genres.genre_id) GROUP BY genre_name
--6c) Кількість фільмів за роком випуску
SELECT release_year, COUNT(shows.show_id) FROM shows GROUP BY release_year ORDER BY release_year