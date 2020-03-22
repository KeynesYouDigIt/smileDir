from db_connect.db_connection import execute_sql
import json

def is_duplicate(phone_number):
    result = execute_sql(
        'SELECT count(*) FROM provider_contact WHERE phone = :phone_number',
        phone_number=parse_phone(phone_number)
    )

    return result.first()[0] > 0

def add_data(data, state_postal_initials):
    result = execute_sql(
            'INSERT INTO provider_contact (provider_name, phone, email, type_of_care, address, city, state_postal_initials, zip) ' +
            'VALUES(:provider_name, :phone, :email, :type_of_care, :address, :city, :state_postal_initials, :zip) '+
            'ON CONFLICT (phone) DO UPDATE SET provider_name = EXCLUDED.provider_name, ' +
                    'phone = EXCLUDED.phone, ' +
                    'email = EXCLUDED.email, ' +
                    'type_of_care = EXCLUDED.type_of_care, '+
                    'address = EXCLUDED.address, ' +
                    'city = EXCLUDED.city, ' +
                    'state_postal_initials = EXCLUDED.state_postal_initials, ' +
                    'zip = EXCLUDED.zip;', 
            provider_name=str(data['provider_name']), 
            phone=parse_phone(data['phone']),
            email=safe_field_get('email', data), 
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
        return str(data[field_name])
    return None

def parse_phone(phone):
    phone=str(phone)
    return phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

def ingest_full(items_found, source_name):
    print('ITEMS FOUND at '+ source_name)
    print(len(items_found))
    error_file_name = 'errors_' + source_name + '.json'
    with open(error_file_name, 'w+') as fp:
        fp.write(json.dumps({}))

    duplicates_found = 0
    for item in items_found:
        # TODO - theres certainly a way to dedup incoming data in memory 
        # by comparing different sources in memory. We should do that instead
        # of constantly clanging against the db.
        if item and 'phone' in item:
            if is_duplicate(item['phone']):
                duplicates_found += 1
            try:
                # just assuming everythings California to get this finished,
                # NOT a safe/long term assumption.
                add_data(item, 'CA')
            except Exception as e:
                with open(error_file_name,'a+') as fp:
                    item['error_message'] = str(e)
                    fp.write(json.dumps(item))

    print('duplicates found and updated')
    print(duplicates_found)