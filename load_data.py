import psycopg2
conn = psycopg2.connect("host=localhost dbname=requests_and_crashes user=requests_and_crashes password = requests_and_crashes ")
cur = conn.cursor()

print "Creating tables..."

cur.execute(open("requests_and_crashes.sql", "r").read())

print "Populating data..."

with open('data/311_Service_Requests_from_2010_to_Present.csv', 'r') as f:
    f.readline()
    cur.copy_from(f, 'requests_tmp', sep=',')

with open('data/NYPD_Motor_Vehicle_Collisions.csv', 'r') as f:
    f.readline()
    cur.copy_from(f, 'crashes_tmp', sep=',')

cur.execute(open("load_data_to_tables.sql", "r").read())

print "All done."

conn.commit()