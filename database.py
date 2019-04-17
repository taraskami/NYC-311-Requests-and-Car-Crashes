import psycopg2
conn = psycopg2.connect("host=localhost dbname=requests_and_crashes user=requests_and_crashes password = requests_and_crashes ")
cur = conn.cursor()

# Functions to query data
def query_fn1(street_name, boro_name):
    cur.execute("SELECT COUNT(*) FROM crashes_location WHERE street = %s OR crossstreet = %s", (street_name, street_name, ))
    result = cur.fetchall()
    return result[0][0]

def query_fn2():
    return

def query_fn3():
    return

def query_fn4():
    return

def query_fn5():
    return

def query_fn6():
    return

def query_fn7():
    return

def query_fn8():
    return

def query_fn9():
    return

def query_fn10():
    return
