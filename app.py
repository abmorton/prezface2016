from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy


import os

# Instatiate and configure app, db, cache, mail, celery, etc.:
app = Flask(__name__)

# app.config.from_object('config.DevConfig')
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from models import Candidate

#  Views #

@app.route('/')
def index():
	title = 'PrezFace2016'
	return render_template('index.html', title=title)


if __name__ == '__main__':
	app.run(host='0.0.0.0')
	# app.run()
