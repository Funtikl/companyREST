from flask_restful import Resource, reqparse
from models.books import BooksModel

class BooksRes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', required=True)
    parser.add_argument('price',  required=True)
    
    def get(self, name):
        book = BooksModel.find_by_name(name)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404    
    
    def post(self, name):
        if BooksModel.find_by_name(name):
            return {'message':"A book {} already exists".format(name)}, 400

        data = BooksRes.parser.parse_args()
        book = BooksModel(**data)

        try:
            book.save_to_db()
        except Exception as ex:
            return {"message": f"Error: {str(ex)}"}
        return book.json(), 201

    def delete(self, name):
        book = BooksModel.find_by_name(name)
        if book:
            book.delete_from_db()
            return {"message":"Book {} deleted".format(name)}
        return {"message":"Book {} not found".format(name)}, 404

    def put(self, name):
        data = BooksRes.parser.parse_args()
        book = BooksModel.find_by_name(name)

        if book:
            book.price = data["price"]
        else:
            book = BooksModel(**data) 

        book.save_to_db()
        return book.json()
        