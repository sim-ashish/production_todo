from pydantic import BaseModel, EmailStr

class UserInput(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOutput(BaseModel):
    id: int
    name: str
    email: EmailStr

