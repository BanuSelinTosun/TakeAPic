#/bin/sh
pip install --editable .
export FLASK_APP=TakeAPic.py
cd TakeAPic
flask run --host=0.0.0.0 --port=8777
