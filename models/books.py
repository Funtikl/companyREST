from app import db

class Books(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    author = db.Column('author', db.String(100))
    price = db.Column('price', db.Integer)

#table 'roles_users' is already defined for this MetaData instance error dealing
    __table_args__ = {'extend_existing': True}

    def __init__(self, author, price):
        self.author = author
        self.price = price