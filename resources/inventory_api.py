"""
    author: gauravsharma01042000@gmail.com
"""

from flask_restful import Resource, abort, reqparse


class InventoryManagement(Resource):
    """
    Inventory management class that has get, put, post and delete, rest api calls.
    """

    ITEMS = dict()  # this will act as db, key-value pair of item_name: item_count

    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)
        self.parser.add_argument('item_name', type=str, help='Item name must be provided.', location='form')
        self.parser.add_argument('item_count', type=int, help='Item count must be a number.', location='form')

    def get(self, item_name: str = None) -> tuple:
        """
        Get method to read items.
        :param item_name: String, default to None.
        :return: Tuple, of response.
        """
        if item_name is None:
            return self.ITEMS, 200
        elif item_name not in self.ITEMS.keys():
            abort(404, message=f"item_name: {item_name} not found.")
        return {'item_name': item_name, 'item_count': self.ITEMS[item_name]}, 200

    def post(self) -> tuple:
        """
        Post method to create the item entry.
        :return: Tuple.
        """
        args = self.parser.parse_args()
        item_name = args['item_name']
        item_count = args['item_count']
        if item_name in self.ITEMS.keys():
            abort(400, message=f"item_name: {item_name} already exists.")
        self.ITEMS[item_name] = item_count
        return {'msg': f"Item {item_name} successfully created."}, 201

    def put(self) -> tuple:
        """
        Put method to update the item.
        :return: Tuple.
        """
        args = self.parser.parse_args()
        item_name = args['item_name']
        item_count = args['item_count']
        if item_name not in self.ITEMS.keys():
            abort(404, message=f"item_name: {item_name} not found.")
        self.ITEMS[item_name] = item_count
        return {'msg': f"Item {item_name} successfully updated."}, 200

    def delete(self):
        """
        Delete method to delete the item from inventory.
        :return: Tuple.
        """
        args = self.parser.parse_args()
        item_name = args['item_name']
        if item_name not in self.ITEMS.keys():
            abort(404, message=f"item_name: {item_name} not found.")
        del self.ITEMS[item_name]
        return {'msg': f"Item {item_name} successfully deleted."}, 200
