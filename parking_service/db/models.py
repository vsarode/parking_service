import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:as2d2p@127.0.0.1/parkingDb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mutex@127.0.0.1/parkingDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String(90), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120))
    mobile_no = db.Column(db.String(15), unique=True, nullable=False)
    address = db.Column(db.String(1024), nullable=True)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    db.create_all()
    print "Success!!    "