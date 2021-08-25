from app import db

class salesman(db.Model):
    _id = db.Column('id', db.Integer, primary_key = True)
    nane = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

