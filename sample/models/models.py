from app.app import db


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), unique = False)
    first_name = db.Column(db.String(100), unique = False)

    def __init__(self, last_name, first_name):
        self.name = last_name + ' ' + first_name
