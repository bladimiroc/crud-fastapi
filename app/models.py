from sqlalchemy import Column, Integer, String
from Database import Base

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(200))
    isComplete = Column(Integer)
