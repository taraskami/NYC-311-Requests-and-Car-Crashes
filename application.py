# For starting application, calling function to populate tables,
# Calling query functions created in database.py, and printing to cmd

import sys
import load_data #Creates tables and populates them.

admin_mode = False #Admin mode lets the user write their own query.
print sys.argv
if len(sys.argv) > 1:
    if sys.argv[1] == "-admin":
        admin_mode = True

if not admin_mode:
    print "Welcome to the NYC 311 Requests and Car Crashes application."
    print "Would you like to examine crashes' location (1), time (2), contributing factor (3), or vehicle type (4)?"
    crashes_detail = input()
    