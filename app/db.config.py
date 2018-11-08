import psycopg2
import os

host = '127.0.0.1'
user = 'Postgres'
db_name = 'SendIt'
password = 'anyPaSSWOrrd'
port = 5432

url = os.getenv('DATABASE_URL')
con = psycopg2.connect(url)

# cursor
cur = con.cursor()
