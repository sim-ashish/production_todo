import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URL'), echo=False)

sessionLocal = sessionmaker(autoflush=False,
                            autocommit = False,
                            bind=engine)

Base = declarative_base()


def get_db():
    '''This function will yield a connection to the database everytime it called'''
    
    db = sessionLocal()
    try:
        yield db

    finally:
        db.close()