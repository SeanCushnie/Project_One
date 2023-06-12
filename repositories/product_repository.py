from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def save(product):
    sql = "INSERT INTO products (manufacturer_id, title, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.manufacturer.id, product.title, product.description, product.stock_quantity, product.buying_cost, product.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(manufacturer, result['title'],result['description'], result['stock_quantity'], result['buying_cost'],result['selling_price'],result['id'] )
    return product

# def select(id):
#     product = None
#     sql = "SELECT * FROM products WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         manufacturer = manufacturer_repository.select(result['manufacturer_id'])
#         product = Product(manufacturer, result['title'],result['description'], result['stock_quantity'], result['buying_cost'],result['selling_price'],result['id'])
#     return product


def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(manufacturer, row['title'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['id'])
        products.append(product)
    return products

def update(product):
    sql="UPDATE products SET (manufacturer_id, title, description, stock_quantity, buying_cost, selling_price) = (%s, %s, %s, %s, %s, %s) WHERE id =%s"
    values = [product.manufacturer.id, product.title, product.description, product.stock_quantity, product.buying_cost, product.selling_price]
    run_sql(sql, values)
