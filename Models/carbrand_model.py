from ast import Str
from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Models.core_model import Base, Session
import datetime

class CarbrandModel(Base):
    __tablename__ = 'car_brands'
    id = Column(Integer, primary_key=True)
    name = Column(String)    
    slug = Column(String)    
    created_at = Column(Date)
    updated_at = Column(Date)
    

def get_all():
    session = Session()
    list = session.query(CarbrandModel).all()
    data = [{
        'id': item.id,
        'name': item.name,
        'slug': item.slug,
        'created_at': item.created_at,
        'updated_at': item.updated_at
    } for item in list ]
    return data

def get_by_id(id):
    session = Session()
    category = session.query(CarbrandModel).filter(CarbrandModel.id == id).one()
    data = {
        'id': category.id,
        'name': category.name,
        'slug': category.slug,        
        'created_at': category.created_at,
        'updated_at': category.updated_at
    }
    return data

def insert_data(data):
    session = Session()
    obj = CarbrandModel()
    obj.name = data["name"]
    obj.slug = data["slug"]    
    obj.created_at = datetime.datetime.now()
    session.add(obj)
    session.commit()
    return data

def update_data(data, id):
    session = Session()
    session.query(CarbrandModel).filter(CarbrandModel.id == id).update({
        'name': data["name"],      
        'slug': data["slug"],      
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data