import os


# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my-secret-key')
    DEBUG = True


key = Config.SECRET_KEY
