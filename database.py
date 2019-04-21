import psycopg2
conn = psycopg2.connect("host=localhost dbname=requests_and_crashes user=requests_and_crashes password = requests_and_crashes ")
cur = conn.cursor()

# Functions to query data
def query_fn1(street_name, boro_name):
    cur.execute("SELECT COUNT(*) FROM crashes_location WHERE street = %s OR crossstreet = %s", (street_name, street_name, ))
    result = cur.fetchall()
    return result[0][0]

def query_fn2(street_name, crossstreet_name):
    cur.execute("SELECT cause1, cause2 FROM (SELECT crashes.id, crashes.contrib_factor1 AS cause1, crashes.contrib_factor2 as cause2, crashes_location.street, crashes_location.crossstreet, crashes_location.id FROM crashes, crashes_location WHERE crashes.id = crashes_location.id GROUP BY crashes.id, crashes.contrib_factor1, crashes.contrib_factor2, crashes_location.street, crashes_location.crossstreet, crashes_location.id) AS var WHERE var.street = %s OR var.crossstreet = %s", (street_name, crossstreet_name, ))
    str = ""
    for row in cur.fetchall():
        str = str + "A possible cause is " + row[0] + " (and) " + row[1] + "\n"
    return str

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
