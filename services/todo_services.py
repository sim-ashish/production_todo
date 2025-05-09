from schemas.todo_schema import (InputTodo,
                                OutputTodo,
                                UpdateTodo)

from repository.user_repo import user_exist_by_id
from fastapi import HTTPException, status
from typing import List, Any
from uuid import UUID
from repository import todo_repo
from sqlalchemy.orm import Session

def list_service(db: Session, user_id: int) -> List[OutputTodo]:
    if user_exist_by_id(user_id, db):
        return todo_repo.get_all(db, user_id)
    
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail=f'access denied')


def create_service(todo: InputTodo, db: Session, user_id: int) -> OutputTodo:
    if user_exist_by_id(user_id, db):
        return todo_repo.create(todo, db, user_id)
    
    raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail=f'user with id {user_id} does not exist')

def update_service(id: UUID, todo: UpdateTodo, db: Session):
    return todo_repo.update(id, todo, db)

def retrieve_service(id: UUID, db: Session) -> OutputTodo:
    if todo_repo.instance_exist(id, db):
        return todo_repo.retrieve(id, db)
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'object with id not found')

def destroy_service(id: UUID, db: Session):
    if todo_repo.instance_exist(id, db):
        return todo_repo.destroy(id, db)
        
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'object with this id not found')