import typing
import sqlalchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapper, scoped_session, sessionmaker, composite, query
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table, MetaData, create_engine, event
from sqlalchemy_utils.functions import create_database, drop_database
from sqlalchemy.orm.
from pychat.domain.models import User, Group, Message
from pychat.domain.ports import UnitOfWork, UnitOfWorkManager
from pychat.domain.ports import (AbstractUserRepository, AbstractMessageRepository, 
                                    AbstractGroupRepository, UserId, GroupId, MessageId)

SessionFactory = typing.Callable[[], sqlalchemy.orm.Session]

class UserRepository(AbstractUserRepository):

    def __init__(self, session):
        self.session = session

    def add(self, user: User):
        self.session.add(user)

    def get_by_username(self, username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()
    
    def _get(self, id: int) -> User:
        return self.session.query(User).get(id)

    def remove(self, user: User):
        self.remove_by_id(user.id)

    def update(self, user: User):
        self.session(User).filter(User.id == user.id).\
            update(
                {
                    User.username: user.username, 
                    User.firstname: user.firstname, 
                    User.lastname: user.lastname,
                    User.updated_at: datetime.utcnow()
                })

    def remove_by_id(self, id: UserId):
        self.session.query(User).filter(User.id == id).\
            delete(synchronize_session=False)

class GroupRepository(AbstractGroupRepository):
    
    def __init__(self, session):
        self.session = session

    def add(self, group: Group):
        pass
    
    def _get(self, id: int) -> Group:
        pass

    def remove(self, group: Group):
        pass

    def update(self, group: Group):
        pass

    def remove_by_id(self, id: GroupId):
        pass

class MessageRepository(AbstractMessageRepository):

    def __init__(self, session):
        self.session = session

    def add(self, message: Message):
        pass
    
    def _get(self, id: int) -> Message:
        pass

    def remove(self, message: Message):
        pass

    def update(self, message: Message):
        pass

    def remove_by_id(self, id: MessageId):
        pass

class SQLAlchemyUnitOfWorkManager(UnitOfWorkManager):
    """
        The Unit of work manager returns a new unit of work. 
        Our UOW is backed by a sql alchemy session whose 
        lifetime can be scoped to a web request, or a 
        long-lived background job.
    """
    def __init__(self, session_maker):
        self.session_maker = session_maker

    def start(self) -> UnitOfWork:
        return SQLAlchemyUnitOfWork(self.session_maker)

class SQLAlchemyUnitOfWork(UnitOfWork):
    """
        The unit of work captures the idea of a set of things that
        need to happen together. 

        Usually, in a relational database, 
        one unit of work == one database transaction.
    """
    def __init__(self, sessionfactory: SessionFactory) -> None:
        self.sessionfactory = sessionfactory
        event.listen(self.sessionfactory, "after_flush", self.gather_events)
        event.listen(self.sessionfactory, "loaded_as_persistent",
                     self.setup_events)

    def __enter__(self):
        self.session = self.sessionfactory()
        self.flushed_events = []
        return self

    def __exit__(self):
        self.publish_events()

    def commit(self):
        self.session.flush()
        self.session.commit()

    def rollback(self):
        self.flushed_events = []
        self.session.rollback()

    def setup_events(self, session, entity):
        entity.events = []

    def gather_events(self, session, ctx):
        flushed_objects = [e for e in session.new] + [e for e in session.dirty]
        for e in flushed_objects:
            try:
                self.flushed_events += e.events
            except AttributeError:
                pass

    def publish_events(self):
        for e in self.flushed_events:
            self.bus.handle(e)

    @property
    def users(self):
        return UserRepository(self.session)
    
    @property
    def groups(self):
        return GroupRepository(self.session)

    @property
    def messages(self):
        return MessageRepository(self.session)


class SQLAlchemy:

    def __init__(self, uri):
        self.engine = create_engine(uri, echo=True)
        self._session_maker = scoped_session(sessionmaker(self.engine),)
        self.uow_manager = SQLAlchemyUnitOfWorkManager(self._session_maker)

    def create_schema(self):
        create_database(self.engine.url)
        self.metadata.create_all()

    def recreate_schema(self):
        self.configure_mappings()
        drop_database(self.engine.url)
        self.create_schema()

    def get_session(self):
        return self._session_maker()

    def start_unit_of_work(self):
        return self.uow_manager.start()

    def configure_mappings(self):
        self.metadata = MetaData(self.engine)

        user_group_table = Table('users_groups', self.metadata,
            Column('user_id', Integer, ForeignKey('users.user_id'), index=True),
            Column('group_id', Integer, ForeignKey('groups.group_id'), index=True)
        )

        message_recipients_table = Table('message_recipients', self.metadata,
            Column('message_id', Integer, ForeignKey('messages.message_id'), index=True, unique=True),
            Column('user_id', Integer, ForeignKey('users.user_id'), index=True, unique=True)
        )

        users_table = Table('users', self.metadata,
                            Column('user_id', Integer, primary_key=True, autoincrement=True),
                            Column('username', String(30), unique=True, nullable=False),
                            Column('firstname', String(30), nullable=True),
                            Column('lastname', String(60), nullable=True),
                            Column('created_at', DateTime, nullable=False),
                            Column('updated_at', DateTime, nullable=True))

        groups_table = Table('groups', self.metadata,
                            Column('group_id', Integer, primary_key=True, autoincrement=True),
                            Column('name', String(45), unique=True),
                            Column('created_at', DateTime, nullable=False),
                            Column('updated_at', DateTime, nullable=True))

        messages_table = Table('messages', self.metadata,
                                Column('message_id', Integer, primary_key=True, autoincrement=True),
                                Column('fk_sender_user_id', Integer, ForeignKey('users.user_id'), nullable=False, index=True),
                                Column('fk_sender_group_id', Integer, ForeignKey('groups.group_id'), nullable=True, index=True),
                                Column('sended_at', DateTime, nullable=False))

        mapper(
            User,
            users_table,
            properties={
                'id':
                users_table.c.user_id,
                'username':
                users_table.c.username,
                'firstname':
                users_table.c.firstname,
                'lastname':
                users_table.c.lastname,
                'created_at':
                users_table.c.created_at,
                'updated_at':
                users_table.c.updated_at,
                'groups':
                relationship(Group, 
                    secondary=user_group_table, 
                    back_populates='users'),
                'sent_messages':
                relationship(Message,
                    back_populates='sender_user'),
                'received_messages':
                relationship(Message,
                        secondary=message_recipients_table,
                        back_populates='message_recipients')
            },
        ),

        mapper(
            Group,
            groups_table,
            properties={
                'id':
                groups_table.c.group_id,
                'name':
                groups_table.c.name,
                'created_at':
                groups_table.c.created_at,
                'updated_at':
                groups_table.c.updated_at,
                'users':
                relationship(User,
                    secondary=user_group_table,
                    back_populates='groups'),
                'messages':
                relationship(Message, 
                    back_populates='sender_group')
            },
        ),

        mapper(
            Message,
            messages_table,
            properties={
                'id':
                messages_table.c.message_id,
                'sender_user_id':
                messages_table.c.fk_sender_user_id,
                'sender_group_id':
                messages_table.c.fk_sender_group_id,
                'sended_at':
                messages_table.c.sended_at,
                'sender_user':
                relationship(User, back_populates='sent_messages'),
                'sender_group':
                relationship(Group, back_populates='messages'),
                'message_recipients':
                relationship(User,
                        secondary=message_recipients_table,
                        back_populates='received_messages')
            }
        )