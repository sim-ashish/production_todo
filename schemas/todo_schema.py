from datetime import date, datetime, timedelta
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field, validator
from uuid import UUID

class Status(str, Enum):
    completed = 'completed'
    pending = 'pending'
    failed = 'failed'

class InputTodo(BaseModel):
    title: str = Field(min_length=2, description='Title should not be empty')
    description: Union[str, None] = None
    due_date: date = Field(
        default=date.today() + timedelta(days=2),
        description='Default due date will be 24 hours after creating the todo'
    )
    priority: bool = False

    @validator('due_date', pre=True)
    def parse_due_date(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, '%d-%m-%Y').date()
        return v

    class Config:
        json_encoders = {
            date: lambda v: v.strftime('%d-%m-%Y')  
        }

class OutputTodo(InputTodo):
    id: UUID
    status: Status 
    created_at: datetime

    class Config:
        json_encoders = {
            **InputTodo.Config.json_encoders,
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')  # Optional: format datetime too
        }

class UpdateTodo(BaseModel):
    title : Union[str, None] = Field(default = None, min_length=2, description='Title should not be empty')
    description : Union[str, None] = None
    status : Union[Status, None] = None
    priority : Union[bool, None] = None