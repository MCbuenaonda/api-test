from distutils.command import config
from flask import Flask
import flask
from flask_cors import CORS
from flask_restful import Api
from swagger_ui import api_doc
from Controllers.products_controller import Products, ProductsAction
from Controllers.business_controller import Business, BusinessAction
from Controllers.company_controller import Company, CompanyAction
from Controllers.category_controller import Category, CategoryAction
from Controllers.carbrand_controller import Carbrand, CarbrandAction
from Controllers.carmodel_controller import Carmodel, CarmodelAction

#configura api
app = Flask(__name__)
api = Api(app)
CORS(app)
api_doc(app, config_path='doc.yaml', url_prefix='/api/doc',title='API Test')

#endpoints
api.add_resource(Products, '/products')
api.add_resource(ProductsAction, '/products/<id>')

api.add_resource(Business, '/business')
api.add_resource(BusinessAction, '/business/<id>')

api.add_resource(Company, '/company')
api.add_resource(CompanyAction, '/company/<id>')

api.add_resource(Category, '/category')
api.add_resource(CategoryAction, '/category/<id>')

api.add_resource(Carbrand, '/carbrand')
api.add_resource(CarbrandAction, '/carbrand/<id>')

api.add_resource(Carmodel, '/carmodel')
api.add_resource(CarmodelAction, '/carmodel/<id>')

app.run(host='0.0.0.0', port=8080, debug=True)