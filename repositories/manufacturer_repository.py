from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product


def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name) VALUES (%s) RETURNING *"
    values = [manufacturer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer


def select(id):
    Manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        manufacturer = Manufacturer(result['name'],result['id'] )
    return manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturer"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers