from flask import Flask
from routes.contacts import contacts

#from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/contactdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False





app.register_blueprint(contacts)


