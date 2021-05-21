"""
W04 Prove : E-commerce System
Author: Nathan Johnston
"""

# #

"""
:Product Class:
id : string
name : string
price : float
quantity : int
__init__(id, name, price, quantity)
get_total_price()
display()
"""




from order import Order
from product import Product
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

# #


"""
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

# #


"""
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
            print()  # skip a line between orders
            order.display_receipt()


# #

""" 
Common issues and explanations:

Order.add_products()
  - most people in this weeks help channel had problems with this
  - this method needs to accept two arguments: self, and the one main.py passes to it: a product instance

the Order class has a list[] of Product instances, and the Customer class has a list[] of Order instances
  - e.g: Order.products --> [p1, p2, p3, ...] and Customer.orders --> [o1, o2, o3, ...]

general class method use:
  - when calling the method, you shouldn't need to pass self as an argument
  - when you are defining it in the class, it should be set as the first parameter
  - if the method has more (non-default) paramenters, you pass that many arguments when calling that method elsewhere


"""