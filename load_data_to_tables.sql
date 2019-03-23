-- INSERT INTO victim_service_calls(call_date, call_time, street_name, cross_street_name, persons_injured, persons_killed)
-- SELECT crashes_tmp.crash_date, crashes_tmp.time, crashes_tmp.street, crashes_tmp.crossstreet, crashes_tmp.persons_injured + crashes_tmp.peds_injured + crashes_tmp.cyclists_killed + crashes_tmp.motorists_injured, crashes_tmp.persons_killed + crashes_tmp.peds_killed + crashes_tmp.cyclists_killed + crashes_tmp.motorists_killed
-- FROM crashes_tmp
-- ON CONFLICT (call_date, call_time, street_name)
-- DO NOTHING;

-- INSERT INTO collision_injuries()

INSERT INTO service_calls(open_time, close_time, street_name, complaint_type, descriptor, location_type, call_status)
SELECT requests_tmp.open_date, requests_tmp.close_date, COALESCE(requests_tmp.street,requests_tmp.intersection1, requests_tmp.bridge_highway_name), requests_tmp.complaint_type, requests_tmp.descriptor, requests_tmp.location_type, requests_tmp.status
FROM requests_tmp
ON CONFLICT(open_time, street_name)
DO NOTHING;

INSERT INTO borough_vehicle(collision_id, collision_date, collision_time, borough, vehicle1_type, vehicle2_type, factor_vehicle1, factor_vehicle2)
SELECT crashes_tmp.id, crashes_tmp.crash_date, crashes_tmp.time, crashes_tmp.boro, crashes_tmp.vehicle_type1, crashes_tmp.vehicle_type2, crashes_tmp.contrib_factor1, crashes_tmp.contrib_factor2
FROM crashes_tmp;

INSERT INTO zipcode(request_id, zipcode, borough, longitude, latitude, complaint_type)
SELECT requests_tmp.id, requests_tmp.zip, requests_tmp.boro, requests_tmp.long, requests_tmp.lat, requests_tmp.complaint_type
FROM requests_tmp
WHERE requests_tmp.zip IS NOT NULL;

INSERT INTO victim_zipcode(collision_id, collision_date, collision_time, zipcode, persons_killed, persons_injured)
SELECT crashes_tmp.id, crashes_tmp.crash_date, crashes_tmp.time, crashes_tmp.zip, crashes_tmp.persons_injured + crashes_tmp.peds_injured + crashes_tmp.cyclists_killed + crashes_tmp.motorists_injured, crashes_tmp.persons_killed + crashes_tmp.peds_killed + crashes_tmp.cyclists_killed + crashes_tmp.motorists_killed
FROM crashes_tmp
WHERE crashes_tmp.zip IS NOT NULL;