import sys
from sqlalchemy import Column, ForeignKey,Date,Numeric Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base=declarative_base()
class Shelter(Base):
    __tablename__='shelter'
    name=Column(String(80), nullable=False)
    address=Column(String(80),nullable=False)
    city=Column(String(80),nullable=False)
    state=Column(String(80),nullable=False)
    zipCode=Column(Integer,nullable=False)
    website=Column(String(80),nullable=False)
    id=Column(Integer, primary_key=True)
class Puppy(Base):
    __tablename__='puppy'
    name=Column(String(80) ,nullable=False)
    id=Column(Integer, primary_key=True)
    gender=Column(String(250))
    weight=Column(Numeric)
    dob=Column(Date)
    shelter_id=Column(Integer,ForeignKey('shelter.id'))
    shelter=relationship(Shelter)








engine=create_engine('sqlite:///puppy.db')
Base.metadata.create_all(engine)