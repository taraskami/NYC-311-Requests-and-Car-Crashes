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
print "\n" + "\n" + "Welcome to the NYC 311 Requests and Car Crashes application."

while (True):
    if not admin_mode:
        print "What would you like to examine?"
        print """0: [Street Lookup]
1: [Street and Number of Crashes]     2: [Potential Causes of Crashes]
3: [Incident on Specific Highway]     4: [Crash Deaths per Street, ZIP, or Borough]
5: [Number of Crashes vs. Requests in a ZipCode by Date]
6: [Crashes on Street in a Period of Time]
7: [Potential Crashes linked to Complaint Type]
8: [Potential Crashes linked to Complaint Reason]
9: [Crashes Info By ID]               10: [Requests Info By ID]
11: Quit"""

        topic_index = input("Menu Option: ")
        if topic_index == 0:
            print "[Street Lookup]"
            print "Manhattan, Brooklyn, Queens, Bronx, Staten Island"
            boro_name = raw_input("Enter the borough you'd like to search within: ")
            results = query_fn0(boro_name.upper())
            results = sorted(results)
            i = 0
            i_max = 99
            end_of_page = False
            while (not end_of_page):
                for j in range(i, i_max + 1):
                    if j < len(results):
                        print results[j]
                    else:
                        end_of_page = True
                        i_max = j
                        break
                print "---------------"
                print "Showing streets " + str(i+1) + "-" + str(i_max + 1)
                if (end_of_page):
                    print "Enter: Quit lookup"
                    lookup_cmd = raw_input()
                    break
                else:
                    print "N: Next Page\nEnter: Quit lookup"
                    lookup_cmd = raw_input()
                    if (lookup_cmd.upper() == "N"):
                        i += 100
                        i_max += 100
                    else:
                        break

        if topic_index == 1:
            print "[Street and Number of Crashes]"
            street_name = raw_input("Input the street you'd like to examine\nTips: you may have to try variations of spellings for street types (i.e. parkway and pkwy): ")
            if(len(street_name == 0)):
                print "Empty string"
            print "Specify a borough (Optional, may leave blank)"
            boro_name = raw_input()
            result = query_fn1(street_name, boro_name)
            print str(result) + " crashes on this street." + "\n"
            
        if topic_index == 2:
            print "[Potential Causes of Crashes]"
            street_name = raw_input("Input the street you'd like to examine\nTips: you may have to try variations of spellings for street types (i.e. parkway and pkwy): ")
            crossstreet_name = raw_input("Input another cross street: ")
            result = query_fn2(street_name, crossstreet_name)
            print "Cause of Crash: " + "\n" + str(result)

        if topic_index == 3:
            print "[Incident on Specific Highway]"
            hw_name = raw_input("Input the highway you'd like to examine: ")
            result = query_fn3(hw_name)
            print "Incident includes: " + "\n" + str(result) 
            
        if topic_index == 4:
            print "[Crash Deaths per Street, ZIP, or Borough]"
            print """1: [Street]
2: [ZIP]
3: [Borough]"""
            type_index = input("Input Option: ")
            if type_index == 1:
                location_name = raw_input("Input the street you'd like to examine\nTips: you may have to try variations of spellings for street types (i.e. parkway and pkwy): ")
                result = query_fn4(location_name, type_index)
                print str(result) + " deaths on this street."
                continue
            if type_index == 2:
                location_name = raw_input("Input the ZIP you'd like to examine: ")
                result = query_fn4(location_name, type_index)
                print str(result) + " deaths in this ZIP."
                continue
            if type_index == 3:
                location_name = raw_input("Input the borough you'd like to examine: ")
                result = query_fn4(location_name, type_index)
                print str(result) + " deaths in this borough."
                continue
        if topic_index == 5:
            print "[Number of Crashes vs. Number of Requests in a ZipCode by Date]"
            zipcode = raw_input("Input a zipcode: ")
            result = query_fn5(zipcode)
            print str(result)


        if topic_index == 6:
            print "[Crashes on Street in a Period of Time]"
            start_time = raw_input("Input the start time in the form (HH:MM:SS): ")
            end_time = raw_input("Input the end time in the form (HH:MM:SS): ")
            street_name = raw_input("Input the street you'd like to examine\nTips: you may have to try variations of spellings for street types (i.e. parkway and pkwy): ")
            result = query_fn6(start_time, end_time, street_name)
            print str(result) + " crashes on this street between these provided hours over the course of this study." + "\n"

        if topic_index == 7:
            print "[Potential Crashes linked to Complaint Type]"
            start_date = raw_input("Input the start date in the form (YYYY-MM-DD): ")
            end_date = raw_input("Input the end date in the form (YYYY-MM-DD): ")
            complaint = raw_input("Input the complaint type: ")
            result = query_fn7(start_date, end_date, complaint)
            print "Possible incident includes: " + "\n" + str(result)

        if topic_index == 8:
            print "[Potential Crashes linked to Reason Type]"
            start_date = raw_input("Input the start date in the form (YYYY-MM-DD): ")
            end_date = raw_input("Input the end date in the form (YYYY-MM-DD): ")
            complaint = raw_input("Input the reason type: ")
            result = query_fn8(start_date, end_date, complaint)
            print "Possible incident includes: " + "\n" + str(result)

        if topic_index == 9:
            id = raw_input("Input ID: ")
            result = query_fn9(id)
            print str(result)

        if topic_index == 10:
            id = raw_input("Input ID: ")
            result = query_fn10(id)
            print str(result)
        
        if topic_index == 11:
            break
            

        
        if topic_index > 11 or topic_index < 0:
            print "Invalid\n"
