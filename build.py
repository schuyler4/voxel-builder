from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from user import User
from base import Base


class Build(Base):
    __tablename__ = "build"

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    code = Column(String())
    user = Column(Integer, ForeignKey("user.id"))

    def __init__(self, title, code, user):
        self.title = title
        self.code = code
        self.user = user

    def __repr__(self):
        return '<Build %r>' % self.title
