from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for flashing messages
db = SQLAlchemy(app)

# Models
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))

# Routes
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
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')

    if not name or not email or not phone:
        flash("All customer fields are required!", "error")
        return redirect(url_for('customers'))

    try:
        new_customer = Customer(name=name, email=email, phone=phone)
        db.session.add(new_customer)
        db.session.commit()
        flash("Customer added successfully!", "success")
    except IntegrityError:
        db.session.rollback()
        flash("Error adding customer!", "error")

    return redirect(url_for('customers'))

@app.route('/orders')
def orders():
    order_list = Order.query.all()
    customer_list = Customer.query.all()  # To populate dropdown in the form
    return render_template('orders.html', orders=order_list, customers=customer_list)

@app.route('/add_order', methods=['POST'])
def add_order():
    customer_id = request.form.get('customer_id')
    product = request.form.get('product')
    status = request.form.get('status')

    if not customer_id or not product or not status:
        flash("All order fields are required!", "error")
        return redirect(url_for('orders'))

    customer = Customer.query.get(customer_id)
    if not customer:
        flash("Selected customer does not exist!", "error")
        return redirect(url_for('orders'))

    try:
        new_order = Order(customer_id=customer_id, product=product, status=status)
        db.session.add(new_order)
        db.session.commit()
        flash("Order added successfully!", "success")
    except IntegrityError:
        db.session.rollback()
        flash("Error adding order!", "error")

    return redirect(url_for('orders'))

@app.route('/report')
def report():
    total_customers = Customer.query.count()
    total_orders = Order.query.count()
    orders_list = Order.query.all()
    return render_template('report.html', customers=total_customers, orders=total_orders, orders_list=orders_list)

# Custom Error Handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    if not os.path.exists('database.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
