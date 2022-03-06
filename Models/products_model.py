from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Models.core_model import Base, Session
import datetime

class ProductsModel(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)
    qty = Column(Integer)
    amount = Column(DECIMAL)
    image = Column(String)
    active = Column(Boolean)
    business_id = Column(Integer)
    category_id = Column(Integer)
    created_at = Column(Date)
    updated_at = Column(Date)
    

def get_all():
    session = Session()
    products = session.query(ProductsModel).all()
    data = [{
        'id': item.id,
        'code': item.code,
        'name': item.name,
        'qty': item.qty,
        'amount': item.amount,
        'image': item.image,
        'active': item.active,
        'business_id': item.business_id,
        'category_id': item.category_id,
        'created_at': item.created_at,
        'updated_at': item.updated_at
    } for item in products ]
    return data

def get_by_id(id):
    session = Session()
    product = session.query(ProductsModel).filter(ProductsModel.id == id).one()
    data = {
        'id': product.id,
        'code': product.code,
        'name': product.name,
        'qty': product.qty,
        'amount': product.amount,
        'image': product.image,
        'active': product.active,
        'business_id': product.business_id,
        'category_id': product.category_id,
        'created_at': product.created_at,
        'updated_at': product.updated_at
    }
    return data

def insert_data(data):
    session = Session()
    obj = ProductsModel()
    obj.code = data["code"]
    obj.name = data["name"]
    obj.qty = data["qty"]
    obj.amount = data["amount"]
    obj.image = data["image"]
    obj.active = data["active"]
    obj.business_id = data["business_id"]
    obj.category_id = data["category_id"]
    obj.created_at = datetime.datetime.now()
    session.add(obj)
    session.commit()
    return data

def update_data(data, id):
    session = Session()
    session.query(ProductsModel).filter(ProductsModel.id == id).update({
        'code': data["code"],
        'name': data["name"],
        'qty': data["qty"],
        'amount': data["amount"],
        'image': data["image"],
        'active': data["active"],
        'business_id': data["business_id"],
        'category_id': data["category_id"],
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data