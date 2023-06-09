from flask import Flask, render_template, redirect, request
from flask import Blueprint
from repositories import product_repository
from repositories import manufacturer_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)