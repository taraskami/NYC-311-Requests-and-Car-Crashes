# Filters placed on the data stored in CSV format

## NYPD Motor Vehicle Collisions
* DATE is between 09/01/2018 and 12/31/2018
    * Too much data in dataset, have to reduce to 4-month period

## 311 Service Requests from 2010 to Present
* Created Date is between 09/01/2018 12:00:00 AM and 12/31/2018 12:00:00 AM
    * Too much data in dataset, have to reduce to 4-month period
* Agency is "DOT"
    * The auto incidents being examined are those caused by road and area conditions i.e. traffic signals, potholes. Department of Transportation documents these. While it would be nice to examine what NYPD complaints are, doing NYPD and DOT would be 300k+ rows of data, which is too much.