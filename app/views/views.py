from app import db, app
from random import choice
from flask import jsonify

from app import celery

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(1000))



@app.route("/process/<name>")
def retorna_nomes(name):
    
    task_valores.delay(name)
    return name


@celery.task()
def insert_valores():
    for i in range(50):

        data = ''.join(choice('ABCDE') for i in range(2))
        results = Usuarios(nome=data)
        print
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

