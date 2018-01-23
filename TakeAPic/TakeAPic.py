# Imports
import flask
import os
from werkzeug.utils import secure_filename    # Needed for image upload
import GoogleFace
import re

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

@app.route('/', methods = ['GET', 'POST'])
def index():
    method = flask.request.method

    if method == 'POST':
        # Do processing
        file = flask.request.files['file']
        print(file.filename)

        file_path = TakeAPic_BASE_PATH + '/jpg/' + file.filename
        print 'the file path is ', file_path

        hap, sad, ang, sur = GoogleFace.main(file_path)
        number_string = str(hap) + " " + str(sad) + " " + str(ang) + " " + str(sur) + " "
        return flask.redirect(flask.url_for('submissions', listOfObjects = number_string))

    elif method == 'GET':
        return flask.render_template('index.html')

@app.route('/submissions', methods = ['GET'])
def submissions():
    emotions = flask.request.args.get('listOfObjects')
    strings = re.findall("\d+\.\d+", emotions)
    return flask.render_template('submissions.html', hap=strings[0], sad=strings[1], ang=strings[2], sur=strings[3])
