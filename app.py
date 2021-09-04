from flask import Flask, render_template, request, redirect
from flask_restful import Api 
from db import db
from flask_sqlalchemy import SQLAlchemy
from resources.salesman import SalesmanResource
from models.salesman import SalesmanModel
from models.books import BookModel
from resources.books import BooksResource
from resources.stores import StoresResource


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXEPTIONS'] = True

app.secret_key = 'very_secret'

@app.before_first_request
def create_tables():
    db.create_all()




api = Api(app)

api.add_resource(SalesmanResource, '/salesman/<string:name>')
api.add_resource(BooksResource, '/books/<string:name>')
api.add_resource(StoresResource, '/stores/<string:name>')
if __name__ == '__main__':
    from views import *
    db.init_app(app)
    app.run(port=5000, debug=True)
