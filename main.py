import psycopg2

username = 'postgres'
password = '110603'
database = 'Shapovalov_Lab2'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT production_name, COUNT(shows.show_id) 
FROM (Production JOIN shows ON shows.production_id = Production.production_id) GROUP BY production_name
'''

query_2 = '''
SELECT genre_name, COUNT(shows.show_id) 
FROM (Genres JOIN shows ON shows.genre_id = genres.genre_id) GROUP BY genre_name
'''

query_3 = '''
SELECT release_year, COUNT(shows.show_id) FROM shows GROUP BY release_year ORDER BY release_year
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_1)
    print("Кількість фільмів кожної країни")
    for row in cur:
        print(row)

    cur = conn.cursor()
    cur.execute(query_2)
    print("Частка фільмів кожного жанру")
    for row in cur:
        print(row)

    print("Кількість фільмів за роком випуску")
    cur = conn.cursor()
    cur.execute(query_3)
    for row in cur:
        print(row)