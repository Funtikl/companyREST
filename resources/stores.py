from flask_restful import Resource, reqparse
from models.stores import StoreModel

class StoresRes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True) 
    parser.add_argument('address', required=True)
    
    def get(self, name):
        storeName = StoreModel.find_by_name(name)
        if storeName:
            return storeName.json()
        return {'message': 'Store not found'}, 404    
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':"A store {} already exists".format(name)}, 400

        data = StoresRes.parser.parse_args()
        print(data)

        store = StoreModel(**data)
        try:
            store.save_to_db()
        except Exception as ex:
            return {"message": f"Error: {str(ex)}"}, 404
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message":"Address {} deleted".format(name)}
        return {"message":"Address {} not found".format(name)}, 404

    def put(self, name):
        data =  StoresRes.parser.parse_args()
        store = StoreModel.find_by_name(name)

        if store:
            store.price = data["address"]
        else:
            store = StoreModel(**data) 

        address.save_to_db()
        return address.json()
        