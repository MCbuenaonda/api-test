from unicodedata import decimal
from sqlalchemy import Column, String, Integer, Date, Boolean, DECIMAL, insert
from Controllers.business_controller import Business
from Controllers.category_controller import Category
from Models.core_model import Base, Session
from Models.business_model import BusinessModel, get_by_id as get_by_id_business 
from Models.category_model import CategoryModel, get_by_id as get_by_id_category 
from Models.carbrand_model import CarbrandModel, get_by_id as get_by_id_carbrand 
from Models.carmodel_model import CarmodelModel, get_by_id as get_by_id_carmodel 
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
    car_brand_id = Column(Integer)
    car_model_id = Column(Integer)
    year = Column(Integer)
    created_at = Column(Date)
    updated_at = Column(Date)

    business = BusinessModel
    category = CategoryModel
    car_brand = CarbrandModel
    car_model = CarmodelModel
    
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
        'car_brand_id': item.car_brand_id,
        'car_model_id': item.car_model_id,
        'created_at': item.created_at,
        'updated_at': item.updated_at,
        'year': item.year,
        'category': get_by_id_category(item.category_id),
        'car_brand': get_by_id_carbrand(item.car_brand_id),
        'car_model': get_by_id_carmodel(item.car_model_id)
    } for item in products ]
    return data

def get_by_id(id):
    session = Session()
    obj = session.query(ProductsModel).filter(ProductsModel.id == id).one()
    data = {
        'id': obj.id,
        'code': obj.code,
        'name': obj.name,
        'qty': obj.qty,
        'amount': obj.amount,
        'image': obj.image,
        'active': obj.active,
        'business_id': obj.business_id,
        'category_id': obj.category_id,
        'car_brand_id': obj.car_brand_id,
        'car_model_id': obj.car_model_id,
        'created_at': obj.created_at,
        'updated_at': obj.updated_at,
        'year': obj.year,
        'business': get_by_id_business(obj.business_id),
        'category': get_by_id_category(obj.category_id),
        'car_brand': get_by_id_carbrand(obj.car_brand_id),
        'car_model': get_by_id_carmodel(obj.car_model_id)
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
    obj.car_brand_id = data["car_brand_id"]
    obj.car_model_id = data["car_model_id"]
    obj.year = data["year"],
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
        'car_brand_id': data["car_brand_id"],
        'car_model_id': data["car_model_id"],
        'year': data["year"],
        'updated_at': datetime.datetime.now()
    })
    session.commit()
    return data