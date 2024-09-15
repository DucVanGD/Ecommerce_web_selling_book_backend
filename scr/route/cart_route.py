from flask import request, jsonify, Blueprint, current_app

cart_route = Blueprint('cart_route', __name__)

@cart_route.route('/cart/all')
def Cartpage():
    return current_app.config['cartOption'].get_Cart()
@cart_route.route('/cart', defaults={'product_id': None}, methods=['GET', 'POST', 'DELETE'])
@cart_route.route('/cart/<product_id>', methods=['get', 'post', 'delete'])
def cart(product_id=0):
    if request.method == 'GET':
        return current_app.config['cartOption'].get_Cart(p_id=product_id)
    
    if request.method == 'POST':
        return current_app.config['cartOption'].add_Cart(product_id  = product_id)
    
    if request.method == 'DELETE':
            return current_app.config['cartOption'].delete_Cart(product_id = product_id)