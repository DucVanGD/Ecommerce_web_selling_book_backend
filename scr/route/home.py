from flask import request, jsonify, Blueprint, current_app

home = Blueprint('home_route', __name__)


@home.route('/')
def homepage():
    return 'Trang chu'

