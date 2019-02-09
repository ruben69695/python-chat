from sqlalchemy import create_engine
import urllib.parse


def get_postgres_engine(user, password, host, port, databaseName):
    password = urllib.parse.quote_plus(password)
    return create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{databaseName}', echo=True)

def get_sqlite_engine(user, password, host, port, databaseName):
    return create_engine('sqlite:///testdb.db', echo=True)