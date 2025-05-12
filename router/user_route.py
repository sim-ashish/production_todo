from fastapi import APIRouter, status, Depends, Body, Response
from sqlalchemy.orm import Session
from config.database import get_db
from typing_extensions import Annotated
from schemas.user_schema import (UserInput,
                                 UserOutput)

from services import user_services
from pydantic import EmailStr


router = APIRouter(
    prefix = "/user",
    tags = ['User']
)

DB_CONNECTION = Annotated[Session, Depends(get_db)]


@router.post('/',
             status_code = status.HTTP_201_CREATED,
             summary = 'Create User',
             description = 'create users using username, password, and email',
             response_model= UserOutput
             )
def register_user(user: UserInput, db: DB_CONNECTION) -> UserOutput:
    return user_services.create_user(user, db)


@router.post('/login',
             status_code = status.HTTP_200_OK,
             summary = 'Login User',
             description = 'Login User using email and password'
             )
def login_user(email: Annotated[EmailStr, Body()], password: Annotated[str, Body()] , response: Response, db: DB_CONNECTION) -> dict:
    return user_services.login_user(email, password, response, db)