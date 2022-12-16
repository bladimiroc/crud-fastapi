from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from Database import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/todo/', response_model=List[schemas.Todo])
def show_todo(db:Session=Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos

@app.post('/todo/',response_model=schemas.Todo)
def create_todo(input:schemas.Todo,db:Session=Depends(get_db)):
    todo = models.Todo(name = input.name,isComplete = input.isComplete)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@app.put('/todo/{todo_id}',response_model=schemas.Todo)
def update_todo(todo_id:int,input:schemas.Todo,db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter_by(id=todo_id).first()
    todo.name = input.name
    todo.isComplete = input.isComplete
    db.commit()
    db.refresh(todo)
    return todo

@app.get('/todo/{todo_id}',response_model=schemas.Todo)
def get_by_id(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter_by(id=todo_id).first()
    return todo

@app.delete('/todo/{todo_id}',response_model=schemas.Answer)
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(models.Todo).filter_by(id=todo_id).first()
    db.delete(todo)
    db.commit()
    answer = schemas.Answer(message="tarea eliminada")
    return answer
