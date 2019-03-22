DROP DATABASE IF EXISTS requests_and_crashes;
CREATE DATABASE requests_and_crashes;

DROP USER IF EXISTS requests_and_crashes;
CREATE USER requests_and_crashes WITH PASSWORD 'requests_and_crashes';

GRANT ALL PRIVILEGES ON DATABASE requests_and_crashes TO requests_and_crashes;