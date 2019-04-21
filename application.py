# For starting application, calling function to populate tables,
# Calling query functions created in database.py, and printing to cmd

import sys

admin_mode = False #Admin mode lets the user write their own query.
run_sql = True #If tables are already created, no need to redo each time.
for i in range(len(sys.argv)):
    if sys.argv[i] == "-admin":
        admin_mode = True
    elif sys.argv[i] == "-preinstalled":
        run_sql = False
if run_sql:
    import load_data #Creates tables and populates them.
from database import *
print "Welcome to the NYC 311 Requests and Car Crashes application."
while (True):
    if not admin_mode:
        print "What would you like to examine?"
        print """1: [Street and Number of Crashes]    2: [Potential Causes of Crashes]
    3: [Crashes on the Highway]           4: [Crash Deaths per Street, ZIP, or Borough]
    5: [Multi-Car Crashes]                6: [Crashes on Street in a Period of Time]
    7: [Potential Crashes linked to Complaint Type]
    8: [Potential Crashes linked to Complaint Reason]
    9: [All Crashes]                      10: [All Requests]"""

        topic_index = input("Menu Option: ")
        if topic_index == 1:
            print "[Street and Number of Crashes]"
            street_name = raw_input("Input the street you'd like to examine\nTips: you may have to try variations of spellings for street types (i.e. parkway and pkwy)")
            print "Specify a borough (Optional, may leave blank)"
            boro_name = raw_input()
            result = query_fn1(street_name, boro_name)
            print str(result) + " crashes on this street."
        if topic_index == 2:
            print "[Potential Causes of Crashes]"
            street_name = raw_input("Input the street you'd like to examine\nTips: you may have to try variations of spellings for street types (i.e. parkway and pkwy): ")
            crossstreet_name = raw_input("Input another cross street: ")
            result = query_fn2(street_name, crossstreet_name)
            print "Cause of Crash: " + "\n" + str(result)
        else:
            print "Invalid"
        
