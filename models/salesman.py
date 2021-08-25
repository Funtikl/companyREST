from app import db

class Salesman(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    nane = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email