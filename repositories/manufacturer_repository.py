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
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results: 
        result = results[0]
        manufacturer = Manufacturer(result['name'], result['id'])
    return manufacturer


def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(row['name'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def update(manufacturer):
    sql="UPDATE manufacturers SET name = (%s) WHERE id =%s"
    values = [manufacturer.name, manufacturer.id]
    # print(values)
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)