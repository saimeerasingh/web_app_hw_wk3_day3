from app import app
from flask import render_template
from models.customer_details import *

@app.route('/orders')
def index():
   return render_template('index.html', name = 'Icecream Truck', customers=customers)

@app.route('/orders/<index>')
def orders(index):
    order = customers[int(index)]
    return render_template('order.html', name = 'Customer Orders', order=order)
    
#in this function pass in a variable, the variable comes from the path
#in the function, select customer by index
#get rid of the for loop in html
