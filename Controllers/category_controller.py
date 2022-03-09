from Models.category_model import get_all, get_by_id, insert_data, update_data
from flask_restful import Resource
from flask import make_response, jsonify, request
import sys

class Category(Resource):
    def get(self):
        try:
            data = get_all()
            return make_response(jsonify(data), 200)
        except:
            return make_response(jsonify({"message":str(sys.exc_info()[1])}), 400)
    def post(self):
        try:
            json_data = request.get_json()
            data = insert_data(json_data)
            return make_response(jsonify(data), 200)
        except:
            return make_response(jsonify({"message":str(sys.exc_info()[1])}), 400)

class CategoryAction(Resource):
    def get(self, id):
        try:
            data = get_by_id(id)
            return make_response(jsonify(data), 200)
        except:
            return make_response(jsonify({"message":str(sys.exc_info()[1])}), 400)
        
    def put(self, id):
        try:
            json_data = request.get_json()
            data = update_data(json_data, id)
            return make_response(jsonify(data), 200)
        except:
            return make_response(jsonify({"message":str(sys.exc_info()[1])}), 400)