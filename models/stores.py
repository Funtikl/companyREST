from app import db

class Stores(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)   
    adress = db.Column('adress', db.String(100))

    def __init__(self, adress):
        self.adress = adress

