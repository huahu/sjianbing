from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class User(Base):
    __tablename__ = 'huahu'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return "<User('%s')>"%self.name

class DefConn(object):
    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://root:@localhost/huahu',echo=True)

    def GetConn(self):
        self.db=scoped_session(sessionmaker(bind=self.engine))
        return self.db



