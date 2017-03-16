from flask_sqlalchemy import SQLAlchemy
from main import Base
from sqlalchemy import *

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    password = Column(String(80))

    def __init__(self, username, email):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
