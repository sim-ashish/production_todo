from sqlalchemy.orm import Session
from schemas.user_schema import (UserInput,
                                 UserOutput)

from models.user import User

def user_exist(user: UserInput, db: Session) -> bool:
    '''This function will check weather the user is present in the database, search using email of the user'''

    email: str = user.email
    exist_user = db.query(User).filter(User.email == email).first()
    if exist_user:
        return True
    
    return False


def user_exist_by_id(user_id, db: Session) -> bool:
    '''This function will check weather the user is present in the database, search using id of the user'''

    exist_user = db.query(User).filter(User.id == user_id).first()
    if exist_user:
        return True
    
    return False

def create(user: UserInput, db: Session) -> UserOutput:
    '''This function will create a new user'''
    
    user_instance = User(**user.model_dump())
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)

    return user_instance