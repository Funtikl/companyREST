from db import db

class SalesmanModel(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def json(self):
        return {'name': self.name, 'email': self.email}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

