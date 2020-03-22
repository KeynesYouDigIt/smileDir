from db_connect.db_connection import execute_sql

# result = execute_sql('select * from provider_contact;')
# for r in result:
#     print(r)

def is_duplicate(phone_number):
    result = execute_sql(
        'SELECT count(*) FROM provider_contact WHERE phone = :phone_number',
        phone_number=phone_number
    )

    return result.first()[0] > 0
