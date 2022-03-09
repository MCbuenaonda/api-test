from ast import Str
from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Models.core_model import Base, Session
import datetime

class CarmodelModel(Base):
    __tablename__ = 'car_models'
    id = Column(Integer, primary_key=True)
    car_brand_id = Column(Integer)
    name = Column(String)    
    slug = Column(String)    
    created_at = Column(Date)
    updated_at = Column(Date)
    

def get_all():
    session = Session()
    list = session.query(CarmodelModel).all()
    data = [{
        'id': item.id,
        'name': item.name,
        'slug': item.slug,
        'car_brand_id':item.car_brand_id,
        'created_at': item.created_at,
        'updated_at': item.updated_at
    } for item in list ]
    return data

def get_by_id(id):
    session = Session()
    obj = session.query(CarmodelModel).filter(CarmodelModel.id == id).one()
    data = {
        'id': obj.id,
        'name': obj.name,
        'slug': obj.slug,        
        'car_brand_id':obj.car_brand_id,
        'created_at': obj.created_at,
        'updated_at': obj.updated_at
    }
    return data

def insert_data(data):
    session = Session()
    obj = CarmodelModel()
    obj.name = data["name"]
    obj.slug = data["slug"]    
    obj.car_brand_id = data["car_brand_id"]    
    obj.created_at = datetime.datetime.now()
    session.add(obj)
    session.commit()
    return data

def update_data(data, id):
    session = Session()
    session.query(CarmodelModel).filter(CarmodelModel.id == id).update({
        'name': data["name"],      
        'slug': data["slug"],      
        'car_brand_id': data["car_brand_id"],      
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data