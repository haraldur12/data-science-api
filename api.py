from flask import Flask, request, redirect, url_for, flash, jsonify
from flask_restful import Resource, Api, reqparse
import json
import numpy as np


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('_id', type=str)

class Service(Resource):
    def get(self):
        result = {
        'first': np.arange(0,20,1).tolist()
        }
        return jsonify(result) 
    def post(self):
        args = parser.parse_args()
        _id = str(args['_id'])
        return jsonify(_id)


api.add_resource(Service, '/api') 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')