from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy


import os

# Instatiate and configure app, db, cache, mail, celery, etc.:
app = Flask(__name__)

# app.config.from_object('config.DevConfig')
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from models import *

#  Views #
@app.route('/')
def index():
	title = "2016 U.S. Presidential Candidates'"
	# Ordering by name, alphabetically.
	candidates = Candidate.query.order_by(Candidate.last_name).all()
	return render_template('index.html', title=title, candidates=candidates)

if __name__ == '__main__':
	# app.run(host='0.0.0.0')
	app.run()
