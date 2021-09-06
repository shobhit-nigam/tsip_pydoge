from flask import Flask, json
from flask_restful import Resource, Api, reqparse

data = []

api = Flask(__name__)

@api.route('/data', methods=['GET'])
def get_data():
    return json.dumps(data)

@api.route('/data', methods=['POST'])
def post_data():

    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True)
    parser.add_argument('name', required=False)
    args = parser.parse_args()

    new_data = {"id" : args['id'], "name": args['name']}

    data.append(new_data)
    return json.dumps({"addition was success" : True}), 201

if __name__ == '__main__':
    api.run()
