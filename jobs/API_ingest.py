import requests as rq
from utils.data_ingest import ingest_full


response = rq.get('https://bw-interviews.herokuapp.com/data/providers')
items_found = response.json()['providers']

ingest_full(items_found, 'API')