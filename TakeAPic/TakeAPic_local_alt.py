# Imports
import flask
import os
from werkzeug.utils import secure_filename    # Needed for image upload
import GoogleFace_local
import re
import pandas as pd
from StringIO import StringIO
import base64
# Flask location

# Base path for project
TakeAPic_BASE_PATH = os.path.dirname(__file__)

# Configure app
app = flask.Flask(__name__)

app.config.from_object(__name__) # Load config from thsie file (permit_generator.py)

app.config.update(dict(
SECRET_KEY = 'key',
USERNAME = 'admin',
PASSWORD = 'default'
))

@app.route('/', methods = ['GET'])
def index():
    method = flask.request.method
    return flask.render_template('index_local.html', title='Home')

@app.route('/submissions', methods = ['GET', 'POST'])
def submissions():
    uploaded_files = flask.request.files

    file_names = []
    for file in uploaded_files.getlist('file'):
        file_names.append(str(file.filename))

    directory_path = [TakeAPic_BASE_PATH + '/' + file_name for file_name in file_names]
    df = GoogleFace_local.feed(directory_path)
    analysis = []
    for i in range(0, df.shape[0]):
        analysis.append(dict(PIC=df.iloc[i]['PIC'], HAP=df.iloc[i]['HAP %'],SAD=df.iloc[i]['SAD %'],ANG=df.iloc[i]['ANG %'],SUR=df.iloc[i]['SUR %']))

    return flask.render_template('submissions_local_alt.html', analysis=analysis)
