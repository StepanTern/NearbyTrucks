from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/customers')
def customers():
    return render_template('customers.html')


if __name__ == '__main__':
    app.run(port=8080, host='localhost', debug=True)
