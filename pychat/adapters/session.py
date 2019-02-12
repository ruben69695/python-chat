import urllib.parse
from pychat.domain.models import User
from pychat.domain.ports import AbstractUserRepository
import orm

def get_sqlite_uri_engine(databasename):
    return f'sqlite:///{databasename}.db'

def get_postgres_uri_engine(user, password, host, port, databaseName):
    password = urllib.parse.quote_plus(password)
    return f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{databaseName}'


if __name__ == "__main__":
    uri_engine = get_postgres_uri_engine('rubenarrebola', 'ruben123', '127.0.0.1', '5432', 'pychat')
    sqlorm = orm.SQLAlchemy(uri_engine)
    sqlorm.recreate_schema()

    uow = sqlorm.start_unit_of_work()
    uow.__enter__()
    user = uow.users
    new_user = User('ruben69695', 'Ruben', 'Arrebola')
    user.add(new_user)
    uow.commit()


