from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '02a577504b42c073a53faeeb9e70ca49'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anonyme:anonyme@localhost:5432/Techno2_project'


db = SQLAlchemy(app)
from app import routes