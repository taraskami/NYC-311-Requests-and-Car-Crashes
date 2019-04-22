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

def query_fn3(hw_name):
    cur.execute("SELECT DISTINCT(complaints) FROM (SELECT requests_highways.id, requests_highways.bridge_highway_name, requests.id, requests.complaint_type AS complaints FROM requests_highways, requests WHERE requests_highways.id = requests.id AND requests_highways.bridge_highway_name = 'Belt Pkwy' GROUP BY requests_highways.id, requests_highways.bridge_highway_name, requests.id, requests.complaint_type) as var", (hw_name))
    str = ""
    for row in cur.fetchall():
        str = str + "-" + row[0] + "\n"
    return str

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

def query_fn5(zipcode):
    st = ""
    crashes = 0
    requests = 0
    # cur.execute("SELECT crash_date, count(DISTINCT crashes_id), count(DISTINCT requests_id) FROM (SELECT crashes.id AS crashes_id, crash_date FROM crashes, crashes_location WHERE crashes.id = crashes_location.id AND crashes_location.zip = %s GROUP BY crashes.id ) as a1, (SELECT requests.id AS requests_id, open_date FROM requests, requests_location WHERE requests.id = requests_location.id AND requests_location.zip = %s GROUP BY requests.id) as a2 GROUP BY crash_date", (zipcode, zipcode, ))
    cur.execute("SELECT DISTINCT(crash_date), num_crashes, num_requests FROM (SELECT DATE(crash_date) as crash_date, count(DISTINCT crashes.id) as num_crashes FROM crashes, crashes_location WHERE crashes.id = crashes_location.id AND crashes_location.zip = %s GROUP BY crash_date) as a1 NATURAL JOIN (SELECT DATE(open_date) as open_date, count(DISTINCT requests.id) as num_requests FROM requests, requests_location WHERE requests.id = requests_location.id AND requests_location.zip = %s GROUP BY open_date) as a2", (zipcode, zipcode, ))
    for row in cur.fetchall():
        st = st + "-" + str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " \n"
        crashes= crashes + row[1]
        requests= requests + row[2]
    st = st + "crashes: " + str(crashes) + " requests: " + str(requests)
    return st

def query_fn6(start_time, end_time, street_name):
    cur.execute("SELECT count(DISTINCT num) FROM (SELECT crashes.crash_time, crashes.id AS num, crashes_location.id, crashes_location.street, crashes_location.crossstreet FROM crashes_location, crashes WHERE crashes_location.id = crashes.id AND crashes.crash_time >= '09:00:00' AND crashes.crash_time <= '10:00:00' AND (crashes_location.street = 'ALBEMARLE ROAD' OR crashes_location.crossstreet = 'ALBEMARLE ROAD') GROUP BY crashes.crash_time, crashes.id, crashes_location.id, crashes_location.street, crashes_location.crossstreet) as var", (start_time, end_time, street_name, street_name, ))
    result = cur.fetchall()
    return result[0][0]

def query_fn7(start_date, end_date, complaint):
    cur.execute("SELECT location, crosslocation FROM (SELECT requests.open_date, requests.close_date, requests.complaint_type, crashes.crash_date, crashes.id, crashes_location.id, crashes_location.street AS location, crashes_location.crossstreet AS crosslocation FROM requests, crashes_location, crashes WHERE (DATE(crashes.crash_date) BETWEEN DATE(%s) AND DATE(%s)) AND (DATE(crashes.crash_date) BETWEEN DATE(requests.open_date) AND DATE(requests.close_date)) AND requests.complaint_type = %s AND crashes_location.id = crashes.id GROUP BY requests.open_date, requests.close_date, requests.complaint_type, crashes.crash_date, crashes.id, crashes_location.id, crashes_location.street, crashes_location.crossstreet) AS var LIMIT 10", (start_date, end_date, complaint, ))
    str = ""
    for row in cur.fetchall():
        str = str + "At " + row[0] + " (and) " + row[1] +  "\n"
    return str

def query_fn8(start_date, end_date, descriptor):
    cur.execute("SELECT location, crosslocation FROM (SELECT requests.open_date, requests.close_date, requests.descriptor, crashes.crash_date, crashes.id, crashes_location.id, crashes_location.street AS location, crashes_location.crossstreet AS crosslocation FROM requests, crashes_location, crashes WHERE (DATE(crashes.crash_date) BETWEEN DATE(%s) AND DATE(%s)) AND (DATE(crashes.crash_date) BETWEEN DATE(requests.open_date) AND DATE(requests.close_date)) AND requests.descriptor = %s AND crashes_location.id = crashes.id GROUP BY requests.open_date, requests.close_date, requests.descriptor, crashes.crash_date, crashes.id, crashes_location.id, crashes_location.street, crashes_location.crossstreet) AS var LIMIT 10", (start_date, end_date, descriptor, ))
    str = ""
    for row in cur.fetchall():
        str = str + "At " + row[0] + " (and) " + row[1] +  "\n"
    return str

def query_fn9(id):
    cur.execute("SELECT * FROM crashes NATURAL JOIN crashes_location WHERE crashes.id = %s", (id, ))
    result = cur.fetchall()
    var = ("Date: " + str(result[0][1]) + "\n"
              "Time: " + str(result[0][2]) + "\n"
              "Cause 1: " + str(result[0][3]) + "\n"
              "Cause 2: " + str(result[0][4]) + "\n"
              "Vehicle 1: " + str(result[0][5]) + "\n"
              "Vehicle 2: " + str(result[0][6]) + "\n"
              "Street: " + str(result[0][11]) + "\n"
              "Cross street: " + str(result[0][12]) + "\n")
    return var

def query_fn10(id):
    cur.execute("SELECT * FROM requests NATURAL JOIN requests_location WHERE requests.id = %s", (id, ))
    result = cur.fetchall()
    var = ("Open Date: " + str(result[0][1]) + "\n"
           "Close Date: " + str(result[0][2]) + "\n"
           "Complaint Type: " + str(result[0][3]) + "\n"
           "Descriptor: " + str(result[0][4]) + "\n"
           "Street: " + str(result[0][17]) + "\n"
           "Cross street: " + str(result[0][18]) + "\n")
    return var
