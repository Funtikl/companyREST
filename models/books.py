from db import db

class BookModel(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    author = db.Column('author', db.String(100))
    price = db.Column('price', db.Integer)

#table 'roles_users' is already defined for this MetaData instance error dealing
    # __table_args__ = {'extend_existing': True}

    def __init__(self, author, price):
        self.author = author
        self.price = price

    def json(self):
        return {'author': self.author, 'price': self.price}
    
    @classmethod
    def find_by_name(cls, author):
        return cls.query.filter_by(author=author).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
