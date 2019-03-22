DROP TABLE IF EXISTS victim_service_calls;
DROP TABLE IF EXISTS collision_injuries;
DROP TABLE IF EXISTS service_calls;
DROP TABLE IF EXISTS borough_vehicle;
DROP TABLE IF EXISTS zipcode;
DROP TABLE IF EXISTS victim_zipcode;

CREATE TEMPORARY TABLE requests_tmp (
    id VARCHAR NOT NULL,
    open_date DATE NOT NULL,
    close_date DATE NOT NULL,
    complaint_type VARCHAR NOT NULL,
    descriptor VARCHAR NOT NULL,
    location_type VARCHAR NOT NULL,
    zip INT NOT NULL,
    address VARCHAR NOT NULL,
    street VARCHAR NOT NULL,
    crossstreet1 VARCHAR NOT NULL,
    crossstreet2 VARCHAR NOT NULL,
    intersection1 VARCHAR NOT NULL,
    intersection2 VARCHAR NOT NULL,
    address_type VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    landmark VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    resoltuion VARCHAR NOT NULL,
    boro VARCHAR NOT NULL,
    x_coord INT NOT NULL,
    y_coord INT NOT NULL,
    bridge_highway_name VARCHAR,
    bridge_highway_direction VARCHAR,
    bridge_road_ramp VARCHAR,
    bridge_highway_segment VARCHAR,
    lat NUMERIC(8, 4) NOT NULL,
    long NUMERIC(8, 4) NOT NULL,
    location VARCHAR NOT NULL
);

CREATE TEMPORARY TABLE crashes_tmp (
    crash_date DATE NOT NULL,
    time TIME NOT NULL,
    boro VARCHAR NOT NULL,
    zip INT NOT NULL,
    lat NUMERIC(8, 4),
    long NUMERIC(8, 4),
    location VARCHAR NOT NULL,
    street VARCHAR NOT NULL,
    crossstreet VARCHAR NOT NULL,
    offstreet VARCHAR NOT NULL,
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

CREATE TABLE victim_service_calls(
    call_time DATE NOT NULL,
    complaint_type VARCHAR NOT NULL,
    street_name VARCHAR,
    cross_street_name VARCHAR,
    persons_injured INT NOT NULL,
    persons_killed INT NOT NULL,

    PRIMARY KEY(call_time, street_name)
);

CREATE TABLE collision_injuries (
    collision_time DATE NOT NULL,
    street_name VARCHAR,
    persons_injured INT NOT NULL,
    persons_killed INT NOT NULL,
    factor_vehicle1 VARCHAR NOT NULL,
    factor_vehicle2 VARCHAR,
    vehicle1_type VARCHAR NOT NULL,
    vehicle2_type VARCHAR,
    PRIMARY KEY(collision_time, street_name)
);

CREATE TABLE service_calls (
    call_time DATE NOT NULL,
    street_name VARCHAR ,
    complaint_type VARCHAR NOT NULL,
    descriptor VARCHAR NOT NULL,
    location_type VARCHAR,
    resolution VARCHAR NOT NULL,
    channel_type VARCHAR NOT NULL,
    call_status VARCHAR NOT NULL,
    PRIMARY KEY(call_time, street_name)
);

CREATE TABLE borough_vehicle (
    collision_id INT NOT NULL,
    collision_date DATE,
    borough VARCHAR(15),
    vehicle1_type VARCHAR NOT NULL,
    vehicle2_type VARCHAR,
    factor_vehicle1 VARCHAR NOT NULL,
    factor_vehicle2 VARCHAR,
    PRIMARY KEY(collision_id)
);

CREATE TABLE zipcode (
    zipcode VARCHAR(5) NOT NULL,
    borough VARCHAR(15) NOT NULL,
    longitude VARCHAR NOT NULL,
    latitude VARCHAR NOT NULL,
    _location VARCHAR NOT NULL,
    complaint_type VARCHAR NOT NULL,
    PRIMARY KEY(longitude, latitude)
);

CREATE TABLE victim_zipcode (
    collision_id INT NOT NULL,
    collision_date DATE NOT NULL,
    zipcode VARCHAR(5) NOT NULL,
    address_type VARCHAR,
    persons_killed INT NOT NULL,
    persons_injured INT NOT NULL,
    PRIMARY KEY(collision_id)
);
