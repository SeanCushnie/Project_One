import unittest 
from models.product import Product
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "EVXB/20L/LE", "floodlight",5,10,20)
        self.manufacturer = Manufacturer("Chalmit", 1)

    def test_manufacturer_has_name(self):
        self.assertEqual("Chalmit", self.manufacturer.name)

    def test_manufacturer_has_id(self):
        self.assertEqual(1, self.manufacturer.id)
    
    def test_manufacturer_links_with_product_via_id(self):
        self.assertEqual(1, self.product.manufacturer)