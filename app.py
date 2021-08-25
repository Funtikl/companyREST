from flask import Flask
from flask_restful import Api 
from db import db
from flask_sqlalchemy import SQLAlchemy
from resources.salesman import SalesmanRes
from models.salesman import SalesmanModel

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXEPTIONS'] = True


app.secret_key = 'very_secret'


@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)

api.add_resource(SalesmanRes, '/salesman/<string:name>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
