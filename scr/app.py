from flask import Flask, jsonify, url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from cart_option import CartOption
from db import db
from route.home import home
from route.cart_route import cart_route

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:0123456789@localhost/sce_db?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    cartOption = CartOption(db=db)
    app.config['cartOption'] = cartOption
    app.register_blueprint(cart_route)
    app.register_blueprint(home)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug= True, port= 5000)