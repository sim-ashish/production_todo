from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = True, index = True)
    name = Column(String, nullable = False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    todos = relationship("Todo", back_populates="owner", cascade="all, delete", lazy="joined")

