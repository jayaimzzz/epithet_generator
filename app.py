
__author__ = "jayaimzzz"

import os 
from flask import jsonify, Flask, request
from dotenv import load_dotenv
from backend_epithet_generator.helpers import Vocabulary, EpithetGenerator

app = Flask(__name__)
path = os.path.abspath(".env")
load_dotenv(path) #fwiw, load_dotenv seems to work without a pathname
FLASK_APP = os.environ.get("FLASK_APP")
FLASK_ENV = os.environ.get("FLASK_ENV")

e_gen = EpithetGenerator()


@app.route('/')
def index():
    random_epithet = e_gen.get_epithets(1)
    dict_ = {"epithets": random_epithet}
    return jsonify(dict_)

@app.route('/vocabulary')
def vocabulary():
    dict_ = {"vocabulary": e_gen.vocab}
    return jsonify(dict_)

@app.route('/epithets/<qty>')
def epithets(qty):
    epithets = e_gen.get_epithets(int(qty))
    dict_ = {"epithets": epithets}
    return jsonify(dict_)
