#/bin/sh
pip install --editable .
export FLASK_APP=face.py
cd face
flask run --host=0.0.0.0 --port=8080
