
__author__ = "jayaimzzz"

import os 
from flask import jsonify, Flask 
from dotenv import load_dotenv


app = Flask(__name__)
path = os.path.abspath(".env")
load_dotenv(path) #fwiw, load_dotenv seems to work without a pathname
FLASK_APP = os.environ.get("FLASK_APP")
FLASK_ENV = os.environ.get("FLASK_ENV")


@app.route('/')
def index():
    dict_ = {"epithets": []}
    return jsonify(dict_)

@app.route('/vocabulary')
def vocabulary():
    dict_ = {"vocabulary": {}}
    return jsonify(dict_)
