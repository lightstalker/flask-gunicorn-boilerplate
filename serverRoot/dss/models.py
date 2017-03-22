from dss import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Test(db.Model):
    __tablename__ = "test"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Test {}".format(self.data)

db.create_all()
