import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true     
from sqlalchemy.orm import session, sessionmaker   

Base = declarative_base()



engine = create_engine('mysql+pymysql://test1:Aijaz123!@localhost:3306/aijaz')
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()