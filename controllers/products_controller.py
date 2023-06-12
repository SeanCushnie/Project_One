from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import product_repository
from repositories import manufacturer_repository
from models.product import Product
import pdb

products_blueprint = Blueprint("products", __name__)



@products_blueprint.route("/")
def index():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)



@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", product_list = products)



@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    if product is not None:
        return render_template('products/show.html', product=product)
    else:
        return redirect("/products")
    

    
@products_blueprint.route("/products/<id>/edit", methods = ['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product = product, all_manufacturers = manufacturers)


@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    # pdb.set_trace()
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    title = request.form['title']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    product = Product(manufacturer, title, description, stock_quantity, buying_cost, selling_price, id)
    print(product.manufacturer.name)
    product_repository.update(product)
    return redirect('/products')