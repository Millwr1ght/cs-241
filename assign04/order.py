"""
W04 Prove : E-commerce System
Author: Nathan Johnston

:Order Class:
id : string
products : Product[]
__init__()
get_subtotal()
get_tax()
get_total()
add_product(product)
display_receipt()
"""

from product import Product


class Order:
    """ the Order class, a list of Product instances and associated info """

    def __init__(self, order_id=''):
        """ """
        self.id = order_id
        self.products = []

    def get_subtotal(self):
        """ Sums the price of each product and returns it """
        subtotal = 0
        for product in self.products:
            subtotal += product.get_total_price()

        return subtotal

    def get_tax(self):
        """ Returns 6.5% times the subtotal """
        return self.get_subtotal() * 0.065  # 6.5% tax --> subtotal * 0.065

    def get_total(self):
        """ Returns the subtotal plus the tax """
        return self.get_subtotal() + self.get_tax()

    def add_product(self, product):
        """ Adds the provided product to the list """
        self.products.append(product)

    def display_receipt(self):
        """ Displays a receipt in this format: Order: 1138 \ Sword (10) - $18999.90 \ Shield (6) - $5938.50 \ Subtotal: $2889.74 \ Tax: $187.83 \ Total: $3077.57 """
        print(f'Order: {self.id}')
        for product in self.products:
            product.display()
        print(f'Subtotal: ${self.get_subtotal():.2f}')
        print(f'Tax: ${self.get_tax():.2f}')
        print(f'Total: ${self.get_total():.2f}')
