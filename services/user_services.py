from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from schemas.user_schema import (UserInput,
                                 UserOutput)

from repository import user_repo
from utils.hashing import hash_password
from pydantic import EmailStr
from datetime import datetime, timedelta, timezone


def create_user(user: UserInput, db: Session) -> UserOutput:
    if user_repo.user_exist(user.email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with same email already registered")
    
    hashed_password = hash_password(user.password)
    user_dict = user.model_dump()
    user_dict['password'] = hashed_password
    user = UserInput(**user_dict)
    return user_repo.create(user, db)


def login_user(email: EmailStr, password: str, response: Response, db: Session):
    if not user_repo.user_exist(email, db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email doesn't exist")
    
    exist, user_id = user_repo.login(email, password, db)

    if exist == True and user_id != None:
        expire_time = datetime.now(timezone.utc) + timedelta(hours=12)
        response.set_cookie(key="user",
                            value=user_id,
                            expires=expire_time, 
                            httponly=True
                            )
        
        return {"detail" : "login success"}
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
