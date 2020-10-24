from flask import Flask, request, redirect, render_template, json, session, jsonify,url_for
from config.config import Config
from flask import send_file, send_from_directory, safe_join, abort

from app.board_generator import BoardGenerator

from werkzeug.utils import secure_filename
import os
import sqlite3
from flask.helpers import url_for

UPLOAD_FOLDER = '/app/static/files'

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["CLIENT_IMAGES"] = "/home/jyenterbriars/Server/app/static/client"


bg = BoardGenerator()
problem_pool = json.loads(open('app/problem_pool.json', "r").read())
#print(problem_pool)


@app.route('/', methods=['GET'])
def hello():
    return bg.generate("test")


@app.route("/get-image/<image_name>")
def get_image(image_name):

    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)



@app.route("/generate-board", methods=['POST'])
def generate():
    json_data = request.get_json()
    print(json_data['questions'])
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename="man.jpg", as_attachment=True)
    except FileNotFoundError:
        abort(404)
    
    
if __name__ == '__main__':
    app.run(debug=True)

