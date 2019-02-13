import pytest
from pychat.domain.ports import AbstractUserRepository, UserId
from pychat.domain.models import User

class UserRepository(AbstractUserRepository):

    def __init__(self, session):
        self.items = []

    def add(self, user: User):
        self.items.append(user)

    def get_by_username(self, username: str) -> User:
        return next((item for item in self.items
                            if item.username == username), None)
    
    def _get(self, id: int) -> User:
        return next((item for item in self.items
                            if item.id == id), None)

    def remove(self, user: User):
        self.remove_by_id(user.id)

    def update(self, user: User):
        index = self.items.index(self._get(user.id))
        self.items[index] = user


    def remove_by_id(self, id: UserId):
        self.items.remove(next(item for item in self.items
                                    if item.id == id))

def test_user_repository_add_user_should_add_it():
    repo = UserRepository(None)
    new_user = User('ruben69695', 'Ruben', 'Arrebola de Haro')
    new_user.id = 1 
    repo.add(new_user)
    saved_user = repo.items[0]
    assert saved_user == new_user

def test_user_repository_remove_user_should_remove_it():
    repo = UserRepository(None)
    new_user = User('ruben69695', 'Ruben', 'Arrebola de Haro')
    new_user.id = 1
    repo.items.append(new_user)
    repo.remove(new_user)
    assert len(repo.items) == 0

def test_user_repository_remove_user_by_id_should_remove_it():
    repo = UserRepository(None)
    new_user = User('ruben69695', 'Ruben', 'Arrebola de Haro')
    new_user.id = 1
    repo.items.append(new_user)
    repo.remove_by_id(new_user.id)
    assert len(repo.items) == 0

def test_user_repository_get_user_by_username_should_return_user():
    repo = UserRepository(None)
    new_user = User('ruben69695', 'Ruben', 'Arrebola de Haro')
    new_user.id = 1
    repo.items.append(new_user)
    user = repo.get_by_username('ruben69695')
    assert user == new_user

def test_user_repository_get_user_by_id_should_return_user():
    repo = UserRepository(None)
    new_user = User('ruben69695', 'Ruben', 'Arrebola de Haro')
    new_user.id = 1
    repo.items.append(new_user)
    user = repo.get(1)
    assert user == new_user

def test_user_repository_update_user_should_update():
    repo = UserRepository(None)
    new_user = User('ruben69695', 'Ruben', 'Arrebola de Haro')
    new_user.id = 1
    repo.items.append(new_user)
    new_user.firstname = 'David'
    repo.update(new_user)
    assert repo.items[0].firstname == 'David'

def test_user_repository_get_user_not_found_should_raise_exception():
    repo = UserRepository(None)
    with pytest.raises(Exception) as excp:
        repo.get(1)
    assert 'User not found' == str(excp.value)
    
