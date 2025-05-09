import uuid
from config.database import Base
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = "todos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default='pending')
    created_at = Column(DateTime, default=func.now())
    due_date = Column(DateTime)
    priority = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    # Link back to User
    owner = relationship("User", back_populates="todos")

