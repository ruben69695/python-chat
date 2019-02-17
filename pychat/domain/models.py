from datetime import datetime

class User:
    def __init__(self, username, firstname, lastname):
        self.id = None
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.created_at = datetime.utcnow()
        self.updated_at = None
        self.groups = []
        self.sent_messages = []
        self.received_messages = []


class Group:

    def __init__(self, name):
        self.id = None
        self.name = ''
        self.created_at = datetime.utcnow()
        self.updated_at = None    
        self.users = []
        self.messages = []


class Message:

    def __init__(self, sender_user_id, sender_group_id):
        self.id = None
        self.sender_user_id = sender_user_id
        self.sender_user = None
        self.sender_group_id = sender_group_id
        self.sender_group = None
        self.message_recipients = []
        self.sended_at = datetime.utcnow()
