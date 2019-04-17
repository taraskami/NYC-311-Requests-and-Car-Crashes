# For starting application, calling function to populate tables,
# Calling query functions created in database.py, and printing to cmd

import sys
import load_data #Creates tables and populates them.
import database

admin_mode = False #Admin mode lets the user write their own query.
print sys.argv
if len(sys.argv) > 1:
    if sys.argv[1] == "-admin":
        admin_mode = True

if not admin_mode:
    print "Welcome to the NYC 311 Requests and Car Crashes application."
    print "What would you like to examine?"
    print """1: [Street and Number of Crashes]    2: [Potential Causes of Crashes]
3: [Crashes on the Highway]           4: [Crash Deaths per Street, ZIP, or Boro]
5: [Multi-Car Crashes]                6: [Crashes on Street in a Period of Time]
7: [Potential Crashes linked to Complaint Type]
8: [Potential Crashes linked to Complaint Reason]
9: [All Crashes]                      10: [All Requests]"""

    topic_index = input()
    if topic_index == '1':
        print "[Street and Number of Crashes]"
        print "Input the street you'd like to examine"
        print "(Tips: you may have to try variations of spellings for street types (i.e. parkway and pkwy)"
        street_name = input()
    else:
        print "..."
    