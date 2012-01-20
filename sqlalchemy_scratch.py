import sqlalchemy
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/fishlog', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     user_name = Column(String)
     password = Column(String)

     def __init__(self, id, user_name, password):
         self.id = id 
         self.user_name = user_name
         self.password = password

 
our_user = session.query(User).filter_by(user_name='mtafel').first()    
print "The user is named", our_user.user_name
