from app import db

class Books(db.Model):
    _id = db.Column('id', db.Integer, primmary_key = True)
    author = db.Column('author', db.Strung(100))
    price = db.Column('price', db.Interer)

    