from ast import Str
from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Models.core_model import Base, Session
from Models.company_model import CompanyModel, get_by_id as get_by_id_company
import datetime

class BusinessModel(Base):
    __tablename__ = 'businesses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    company_id = Column(Integer)
    active = Column(Boolean)
    created_at = Column(Date)
    updated_at = Column(Date)

    company = CompanyModel
    

def get_all():
    session = Session()
    products = session.query(BusinessModel).all()
    data = [{
        'id': item.id,
        'name': item.name,
        'address': item.address,
        'company_id': item.company_id,       
        'active': item.active,
        'created_at': item.created_at,
        'updated_at': item.updated_at,
        'company': get_by_id_company(item.company_id)
    } for item in products ]
    return data

def get_by_id(id):
    session = Session()
    obj = session.query(BusinessModel).filter(BusinessModel.id == id).one()
    data = {
        'id': obj.id,
        'name': obj.name,
        'address': obj.address,
        'company_id': obj.company_id,       
        'active': obj.active,
        'created_at': obj.created_at,
        'updated_at': obj.updated_at,
        'company': get_by_id_company(obj.company_id)
    }
    return data

def insert_data(data):
    session = Session()
    obj = BusinessModel()
    obj.name = data["name"]
    obj.address = data["address"]
    obj.company_id = data["company_id"]
    obj.active = data["active"]
    obj.created_at = datetime.datetime.now()
    session.add(obj)
    session.commit()
    return data

def update_data(data, id):
    session = Session()
    session.query(BusinessModel).filter(BusinessModel.id == id).update({
        'name': data["name"],
        'address': data["address"],
        'company_id': data["company_id"],
        'active': data["active"],        
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data