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


#routes
@app.route('/', methods=('GET','POST'))
def home():
    return render_template('index.html')


@app.route('/books', methods=('GET','POST'))
def book():
    if request.method == "POST":
        return redirect('/books/{}'.format(request.form.get('books')))
        print(request.form.get('books'))
    return render_template('books.html')

@app.route('/salesman', methods=('GET','POST'))
def salesman():
    if request.method == "POST":
        print(request.form.get('salesman'))
        return redirect('/salesman/{}'.format(request.form.get('salesman')))
        
    return render_template('salesman.html')


@app.route('/stores', methods=('GET','POST'))
def stores():
    if request.method == "POST":
        print(request.form.get('store'))
        return redirect('/stores/{}'.format(request.form.get('address')))
        
    return render_template('stores.html')
api = Api(app)

api.add_resource(SalesmanResource, '/salesman/<string:name>')
api.add_resource(BooksResource, '/books/<string:name>')
api.add_resource(StoresResource, '/stores/<string:name>')
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
