from ast import Str
from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Models.core_model import Base, Session
import datetime

class CompanyModel(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)    
    active = Column(Boolean)
    created_at = Column(Date)
    updated_at = Column(Date)
    

def get_all():
    session = Session()
    list = session.query(CompanyModel).all()
    data = [{
        'id': item.id,
        'name': item.name,        
        'user_id': item.user_id,       
        'active': item.active,
        'created_at': item.created_at,
        'updated_at': item.updated_at
    } for item in list ]
    return data

def get_by_id(id):
    session = Session()
    company = session.query(CompanyModel).filter(CompanyModel.id == id).one()
    data = {
        'id': company.id,
        'name': company.name,
        'user_id': company.user_id,       
        'active': company.active,
        'created_at': company.created_at,
        'updated_at': company.updated_at
    }
    return data

def insert_data(data):
    session = Session()
    obj = CompanyModel()
    obj.name = data["name"]
    obj.user_id = data["user_id"]
    obj.active = data["active"]
    obj.created_at = datetime.datetime.now()
    session.add(obj)
    session.commit()
    return data

def update_data(data, id):
    session = Session()
    session.query(CompanyModel).filter(CompanyModel.id == id).update({
        'name': data["name"],
        'user_id': data["user_id"],
        'active': data["active"],        
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data