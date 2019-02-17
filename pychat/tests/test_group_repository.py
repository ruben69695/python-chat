import pytest
from pychat.domain.ports import AbstractGroupRepository, GroupId
from pychat.domain.models import Group

class GroupRepository(AbstractGroupRepository):

    def __init__(self, session):
        self.items = []

    def add(self, group: Group):
        self.items.append(group)
    
    def _get(self, id: int) -> Group:
        return next((item for item in self.items
                            if item.id == id), None)

    def remove(self, group: Group):
        self.remove_by_id(group.id)

    def update(self, group: Group):
        index = self.items.index(self._get(group.id))
        self.items[index] = group


    def remove_by_id(self, id: GroupId):
        self.items.remove(next(item for item in self.items
                                    if item.id == id))

def test_group_repository_add_group_should_add_it():
    repo = GroupRepository(None)
    new_group = Group('Intergalactic Python Team')
    new_group.id = 1 
    repo.add(new_group)
    saved_group = repo.items[0]
    assert saved_group == new_group

def test_group_repository_remove_group_should_remove_it():
    repo = GroupRepository(None)
    new_group = Group('Intergalactic Python Team')
    new_group.id = 1 
    repo.items.append(new_group)
    repo.remove(new_group)
    assert len(repo.items) == 0

def test_group_repository_remove_group_by_id_should_remove_it():
    repo = GroupRepository(None)
    new_group = Group('Intergalactic Python Team')
    new_group.id = 1 
    repo.items.append(new_group)
    repo.remove_by_id(new_group.id)
    assert len(repo.items) == 0

def test_group_repository_get_group_by_id_should_return_group():
    repo = GroupRepository(None)
    new_group = Group('Intergalactic Python Team')
    new_group.id = 1 
    repo.items.append(new_group)
    group = repo.get(1)
    assert group == new_group

def test_group_repository_update_group_should_update():
    repo = GroupRepository(None)
    new_group = Group('Intergalactic Python Team')
    new_group.id = 1 
    repo.items.append(new_group)
    new_group.name = 'Space Potatoes'
    repo.update(new_group)
    assert repo.items[0].name == 'Space Potatoes'

def test_group_repository_get_group_not_found_should_raise_exception():
    repo = GroupRepository(None)
    with pytest.raises(Exception) as excp:
        repo.get(1)
    assert 'Group not found' == str(excp.value)