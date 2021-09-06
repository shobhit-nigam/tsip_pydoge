from flask import Flask, json
from flask_restful import Resource, Api, reqparse
from flask import render_template
import pandas as pd

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

class BigMarket(Resource):
    def get(self):
        data = pd.read_excel('bigmarket.xlsx')
        data = data.to_dict()
        return {'market_details': data}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Month', required=True)
        parser.add_argument('Store', required=False)
        parser.add_argument('Sales', required=False)
        args = parser.parse_args()

        data = pd.read_excel('bigmarket.xlsx')

        if args['Month'] in list(data['Month']):
            return {
            'message': f"'{args['Month']}' already exists"
            }, 410
        else:
            new_data = pd.DataFrame({
            'Month':[args['Month']],
            'Store':[args['Store']],
            'Sales':[args['Sales']]
            })

        data.append(new_data, ignore_index=True)
        data.to_excel("bigmarket_1.xlsx", index=False)
        return {'data': data.to_dict()}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Month', required=True)
        args = parser.parse_args()

        data = pd.read_excel('bigmarket.xlsx')

        if args['Month'] in list(data['Month']):
            del data['Month']

            data.to_excel("bigmarket.xlsx", index=False)
            return {'data': data.to_dict()}, 200
        else:
            return {
            'message': f"'{args['Month']}' not found"
            }, 404

api.add_resource(BigMarket, '/bigmarket')

if __name__ == '__main__':
    app.run()
