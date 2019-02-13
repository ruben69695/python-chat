import abc
from typing import NewType
from pychat.domain.models import User, Group, Message

UserId = NewType('UserId', int)
GroupId = NewType('GroupId', int)
MessageId = NewType('MessageId', int)


class UnitOfWork(abc.ABC):

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, type, value, traceback):
        pass

    @abc.abstractmethod
    def commit(self):
        pass

    @abc.abstractmethod
    def rollback(self):
        pass


class UnitOfWorkManager(abc.ABC):

    @abc.abstractmethod
    def start(self) -> UnitOfWork:
        pass

class AbstractUserRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, user: User):
        pass

    @abc.abstractmethod
    def remove(self, user: User):
        pass

    @abc.abstractmethod
    def update(self, user: User):
        pass

    @abc.abstractmethod
    def remove_by_id(self, id: UserId):
        pass
    
    @abc.abstractmethod
    def _get(self, id: UserId) -> User:
        pass

    @abc.abstractmethod
    def get_by_username(self, username: str) -> User:
        pass

    def get(self, id) -> User:
        user = self._get(id)
        if user is None:
            raise Exception('User not found')
        return user

class AbstractGroupRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, group: Group):
        pass

    @abc.abstractmethod
    def remove(self, group: Group):
        pass

    @abc.abstractmethod
    def update(self, group: Group):
        pass

    @abc.abstractmethod
    def remove_by_id(self, id: GroupId):
        pass

    @abc.abstractmethod
    def _get(self, id: GroupId) -> Group:
        pass

    def get(self, id) -> Group:
        group = self._get(id)
        if group is None:
            raise Exception('Group not found')
        return group

class AbstractMessageRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, message: Message):
        pass

    @abc.abstractmethod
    def remove(self, message: Message):
        pass

    @abc.abstractmethod
    def update(self, message: Message):
        pass

    @abc.abstractmethod
    def remove_by_id(self, id: MessageId):
        pass

    @abc.abstractmethod
    def _get(self, id: MessageId) -> Message:
        pass

    def get(self, id) -> Message:
        message = self._get(id)
        if message is None:
            raise Exception('Message not found')
        return message