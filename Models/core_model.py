from flask import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cfn

engine = create_engine(cfn.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()