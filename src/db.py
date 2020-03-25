from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
# Init db
db = SQLAlchemy(app)


class Journal(db.Model):

    # Required Fields
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    title = db.Column(db.String(20000))
    journal_type = db.Column(db.String(100))
    issn = db.Column(db.String(100))
    sjr = db.Column(db.String(25))
    sjr_best_quartile = db.Column(db.String(10))
    h_index = db.Column(db.Integer)
    total_docs_08 = db.Column(db.Integer)
    total_docs_3yrs = db.Column(db.Integer)
    total_refs = db.Column(db.Integer)
    total_cites_3yrs = db.Column(db.Integer)
    citable_docs_3yrs = db.Column(db.Integer)
    cites_docs_2yrs = db.Column(db.String(25))
    ref_doc = db.Column(db.String(25))
    country = db.Column(db.String(100))
    publisher = db.Column(db.String(200))
    coverage = db.Column(db.String(200))
    categories = db.Column(db.String(200))

    def __init__(self, post):
        # Required Fields
        self.rank = post[0]
        self.id = post[1]
        self.title = post[2]
        self.journal_type = post[3]
        self.issn = post[4]
        self.sjr = post[5]
        self.sjr_best_quartile = post[6]
        self.h_index = post[7]
        self.total_docs_08 = post[8]
        self.total_docs_3yrs = post[9]
        self.total_refs = post[10]
        self.total_cites_3yrs = post[11]
        self.citable_docs_3yrs = post[12]
        self.cites_docs_2yrs = post[13]
        self.ref_doc = post[14]
        self.country = post[15]
        self.publisher = post[16]
        self.coverage = post[17]
        self.categories = post[18]


# create database
db.create_all()
