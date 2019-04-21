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

def query_fn4(location_name, type_index):
    num = 0;
    if(type_index == 1):
        cur.execute("SELECT DISTINCT(num), killed FROM (SELECT crashes_victims.persons_killed AS killed, crashes_victims.id AS num, crashes_location.id, crashes_location.street, crashes_location.crossstreet FROM crashes_location, crashes_victims WHERE crashes_victims.id = crashes_location.id AND (crashes_location.street = %s OR crashes_location.crossstreet = %s) GROUP BY crashes_victims.persons_killed, crashes_victims.id, crashes_location.id, crashes_location.street, crashes_location.crossstreet) as var", (location_name, location_name, ))
        for row in cur.fetchall():
            num += row[1]
        return num
    if(type_index == 2):
        cur.execute("SELECT DISTINCT(num), killed FROM (SELECT crashes_victims.persons_killed AS killed, crashes_victims.id AS num, crashes_location.id, crashes_location.zip FROM crashes_location, crashes_victims WHERE crashes_victims.id = crashes_location.id AND crashes_location.zip = %s GROUP BY crashes_victims.persons_killed, crashes_victims.id, crashes_location.id, crashes_location.zip) as var", (location_name, ))
        for row in cur.fetchall():
            num += row[1]
        return num
    if(type_index == 3):
        cur.execute("SELECT DISTINCT(num), killed FROM (SELECT crashes_victims.persons_killed AS killed, crashes_victims.id AS num, crashes_location.id, crashes_location.boro FROM crashes_location, crashes_victims WHERE crashes_victims.id = crashes_location.id AND crashes_location.boro = %s GROUP BY crashes_victims.persons_killed, crashes_victims.id, crashes_location.id, crashes_location.boro) as var", (location_name, ))
        for row in cur.fetchall():
            num += row[1]
        return num
    return -1

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
