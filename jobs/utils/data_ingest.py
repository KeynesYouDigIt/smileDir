from db_connect.db_connection import execute_sql

# result = execute_sql('select * from provider_contact;')
# for r in result:
#     print(r)

def is_duplicate(phone_number):
    result = execute_sql(
        'SELECT count(*) FROM provider_contact WHERE phone = :phone_number',
        phone_number=parse_phone(phone_number)
    )

    return result.first()[0] > 0

def add_data(data, state_postal_initials):
    result = execute_sql(
            'INSERT INTO provider_contact (provider_name, phone, email, type_of_care, address, city, state_postal_initials, zip)' +
            'VALUES(:provider_name, :phone, :email, :type_of_care, :address, :city, :state_postal_initials, :zip)', 
            provider_name=data['provider_name'], 
            phone=parse_phone(data['phone']),
            email=data['email'], 
            type_of_care=safe_field_get('type_of_care', data), 
            address=safe_field_get('address', data), 
            city=safe_field_get('city', data),
            # assuming the data can be organized by state, would like to not do that at some point.
            state_postal_initials=state_postal_initials,
            # the data comes in with this key, but its a python built in. Maybe tune up if possible.
            zip=safe_field_get('zip', data), 
    )

    return result

def safe_field_get(field_name, data):
    if field_name in data:
        return data[field_name]
    return None

def parse_phone(phone):
    return phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')