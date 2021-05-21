"""
W04 Prove : E-commerce System
Author: Nathan Johnston

:Product Class:
id : string
name : string
price : float
quantity : int
__init__(id, name, price, quantity)
get_total_price()
display()
"""


class Product:
    """ the product class, a single product and associated info """

    def __init__(self, product_id='', product_name='', product_price=0.0, product_quantity=0):
        """ set up initial product values """
        self.id = product_id
        self.name = product_name
        self.price = product_price
        self.quantity = product_quantity

    def get_total_price(self):
        """ Returns the price multiplied by the quantity """
        return self.price * self.quantity

    def display(self):
        """ displays product name, quantity, and total price in this format: 'Pencil (10) - $12.90' """
        print(f'{self.name} ({self.quantity}) - ${self.get_total_price():.2f}')
