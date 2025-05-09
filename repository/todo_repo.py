from sqlalchemy.orm import Session
from typing import List, Any
from uuid import UUID

from schemas.todo_schema import (InputTodo,
                                 OutputTodo,
                                 UpdateTodo)

from models import todo as todo_model


def instance_exist(id: UUID, db: Session) -> bool:
    '''This function will check weather the user with id is present in the database or not and return bool value'''

    todo_instance = db.query(todo_model.Todo).filter(todo_model.Todo.id == id).first()
    if todo_instance:
        return True
    
    return False


def get_all(db: Session, user_id: int) -> List[OutputTodo]:
    '''This function will return all todos filtered with user_id'''

    todos = db.query(todo_model.Todo).filter(todo_model.Todo.user_id == user_id).all()

    return todos

def create(todo: InputTodo, db: Session, user_id: int) -> OutputTodo:
    '''This function will create a new record in the database'''

    todo_instance = todo_model.Todo(**todo.model_dump(), user_id = user_id)
    db.add(todo_instance)
    db.commit()
    db.refresh(todo_instance)

    return todo_instance

def update(id: UUID, todo: UpdateTodo, db: Session):
    '''This function will update the record in the database'''

    db.query(todo_model.Todo).filter(todo_model.Todo.id == id).update(todo.model_dump(exclude_unset = True))
    db.commit()

    return


def retrieve(id: UUID, db: Session) -> OutputTodo:
    '''This function will retrieve a single record from database, filtered by id'''

    todo_instance = db.query(todo_model.Todo).filter(todo_model.Todo.id == id).first()

    return todo_instance


def destroy(id: UUID, db: Session):
    '''This function will delete a record from the database'''
    
    todo_instance = db.query(todo_model.Todo).filter(todo_model.Todo.id == id).first()
    db.delete(todo_instance)
    db.commit()

    return

