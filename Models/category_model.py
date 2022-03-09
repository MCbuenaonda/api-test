from ast import Str
from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Models.core_model import Base, Session
import datetime

class CategoryModel(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)    
    created_at = Column(Date)
    updated_at = Column(Date)
    

def get_all():
    session = Session()
    list = session.query(CategoryModel).all()
    data = [{
        'id': item.id,
        'name': item.name,                
        'created_at': item.created_at,
        'updated_at': item.updated_at
    } for item in list ]
    return data

def get_by_id(id):
    session = Session()
    category = session.query(CategoryModel).filter(CategoryModel.id == id).one()
    data = {
        'id': category.id,
        'name': category.name,        
        'created_at': category.created_at,
        'updated_at': category.updated_at
    }
    return data

def insert_data(data):
    session = Session()
    obj = CategoryModel()
    obj.name = data["name"]    
    obj.created_at = datetime.datetime.now()
    session.add(obj)
    session.commit()
    return data

def update_data(data, id):
    session = Session()
    session.query(CategoryModel).filter(CategoryModel.id == id).update({
        'name': data["name"],      
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data