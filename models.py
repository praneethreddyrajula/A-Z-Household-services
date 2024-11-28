from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String,Integer,Text,DateTime
from sqlalchemy import Column
from sqlalchemy import engine
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    email = Column(String(255),unique=True, nullable=False)
    password = Column(Text,nullable=False)
    fullname = Column(String(255), nullable=False)
    serviceName = Column(String(255))
    experience = Column(Integer)
    address = Column(Text)
    pinCode = Column(Integer)

Base.metadata.create_all(engine)