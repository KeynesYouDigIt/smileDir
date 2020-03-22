from db_connect.db_connection import connection

result = connection.execute('select * from provider_contact;')
for r in result:
    print(r)
