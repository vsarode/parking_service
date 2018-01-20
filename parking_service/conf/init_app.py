from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:as2d2p@127.0.0.1/parkingDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
