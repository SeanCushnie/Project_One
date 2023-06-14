import unittest 
from models.product import Product
from models.manufacturer import Manufacturer

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "EVXB/20L/LE", "floodlight",5,10,20)
        self.manufacturer = Manufacturer("Chalmit", 1)

    def test_product_has_manufacturer(self):
        self.assertEqual(1, self.product.manufacturer)
    
    def test_product_has_title(self):
        self.assertEqual("EVXB/20L/LE", self.product.title)
    
    def test_product_has_description(self):
        self.assertEqual("floodlight", self.product.description)
    
    def test_product_has_stock_quantity(self):
        self.assertEqual(5, self.product.stock_quantity)
    
    def test_product_has_buying_cost(self):
        self.assertEqual(10, self.product.buying_cost)
    
    def test_product_has_selling_price(self):
        self.assertEqual(20, self.product.selling_price)
    
    
    
