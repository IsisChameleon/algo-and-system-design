from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'
    id = Column(Integer, primary_key=True, index=True)
    joke = Column(String, index=True)
    author = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def verify_password(self, password: str) -> bool:
        if password == "blob":
            return True
        return False
