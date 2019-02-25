CREATE TABLE auto_incident (
    -- Put attributes here 
);

CREATE TABLE three_one_one_request (
    -- Put attributes here
);

-- This is one way I see of creating a table. Could also look at how it's done for baseball data in HW3
-- COPY auto_incident( Put attributes here )
-- FROM 'NYPD_Motor_Vehicle_Collisions.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE collision_injuries (
    collision_time DATETIME NOT NULL,
    street_name VARCHAR,
    persons_injured INT NOT NULL,
    persons_killed INT NOT NULL,
    factor_vehicle1 VARCHAR NOT NULL,
    factor_vehicle2 VARCHAR,
    vehicle1_type VARCHAR NOT NULL,
    vehicle2_type VARCHAR
);

CREATE TABLE service_calls (
    call_time DATETIME NOT NULL,
    street_name VARCHAR ,
    complaint_type VARCHAR NOT NULL,
    descriptor VARCHAR NOT NULL,
    location_type VARCHAR,
    resolution VARCHAR NOT NULL,
    channel_type VARCHAR NOT NULL,
    status VARCHAR NOT NULL
);

CREATE TABLE borough_vehicle (
    collision_date DATE,
    borough VARCHAR(15),
    vehicle1_type VARCHAR NOT NULL,
    vehicle2_type VARCHAR,
    factor_vehicle1 VARCHAR NOT NULL,
    factor_vehicle2 VARCHAR
);