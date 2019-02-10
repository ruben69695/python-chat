from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table
import connection

Base = declarative_base()

user_group_table = Table('users_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), index=True),
    Column('group_id', Integer, ForeignKey('groups.group_id'), index=True)
)

message_recipients_table = Table('message_recipients', Base.metadata,
    Column('message_id', Integer, ForeignKey('messages.message_id'), index=True, unique=True),
    Column('user_id', Integer, ForeignKey('users.user_id'), index=True, unique=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(30), unique=True, nullable=False)
    firstname = Column('firstname', String(30), nullable=True)
    lastname = Column('lastname', String(60), nullable=True)
    created_at = Column('created_at', DateTime, nullable=False)
    updated_at = Column('updated_at', DateTime, nullable=True)
    groups = relationship('Group',
                secondary=user_group_table,
                back_populates='users')
    sent_messages = relationship('Message',back_populates='sender_user')
    received_messages = relationship('Message',
                            secondary=message_recipients_table,
                            back_populates='message_recipients')

    def __repr__(self):
        return f'<User (id={self.id}, firstname={self.firstname}, lastname={self.lastname}, username={self.username})>'

class Group(Base):
    __tablename__ = 'groups'

    id = Column('group_id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(45), unique=True)
    created_at = Column('created_at', DateTime, nullable=False)
    updated_at = Column('updated_at', DateTime, nullable=True)    
    users = relationship('User',
                secondary=user_group_table,
                back_populates='groups')
    messages = relationship('Message', back_populates='sender_group')

    def __repr__(self):
        return f'<Group (id={self.id}, name={self.name})>'

class Message(Base):
    __tablename__ = 'messages'

    id = Column('message_id', Integer, primary_key=True, autoincrement=True)
    sender_user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False, index=True)
    sender_user = relationship('User', back_populates='sent_messages')
    sender_group_id = Column(Integer, ForeignKey('groups.group_id'), nullable=True, index=True)
    sender_group = relationship('Group', back_populates='messages')
    message_recipients = relationship('User',
                            secondary=message_recipients_table,
                            back_populates='received_messages')
    sended_at = Column('sended_at', DateTime, nullable=False)

    def __repr__(self):
        return f'<Message (id={self.id}, sender={self.sender_user_id}, sender_group={self.sender_group_id})>'


Base.metadata.create_all(connection.engine)