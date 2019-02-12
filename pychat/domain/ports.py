import abc
import typing
from pychat.domain.models import User, Group, Message

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
    def add(self, user: User) -> User:
        pass
    
    @abc.abstractmethod
    def _get(self, id: int) -> User:
        pass

    def get(self, id) -> User:
        user = self._get(id)
        if user is None:
            raise Exception('User not found')
        return user

class AbstractGroupRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, group: Group) -> Group:
        pass

    @abc.abstractmethod
    def _get(self, id: int) -> Group:
        pass

    def get(self, id) -> Group:
        group = self._get(id)
        if group is None:
            raise Exception('Group not found')
        return group

class AbstractMessageRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, group: Message) -> Message:
        pass

    @abc.abstractmethod
    def _get(self, id: int) -> Message:
        pass

    def get(self, id) -> Message:
        message = self._get(id)
        if message is None:
            raise Exception('Message not found')
        return message