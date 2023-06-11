from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository 

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Hawke")
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Chalmit")
manufacturer_repository.save(manufacturer_2)
manufacturer_repository.select_all()

product_1 = Product(manufacturer_1, "501/453/UNIV/A/M20/BRASS", "20mm gland, suitable for use in hazardous areas where cold-flow could be a potential issue", 10, 5, 15)
product_repository.save(product_1)
product_2 = Product(manufacturer_2, "EVXB/20/LE", "Non-Emergency Floodlight, Zone 1, 20,980lm", 5, 2500, 3500)
product_repository.save(product_2)
product_3 = Product(manufacturer_2, "EVXB/10/LE", "Non-Emergency Floodlight, Zone 1, 20,980lm", 0, 2500, 3500)
product_repository.save(product_3)
manufacturer_repository.select_all()