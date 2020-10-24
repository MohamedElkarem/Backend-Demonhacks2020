from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from config.config import Config
from flask import send_file, send_from_directory, safe_join, abort

from werkzeug.utils import secure_filename
import os
import sqlite3
from flask.helpers import url_for

UPLOAD_FOLDER = '/app/static/files'

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CLIENT_IMAGES"] = "/home/jyenterbriars/Server/app/static/client"

@app.route('/', methods=['GET'])
def hello():
    return "hello there degenerate"


@app.route("/get-image/<image_name>")
def get_image(image_name):

    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)

    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, ssl_context='adhoc')

