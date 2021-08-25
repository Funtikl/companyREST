from app import db

class Stores(db.Model):
    _id = db.Column('id', db.Integer, primary_key = True)   
    adress = db.Column('adress', db.String(100))

