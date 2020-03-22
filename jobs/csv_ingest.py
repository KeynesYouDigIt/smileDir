import pandas
from utils.data_ingest import ingest_full


df = pandas.read_csv(
    'x_ca_omcc_providers.csv',
    header = None
)
df.columns = [
        'provider_name', 'type_of_care', 'address', 'city', 
        'state_postal_initials', 'zip', 'phone'
    ]

items_found = df.to_dict('records') 
ingest_full(items_found, 'csv')