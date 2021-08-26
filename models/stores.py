from db import db

class StoreModel(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)   
    name = db.Column('name', db.String)
    address = db.Column('address', db.String(100))

    def __init__(self, name, address):
        self.name = name
        self.address = address


    def json(self):
        return {'name':self.name, 'address': self.address}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()