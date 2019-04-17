# NYC-311-Requests-and-Car-Crashes
A collaborative PostgreSQL-oriented final project for the Spring 2019 Database Systems course taught at RPI.

To setup: run Postgres as user postgres and run file `requests_and_crashes_setup.sql`
```
psql -U postgres
\i requests_and_crashes_setup.sql
\q
```

To run:
`python load_data.py`

To check tables if they exist:
```
psql -U requests_and_crashes
\db
\du
\lt
SELECT * FROM <insert table name here>;
\q
```