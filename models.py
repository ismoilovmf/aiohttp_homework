import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from db_config import DSN

engine = create_async_engine(DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=False)

    def __str__(self):
        return f'{self.id} {self.email} {self.password}'


class Advertisement(Base):
    __tablename__ = 'Advertisements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=50), nullable=False)
    description = Column(String(length=100), nullable=False)
    created = Column(DateTime, default=datetime.datetime.now())
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    user = relationship(User, backref='advertisements')
