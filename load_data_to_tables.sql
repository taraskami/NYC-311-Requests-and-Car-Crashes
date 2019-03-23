INSERT INTO victim_service_calls(call_date, call_time, street_name, cross_street_name, persons_injured, persons_killed)
SELECT crashes_tmp.crash_date, crashes_tmp.time, crashes_tmp.street, crashes_tmp.crossstreet, crashes_tmp.persons_injured + crashes_tmp.peds_injured + crashes_tmp.cyclists_killed + crashes_tmp.motorists_injured, crashes_tmp.persons_killed + crashes_tmp.peds_killed + crashes_tmp.cyclists_killed + crashes_tmp.motorists_killed
FROM crashes_tmp
ON CONFLICT (call_date, call_time, street_name)
DO NOTHING;

