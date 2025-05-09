from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from schemas.user_schema import (UserInput,
                                 UserOutput)

from repository import user_repo
from utils.hashing import hash_password


def create_user(user: UserInput, db: Session) -> UserOutput:
    if user_repo.user_exist(user, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with same email already registered")
    
    hashed_password = hash_password(user.password)
    user_dict = user.model_dump()
    user_dict['password'] = hashed_password
    user = UserInput(**user_dict)
    return user_repo.create(user, db)