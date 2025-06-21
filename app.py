from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# PostgreSQL connection via Render Environment Variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Optional: Silence deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    product = db.Column(db.String(100))
    status = db.Column(db.String(20))

@app.route('/')
def dashboard():
    total_customers = Customer.query.count()
    total_orders = Order.query.count()
    return render_template('dashboard.html', customers=total_customers, orders=total_orders)

@app.route('/customers')
def customers():
    customer_list = Customer.query.all()
    return render_template('customers.html', customers=customer_list)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    new_customer = Customer(name=name, email=email, phone=phone)
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for('customers'))

@app.route('/orders')
def orders():
    order_list = Order.query.all()
    return render_template('orders.html', orders=order_list)

@app.route('/add_order', methods=['POST'])
def add_order():
    customer_id = request.form['customer_id']
    product = request.form['product']
    status = request.form['status']
    new_order = Order(customer_id=customer_id, product=product, status=status)
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for('orders'))

@app.route('/report')
def report():
    total_customers = Customer.query.count()
    total_orders = Order.query.count()
    orders_list = Order.query.all()
    return render_template('report.html', customers=total_customers, orders=total_orders, orders_list=orders_list)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensures tables are created in PostgreSQL
    app.run(debug=True)
