DROP TABLE IF EXISTS victim_service_calls;
DROP TABLE IF EXISTS collision_injuries;
DROP TABLE IF EXISTS service_calls;
DROP TABLE IF EXISTS borough_vehicle;
DROP TABLE IF EXISTS zipcode;
DROP TABLE IF EXISTS victim_zipcode;

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

-- CREATE TABLE victim_service_calls(
--     call_date DATE NOT NULL,
--     call_time TIME NOT NULL,
--     street_name VARCHAR,
--     cross_street_name VARCHAR,
--     persons_injured INT NOT NULL,
--     persons_killed INT NOT NULL,
--     PRIMARY KEY(call_date, call_time, street_name)
-- );


CREATE TABLE service_calls (
    open_time DATE NOT NULL,
    close_time DATE,
    street_name VARCHAR,
    complaint_type VARCHAR NOT NULL,
    descriptor VARCHAR NOT NULL,
    location_type VARCHAR,
    call_status VARCHAR NOT NULL,
    PRIMARY KEY(open_time, street_name)
);

CREATE TABLE borough_vehicle (
    collision_id INT NOT NULL,
    collision_date DATE,
    collision_time TIME,
    borough VARCHAR(15),
    vehicle1_type VARCHAR NOT NULL,
    vehicle2_type VARCHAR,
    factor_vehicle1 VARCHAR NOT NULL,
    factor_vehicle2 VARCHAR,
    PRIMARY KEY(collision_id)
);

CREATE TABLE zipcode (
    request_id INT NOT NULL,
    zipcode VARCHAR(5) NOT NULL,
    borough VARCHAR(15) NOT NULL,
    longitude VARCHAR,
    latitude VARCHAR,
    complaint_type VARCHAR NOT NULL,
    PRIMARY KEY(request_id)
);

CREATE TABLE victim_zipcode (
    collision_id INT NOT NULL,
    collision_date DATE NOT NULL,
    collision_time TIME NOT NULL,
    zipcode VARCHAR(5) NOT NULL,
    address_type VARCHAR,
    persons_killed INT NOT NULL,
    persons_injured INT NOT NULL,
    PRIMARY KEY(collision_id)
);
