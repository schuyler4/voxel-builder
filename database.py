from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func
from sqlalchemy import *
from base import Base

from user import User
from build import Build

engine = create_engine('sqlite:///data.db', echo=True)
Session = sessionmaker(bind=engine)
metadata = MetaData()
Base.metadata.create_all(engine)


#engine = create_engine('sqlite:///data.db', echo=True)
db_session = Session()
#metadata = MetaData()

#db.create_all()
