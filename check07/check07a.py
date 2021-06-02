"""
File: check07a.py

Starting template for your checkpoint assignment.

Author: Nathan Johsnton
"""


# : Create a base car class here
class Car:
    """ the Car class.
    name : string
    __init__()
    get_door_specs() : string
    """

    def __init__(self):
        """ inititalize """
        self.name = ''

    def get_door_specs(self):
        """ """
        return 'Unknown door specs'


# : Create a civic class here
class Civic(Car):
    """ the honda civic class
    name : str
    __init__()
    get_door_specs() : "4 doors"
    """

    def __init__(self):
        """ variable setup"""
        super().__init__()

        self.name = 'Civic'

    def get_door_specs(self):
        """ retruns a specific str """
        return "4 doors"


# : Create an Odyssey class here
class Odyssey(Car):
    """ the honda odyssey class 
    name : str
    __init__()
    get_door_specs() : "2 front doors, 2 sliding doors, 1 tail gate"
    """

    def __init__(self):
        """ variable setup"""
        super().__init__()

        self.name = 'Odyssey'

    def get_door_specs(self):
        """ retruns a specific str """
        return "2 front doors, 2 sliding doors, 1 tail gate"


# : Create a Ferrari class here
class Ferrari(Car):
    """ the ferrari class
    name : str
    __init__()
    get_door_specs() : "2 butterfly doors"
    """

    def __init__(self):
        """ variable setup"""
        super().__init__()

        self.name = 'Ferrari'

    def get_door_specs(self):
        """ retruns a specific str """
        return "2 butterfly doors"

# : Create attach_doors() function (not a class method or therwise part of a class)


def attach_doors(car):
    """ 
    should accept any type of car and display the text: "Attaching doors to {name} - {doors}".
    """
    print(f'Attaching doors to {car.name} - {car.get_door_specs()}')


def main():
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)


if __name__ == "__main__":
    main()
