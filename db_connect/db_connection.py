import os
from sqlalchemy import create_engine

# read vital database vars from .env
settings = {
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT'],
    'NAME': os.environ['POSTGRES_DB'],
    'USER': os.environ['POSTGRES_USER'],
    'PASSWORD': os.environ['POSTGRES_PASSWORD'],
}

INITIAL_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{name}'.format(
    user=settings['USER'],
    pw=settings['PASSWORD'],
    url=settings['HOST'] + ':' + settings['PORT'],
    name=settings['NAME']
)

connection = create_engine(INITIAL_URL).connect()
