from flask_restful import Resource, reqparse
from models.salesman import SalesmanModel

class SalesmanRes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('email',  required=True)
    def get(self, name):
        salesman = SalesmanModel.find_by_name(name)
        if salesman:
            return salesman.json()
        return {'message': 'Salesman not found'}    
    
    def post(self, name):
        if SalesmanModel.find_by_name(name):
            return {'message':"A salesman {} already exists".format(name)}, 400

        data = SalesmanRes.parser.parse_args()

        salesman = SalesmanModel(**data)

        try:
            salesman.save_to_db()
        except:
            return {"message":"Error"}
        return salesman.json(), 201