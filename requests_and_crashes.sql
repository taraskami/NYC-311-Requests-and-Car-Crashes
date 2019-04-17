-- Creating tables that will be populated by load_data_to_tables, called by load_data.py

DROP TABLE IF EXISTS crashes;
DROP TABLE IF EXISTS crashes_location;
DROP TABLE IF EXISTS crashes_victims;
DROP TABLE IF EXISTS requests;
DROP TABLE IF EXISTS requests_location;
DROP TABLE IF EXISTS requests_highways;

CREATE TEMPORARY TABLE requests_tmp (
    id INT NOT NULL,
    open_date TIMESTAMP NOT NULL,
    close_date TIMESTAMP,
    complaint_type VARCHAR NOT NULL,
    descriptor VARCHAR NOT NULL,
    location_type VARCHAR,
    zip INT,
    address VARCHAR,
    street VARCHAR,
    crossstreet1 VARCHAR,
    crossstreet2 VARCHAR,
    intersection1 VARCHAR,
    intersection2 VARCHAR,
    address_type VARCHAR,
    city VARCHAR,
    landmark VARCHAR,
    status VARCHAR,
    boro VARCHAR NOT NULL,
    x_coord INT,
    y_coord INT,
    bridge_highway_name VARCHAR,
    bridge_highway_direction VARCHAR,
    bridge_road_ramp VARCHAR,
    bridge_highway_segment VARCHAR,
    lat NUMERIC(8, 4),
    long NUMERIC(8, 4)
);

CREATE TEMPORARY TABLE crashes_tmp (
    crash_date DATE NOT NULL,
    time TIME NOT NULL,
    boro VARCHAR NOT NULL,
    zip INT,
    lat NUMERIC(8, 4),
    long NUMERIC(8, 4),
    street VARCHAR NOT NULL,
    crossstreet VARCHAR NOT NULL,
    persons_injured INT NOT NULL,
    persons_killed INT NOT NULL,
    peds_injured INT NOT NULL,
    peds_killed INT NOT NULL,
    cyclists_injured INT NOT NULL,
    cyclists_killed INT NOT NULL,
    motorists_injured INT NOT NULL,
    motorists_killed INT NOT NULL,
    contrib_factor1 VARCHAR,
    contrib_factor2 VARCHAR,
    contrib_factor3 VARCHAR,
    contrib_factor4 VARCHAR,
    contrib_factor5 VARCHAR,
    id INT NOT NULL,
    vehicle_type1 VARCHAR,
    vehicle_type2 VARCHAR,
    vehicle_type3 VARCHAR,
    vehicle_type4 VARCHAR,
    vehicle_type5 VARCHAR
);

CREATE TABLE crashes(
    id INT NOT NULL,
    crash_date DATE NOT NULL,
    crash_time TIME NOT NULL,
    contrib_factor1 VARCHAR,
    contrib_factor2 VARCHAR,
    vehicle_type1 VARCHAR,
    vehicle_type2 VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE crashes_location(
    id INT NOT NULL,
    boro VARCHAR NOT NULL,
    zip INT,
    lat NUMERIC(8, 4),
    long NUMERIC(8, 4),
    street VARCHAR NOT NULL,
    crossstreet VARCHAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE crashes_victims(
    id INT NOT NULL,
    persons_killed INT NOT NULL,
    persons_injured INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE requests(
    id INT NOT NULL,
    open_date TIMESTAMP NOT NULL,
    close_date TIMESTAMP,
    complaint_type VARCHAR NOT NULL,
    descriptor VARCHAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE requests_location(
    id INT NOT NULL,
    location_type VARCHAR,
    zip INT,
    address VARCHAR,
    address_type VARCHAR,
    city VARCHAR,
    landmark VARCHAR,
    boro VARCHAR,
    lat NUMERIC(8, 4),
    long NUMERIC(8, 4),
    street VARCHAR,
    crossstreet1 VARCHAR,
    crossstreet2 VARCHAR,
    intersection1 VARCHAR,
    intersection2 VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE requests_highways(
    id INT NOT NULL,
    bridge_highway_name VARCHAR,
    bridge_road_ramp VARCHAR,
    bridge_highway_segment VARCHAR,
    PRIMARY KEY (id)
);