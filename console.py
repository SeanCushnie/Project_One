from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository 

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Hawke")
manufacturer_repository.save("manufacturer_1")
manufacturer_2 = Manufacturer("Chalmit")
manufacturer_repository.save("manufacturer_2")
manufacturer_repository.select_all