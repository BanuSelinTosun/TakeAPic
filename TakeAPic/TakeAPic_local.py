# Imports
import flask
import os
from werkzeug.utils import secure_filename    # Needed for image upload
import GoogleFace_local
import re
import pandas as pd

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

    #print file_names

    directory_path = [TakeAPic_BASE_PATH + '/' + file_name for file_name in file_names]
    #print directory_path
    #
    df = GoogleFace_local.feed(directory_path)
    #dictionary = df.T.to_dict().values()
    #
    # sample = [{'name':'1'},{'name':'2'}]

    return flask.render_template('submissions_local.html', name="Analysis", tables = [df.head(len(df)).to_html()])
