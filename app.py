from flask import Flask
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy



#testing branch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXEPTIONS'] = True

app.secret_key = 'very_secret'

db = SQLAlchemy(app)
api = Api(app)

@app.route('/')
def home():
    return "Hello, World"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
