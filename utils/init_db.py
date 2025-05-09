from config.database import engine
from models.todo import Todo
from models.user import User


def create_tables():
    Todo.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)
