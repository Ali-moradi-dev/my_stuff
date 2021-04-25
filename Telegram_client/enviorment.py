from dotenv import load_dotenv
from os import environ

# load .env to current project environment variables
load_dotenv()


phone = environ.get('PHONE')
api_id = environ.get('API_ID')
api_hash = environ.get('API_HASH')
host = str(environ.get('HOST'))
port = int(environ.get('PORT'))

