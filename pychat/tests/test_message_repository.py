from pychat.domain.ports import AbstractMessageRepository, MessageId
from pychat.domain.models import Message
import pytest

class MessageRepository(AbstractMessageRepository):

    def __init__(self, session):
        self.items = []

    def add(self, message: Message):
        self.items.append(message)

    def remove(self, message: Message):
        self.remove_by_id(message.id)

    def update(self, message: Message):
        index = self.items.index(self._get(message.id))
        self.items[index].message_recipients = message.message_recipients
        self.items[index].sended_at = message.sended_at


    def remove_by_id(self, id: MessageId):
        self.items.remove(self._get(id))

    def _get(self, id: MessageId) -> Message:
        return next((item for item in self.items
                            if item.id == id), None)

def test_message_repository_add_message_should_add_it():
    repo = MessageRepository(None)
    message = Message(1, None)
    message.message_recipients = [2]
    repo.add(message)
    assert repo.items[0].sender_user_id == 1

def test_message_repository_remove_message_should_remove_it():
    repo = MessageRepository(None)
    message = Message(1, None)
    message.message_recipients = [2]
    repo.items.append(message)
    repo.remove(message)
    assert len(repo.items) == 0

def test_message_repository_remove_message_by_id_should_remove_it():
    repo = MessageRepository(None)
    message = Message(1, None)
    message.message_recipients = [2]
    repo.items.append(message)
    repo.remove_by_id(message.id) 
    assert len(repo.items) == 0

def test_message_repository_update_message_by_id_should_update_it():
    repo = MessageRepository(None)
    message = Message(1, None)
    message.message_recipients = [2]
    repo.items.append(message)
    message.message_recipients = [4]
    repo.update(message)
    assert repo.items[0].message_recipients == [4]

def test_message_repository_get_message_by_id_should_return_the_message():
    repo = MessageRepository(None)
    message = Message(1, None)
    message.message_recipients = [2]
    repo.items.append(message)
    message_rescued = repo.get(message.id)
    assert message == message_rescued

def test_message_repository_get_message_not_found_should_raise_exception():
    repo = MessageRepository(None)
    with pytest.raises(Exception) as excp:
        repo.get(1)
    assert 'Message not found' == str(excp.value)

    
    