from flask_restful import Resource, reqparse
from models.books import BookModel


class BooksResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', required=True)
    parser.add_argument('price',  required=True)
    
    def get(self, name):

        book = BookModel.find_by_name(name)
        if book:
            return "The author of book is {} and the price is {}".format(book.json()['author'], book.json()['price'])
        return {'message': 'Book not found'}, 404    

    def post(self, name):
        if BookModel.find_by_name(name):
            return {'message':"A book {} already exists".format(name)}, 400

        data = BooksResource.parser.parse_args()
        book = BookModel(**data)

        try:
            book.save_to_db()
        except Exception as ex:
            return {"message": f"Error: {str(ex)}"}, 500
        return book.json(), 201

    def delete(self, name):
        book = BookModel.find_by_name(name)
        if book:
            book.delete_from_db()
            return {"message":"Book {} deleted".format(name)}, 200
        return {"message":"Book {} not found".format(name)}, 404

    def put(self, name):
        data = BooksResource.parser.parse_args()
        book = BookModel.find_by_name(name)

        if book:
            book.price = data["price"]
        else:
            book = BookModel(**data) 

        book.save_to_db()
        return book.json(), 201
        