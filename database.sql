CREATE TABLE victim_service_calls(
    call_time DATETIME NOT NULL,
    complaint_type VARCHAR NOT NULL,
    street_name VARCHAR,
    cross_street_name VARCHAR,
    persons_injured INT NOT NULL,
    persons_killed INT NOT NULL,

    PRIMARY KEY(call_time, street_name)
);

CREATE TABLE collision_injuries (
    collision_time DATETIME NOT NULL,
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
    call_time DATETIME NOT NULL,
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
    collision_id INT(10) UNSIGNED NOT NULL,
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
    collision_id INT(10) UNSIGNED NOT NULL,
    collision_date DATE NOT NULL,
    zipcode VARCHAR(5) NOT NULL,
    address_type VARCHAR,
    persons_killed INT NOT NULL,
    persons_injured INT NOT NULL,
    PRIMARY KEY(collision_id)
);
