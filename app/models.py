from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Throw(Base):
    __tablename__ = "throws"
    id = Column(Integer, primary_key=True)
    target = Column(String)
    hit = Column(Boolean)