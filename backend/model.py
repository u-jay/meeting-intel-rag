from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    summary = Column(Text)
    topics = Column(Text)
    sentiment = Column(Text)
    actions = Column(Text)
