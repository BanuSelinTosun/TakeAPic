# Imports
import flask
import os
from werkzeug.utils import secure_filename    # Needed for image upload
import GoogleFace_local
import re
import pandas as pd
from StringIO import StringIO
import base64
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
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

    if len(uploaded_files) == 0:
        file_paths = []
        for the_file in os.listdir('./mini_jpg'):
            if the_file.split('.')[-1] == 'jpg':
                file_paths.append(str(the_file))
        directory_path = ['./mini_jpg/' + file_path for file_path in file_paths]

    else:
        file_paths = []
        for file in uploaded_files.getlist('file'):
            file.save('./static/uploads/' + str(file.filename).split('/')[-1])
            file_paths.append('./static/uploads/' + str(file.filename).split('/')[-1])

        directory_path = [TakeAPic_BASE_PATH + '/' + file_path for file_path in file_paths]

    df = GoogleFace_local.feed(directory_path)

    img_paths, img_names = GoogleFace_local.top_three(df)

    return flask.render_template('submissions_local.html', img_paths = img_paths, name="Analysis", tables = [df.head(len(df)).to_html()])
