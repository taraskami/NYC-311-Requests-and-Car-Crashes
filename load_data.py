import psycopg2
conn = psycopg2.connect("host=localhost dbname=requests_and_crashes user=requests_and_crashes")
cur = conn.cursor()

with open('311_Service_Requests_from_2010_to_Present.csv', 'r') as f:
    next(f)
    cur.copy_from(f, '', sep=',')