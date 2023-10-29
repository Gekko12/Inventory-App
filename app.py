"""
    author: gauravsharma01042000@gmail.com
"""

from flask import Flask
from flask_restful import Api
from resources.inventory_api import InventoryManagement

app = Flask(__name__)
api = Api(app)

api.add_resource(InventoryManagement, '/inv/get', '/inv/get/<string:item_name>', '/inv/add',
                 '/inv/put', '/inv/delete')

if __name__ == "__main__":
    app.run(debug=True)
