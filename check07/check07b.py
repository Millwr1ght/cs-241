"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

from abc import ABC, abstractmethod
# from math import pi # but nooooo, this is wroooong
pi = 3.14


class Shape(ABC):
    def __init__(self):
        self.name = ""

    def display(self):
        print(f"{self.name} - {self.get_area():.2f}")

    # TODO: Add an abstractmethod here called get_area
    @abstractmethod
    def get_area(self):
        """ """
        raise ConnectionError('overriden method necessary')


class Circle(Shape):
    """ """

    def __init__(self, Radius: float = 0.0):
        """ variable setup"""
        super().__init__()

        self.name = 'Circle'
        self.radius = Radius

    def get_area(self):
        """ return 3.14 * radius * radius """
        return pi * (self.radius ** 2)


class Rectangle(Shape):
    """ """

    def __init__(self, Length: float = 0.0, Width: float = 0.0):
        """ variable setup"""
        super().__init__()

        self.name = 'Rectangle'
        self.length = Length
        self.width = Width

    def get_area(self):
        """ return lxw"""
        return self.width * self.length


def main():

    shapes = []
    command = ""

    while command != "q":
        command = input(
            "Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            c = Circle(radius)
            shapes.append(c)

        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            r = Rectangle(length, width)
            shapes.append(r)

    # Done entering shapes, now lets print them all out:
    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()
