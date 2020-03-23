from db_connect.db_connection import execute_sql

print('be sure you have run data ingestion before running reports!')

print('I have found')
print(execute_sql('SELECT count(*) FROM provider_contact').first()[0])
print('records.')

print('here is a count by zip code')
zips_fetch = execute_sql('SELECT DISTINCT zip FROM provider_contact').fetchall()
zips = [z[0] for z in zips_fetch]

for zp in zips:
    print(zp)
    print(execute_sql('SELECT count(*) FROM provider_contact WHERE zip=:zip', zip=zp).first())