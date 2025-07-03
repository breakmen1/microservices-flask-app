from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 49999},
        {"id": 2, "name": "Phone", "price": 19999}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
