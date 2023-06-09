from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import product_repository
from repositories import manufacturer_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/")
def index():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", product_list = products)