web: flask run --host 0.0.0.0 --port ${PORT}
pre1: export FLASK_APP=run.py
pre2: export FLASK_CONFIG=production
init: flask db init
migrate: flask db migrate
upgrade: flask db upgrade