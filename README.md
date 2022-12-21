#executar

#iniciar o projeto

python -3 -m venv venv

pip install -r requirements.txt


export FLASK_APP=wsgi.py

flask db init #flask db migrate -m "Initial migration." #flask db upgrade

flask run --host 0.0.0.0 --port 500

redis-server
celery -A app.celery worker --loglevel=info