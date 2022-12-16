from typing import Optional
from pydantic import BaseModel
  
class Todo(BaseModel):
    id:Optional[int]
    name:str
    isComplete:bool

    class Config:
        orm_mode = True

class Answer(BaseModel):
    message:str  