""" 
W06 Team.py v2
Circles

Authors: Nathan, Tode
"""


class Point:
    """ 
    x : float
    y : float
    prompt_for_point() : None
    display() : None
    """

    def __init__(self):
        """ setup variables """
        self.x = 0.0
        self.y = 0.0

    def prompt_for_point(self):
        """ get x, y"""
        self.x = float(input('Enter X: '))
        self.y = float(input('Enter Y: '))

    def display(self):
        """ show x,y """
        print(f'Center:\n({self.x:.2f}, {self.y:.2f})')


class Circle:
    """ the circle class """

    def __init__(self):
        """ setting up the variables """

        # normal stuff
        self.radius = 0.0
        self.center = Point()

    def prompt_for_circle(self):
        """ to get all the circle info: x, y, radius """
        self.center.prompt_for_point()
        self.radius = float(input('Enter radius: '))

    def display(self):
        """
        Center:
        (1, 2)
        Radius: 3
        """
        self.center.display()
        print(f'Radius: {self.radius:.2f}')


def main():
    """ main function """
    # make a circle
    circle = Circle()

    # ask for info
    circle.prompt_for_circle()

    # display values
    circle.display()


if __name__ == '__main__':
    main()
