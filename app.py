from distutils.command import config
from flask import Flask
import flask
from flask_cors import CORS
from flask_restful import Api
from swagger_ui import api_doc
#from Controllers.test_controller import Test
from Controllers.products_controller import Products, ProductsAction

#configura api
app = Flask(__name__)
api = Api(app)
CORS(app)
api_doc(app, config_path='doc.yaml', url_prefix='/api/doc',title='API Test')

#endpoints
#test
#api.add_resource(Test, '/')
api.add_resource(Products, '/products')
api.add_resource(ProductsAction, '/products/<id>')

app.run(host='0.0.0.0', port=5001, debug=True)