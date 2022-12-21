import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
from flask_celery import make_celery


import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret@@@aaaa35635'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://localhost:6379',
    'result_backend': 'redis://localhost:6379',
})
celery = make_celery(app)

db = SQLAlchemy(app)
with app.app_context():

    from app.views import views
