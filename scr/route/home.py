from flask import request, jsonify, Blueprint, current_app

routes = Blueprint('route', __name__)


@routes.route('/')
def homepage():
    return 'Trang chu'

@routes.route('/cart')
def Cartpage():
    return 'Gio hang'

@routes.route('/cart/<int:product_id>', methods=['GET', 'POST', 'DELETE'])
def cart(product_id=None):
    if request.method == 'GET':
        name = request.args.get('name')
        return current_app.config['cartOption'].get_Cart(p_id=int(product_id), p_name=name)
    
    if request.method == 'POST':
        product_id = request.json.get('product_id') 
        return current_app.config['cartOption'].add_Cart(product_id=int(product_id))
    
    if request.method == 'DELETE':
        product_id = request.args.get('product_id')  
        if product_id is not None:
            return current_app.config['cartOption'].delete_Cart(product_id=(product_id))
        else:
            return jsonify({"error": "Không tìm thấy sản phẩm"}), 400