from flask import Flask, request, jsonify

app = Flask(__name__)
cart = []

@app.route('/cart')
def get_cart():
    return jsonify(cart)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    item = request.get_json()
    cart.append(item)
    return jsonify({"message": "Item added", "cart": cart})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
