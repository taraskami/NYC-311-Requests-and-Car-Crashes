INSERT INTO crashes(id, crash_date, crash_time, contrib_factor1, contrib_factor2, vehicle_type1, vehicle_type2)
SELECT crashes_tmp.id, crashes_tmp.crash_date, crashes_tmp.time, UPPER(crashes_tmp.contrib_factor1), UPPER(crashes_tmp.contrib_factor2), UPPER(crashes_tmp.vehicle_type1), UPPER(crashes_tmp.vehicle_type2)
FROM crashes_tmp
ON CONFLICT(id)
DO NOTHING;

INSERT INTO crashes_location(id, boro, zip, lat, long, street, crossstreet)
SELECT crashes_tmp.id, UPPER(crashes_tmp.boro), crashes_tmp.zip, crashes_tmp.lat, crashes_tmp.long, UPPER(crashes_tmp.street), UPPER(crashes_tmp.crossstreet)
FROM crashes_tmp
ON CONFLICT(id)
DO NOTHING;

INSERT INTO crashes_victims(id, persons_injured, persons_killed)
SELECT crashes_tmp.id, crashes_tmp.persons_injured + crashes_tmp.peds_injured + crashes_tmp.cyclists_injured + crashes_tmp.motorists_injured, crashes_tmp.persons_killed + crashes_tmp.peds_killed + crashes_tmp.cyclists_killed + crashes_tmp.motorists_killed
FROM crashes_tmp
ON CONFLICT(id)
DO NOTHING;

INSERT INTO requests(id, open_date, close_date, complaint_type, descriptor)
SELECT requests_tmp.id, requests_tmp.open_date, requests_tmp.close_date, UPPER(requests_tmp.complaint_type), UPPER(requests_tmp.descriptor)
FROM requests_tmp
ON CONFLICT(id)
DO NOTHING;

INSERT INTO requests_location(id, location_type, zip, address, address_type, city, landmark, boro, lat, long, street, crossstreet1, crossstreet2, intersection1, intersection2)
SELECT requests_tmp.id, UPPER(requests_tmp.location_type), requests_tmp.zip, UPPER(requests_tmp.address), UPPER(requests_tmp.address_type), UPPER(requests_tmp.city), UPPER(requests_tmp.landmark), UPPER(requests_tmp.boro), requests_tmp.lat, requests_tmp.long, UPPER(requests_tmp.street), UPPER(requests_tmp.crossstreet1), UPPER(requests_tmp.crossstreet2), UPPER(requests_tmp.intersection1), UPPER(requests_tmp.intersection2)
FROM requests_tmp
ON CONFLICT(id)
DO NOTHING;

INSERT INTO requests_highways(id, bridge_highway_name, bridge_road_ramp, bridge_highway_segment)
SELECT requests_tmp.id, UPPER(requests_tmp.bridge_highway_name), UPPER(requests_tmp.bridge_road_ramp), UPPER(requests_tmp.bridge_highway_segment)
FROM requests_tmp
WHERE (requests_tmp.bridge_highway_name = '') IS FALSE
OR (requests_tmp.bridge_road_ramp = '') IS FALSE
OR (requests_tmp.bridge_highway_segment =  '') IS FALSE
ON CONFLICT(id)
DO NOTHING;
