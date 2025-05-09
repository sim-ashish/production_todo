from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str:
    '''This function will has the password using bcrypt scheme, returns the hashed password'''
    
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''This password matches the plain and hashed passwprd and return a boolean value'''

    return pwd_context.verify(plain_password, hashed_password)
