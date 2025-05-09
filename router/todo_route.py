from fastapi import APIRouter, status,  Depends
from sqlalchemy.orm import Session
from dependency import check_user_cookie

from schemas import (InputTodo,
                     OutputTodo,
                     UpdateTodo) 

from services import todo_services
from typing_extensions import Annotated
from config.database import get_db
from typing import List
from uuid import UUID


router = APIRouter (
    prefix = "/todo",
    tags = ['Todo']
)

DB_CONNECTION = Annotated[Session, Depends(get_db)]

@router.get(
        '/',
        status_code=status.HTTP_200_OK, 
        summary="List all todos",
        description="List all the todos for the authenticated user"
        )
def all_todo(db: DB_CONNECTION, user_id: int = Depends(check_user_cookie)) -> List[OutputTodo]:
    return todo_services.list_service(db, user_id)


@router.post(
            '/', 
            status_code=status.HTTP_201_CREATED,
            summary="Create a Todo",
            description="Create a new todo"
            )
def create_todo(todo: InputTodo, db: DB_CONNECTION, user_id: int = Depends(check_user_cookie)) -> OutputTodo :
    return todo_services.create_service(todo, db, user_id)



@router.patch('/{id: UUID}',
             status_code=status.HTTP_200_OK,
             summary="Update a Todo",
             description="Update a todo partially or fully using id"
             )
def update_todo(id: UUID,todo: UpdateTodo, db: DB_CONNECTION):
    return todo_services.update_service(id, todo, db)


@router.get('/{id: UUID}',
             status_code=status.HTTP_204_NO_CONTENT,
             summary="Retrieve a Todo",
             description="Retrieve a single todo using id"
             )
def retrieve(id: UUID, db: DB_CONNECTION):
    return todo_services.retrieve_service(id, db)


@router.delete('/{id: UUID}',
                status_code=status.HTTP_204_NO_CONTENT,
                summary="Delete a Todo",
                description="Delete a todo using id"
                )
def destroy_todo(id: UUID, db: DB_CONNECTION):
    return todo_services.destroy_service(id, db)