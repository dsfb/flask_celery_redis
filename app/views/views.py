from app import db, app
from random import choice
from flask import jsonify

from app import celery
from app.models.models import Usuario



@app.route("/nomes/<name>")
def retorna_nomes(name):
    
    task_valores.delay(name)
    return name


@celery.task()
def insert_valores():
    for i in range(50):

        data = ''.join(choice('ABCDE') for i in range(2))
        results = Usuario(nome=data)
        db.session.add(results)

        db.session.commit()

    return 'FEITO!'


@app.route('/insert', methods=['GET','POST'])
def insert_valor():
    task = insert_valores.delay()
    return jsonify({"valor":task.id}), 202


@celery.task()
def task_valores(string):
    return string

