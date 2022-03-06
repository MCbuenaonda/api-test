from Models.mundial_model import get_all
from flask_restful import Resource
from flask import make_response, jsonify

class Test(Resource):
    def get(self):
        data = get_all()
        return make_response(jsonify(data), 200)
    def post(self):
        data = get_all()
        return make_response(jsonify(data), 200)