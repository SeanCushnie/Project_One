from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository


def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        manufacturer = manufacturer_repository.select(result['id'])
        product = Product(manufacturer, result['title'],result['description'], result['stock_quantity'], result['buying_cost'],result['selling_price'],result['id'])
    return product


def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        manufacturer = manufacturer_repository.select(row['id'])