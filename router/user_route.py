from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from typing_extensions import Annotated
from schemas.user_schema import (UserInput,
                                 UserOutput)

from services import user_services


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
