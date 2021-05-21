"""
W04 Prove : E-commerce System
Author: Nathan Johnston

:Customer Class:
id : string
name : string
orders : Order[]
__init__()
get_order_count()
get_total()
add_order(order)
display_summary()
display_receipts()
"""

from order import Order


class Customer:
    """ the Customer Class, a list of Orders and associated info and methods """

    def __init__(self, customer_id='', customer_name=''):
        """ sets up the default customer initialization """
        self.id = customer_id
        self.name = customer_name
        self.orders = []

    def get_order_count(self):
        """ Returns the number of orders """
        return len(self.orders)

    def get_total(self):
        """ Returns the total price of all orders combined """
        total = 0
        for order in self.orders:
            total += order.get_total()

        return total

    def add_order(self, order):
        """ Adds the provided order to the list of orders """
        self.orders.append(order)

    def display_summary(self):
        """ display a summary of the customer's data """
        print(f'Summary for customer \'{self.id}\':')
        print(f'Name: {self.name}')
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: ${self.get_total():.2f}')

    def display_receipts(self):
        """ Displays all the orders' receipts as follows: """
        print(f'Detailed receipts for customer \'{self.id}\':')
        print(f'Name: {self.name}')
        for order in self.orders:
            print() #skip a line between orders
            order.display_receipt()
