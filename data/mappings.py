from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table
import connection

Base = declarative_base()

user_group_table = Table('users_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('group_id', Integer, ForeignKey('groups.group_id'))
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

    def __repr__(self):
        return f'<Group (id={self.id}, name={self.name})>'

Base.metadata.create_all(connection.engine)