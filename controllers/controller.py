from app import app
from flask import render_template
from models.customer_details import *

@app.route('/customers')
def index():
   return render_template('index.html', name = 'Icecream Truck', customers=customers)
