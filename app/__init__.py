from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from config.config import Config

from werkzeug.utils import secure_filename
import os
import sqlite3
from flask.helpers import url_for

UPLOAD_FOLDER = '/app/static/files'

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def hello():
    return "hello there"
    
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, ssl_context='adhoc')

