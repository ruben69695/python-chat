import urllib.parse

def get_postgres_uri_engine(user, password, host, port, databaseName):
    password = urllib.parse.quote_plus(password)
    return f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{databaseName}'

def get_sqlite_uri_engine(databasename):
    return f'sqlite:///{databasename}.db'