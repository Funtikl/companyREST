from flask_restful import Resource, reqparse
from models.salesman import SalesmanModel

class SalesmanResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('email',  required=True)
    
    def get(self, name):
        salesman = SalesmanModel.find_by_name(name)
        if salesman:
            return salesman.json()
        return {'message': 'Salesman not found'}, 404    
    
    def post(self, name):
        if SalesmanModel.find_by_name(name):
            return {'message':"A salesman {} already exists".format(name)}, 400

        data = SalesmanResource.parser.parse_args()

        salesman = SalesmanModel(**data)

        try:
            salesman.save_to_db()
        except Exception as ex:
            return {"message": f"Error: {str(ex)}"}, 500
        return salesman.json(), 201

    def delete(self, name):
        salesman = SalesmanModel.find_by_name(name)
        if salesman:
            salesman.delete_from_db()
            return {"message":"Salesman {} deleted".format(name)}, 200
        return {"message":"Salesman {} not found".format(name)},404

    def put(self, name):
        data = SalesmanResource.parser.parse_args()
        salesman = SalesmanModel.find_by_name(name)

        if salesman:
            salesman.email = data["email"]
        else:
           salesman = SalesmanModel(**data) 

        salesman.save_to_db()
        return salesman.json(),201
