from user import User
from build import Build
from main import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func
from sqlalchemy import *

engine = create_engine('sqlite:///data.db', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()
metadata = MetaData()
Base.metadata.create_all(engine)


#engine = create_engine('sqlite:///data.db', echo=True)
##db_session = Session()
#metadata = MetaData()

#db.create_all()
