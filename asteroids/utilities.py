"""
File: utilities.py
Original Author: Nathan Johnston

File contains two basic utility classes, Point and Velocity

___Point()___
x : float
y : float
__init__()

___Velocity()___
dx : float
dy : float
__init__()
"""


class Point:
    """ The Point Class, which defines a co-ordinate pair on the SCREEN """

    def __init__(self, start_x: float = 0, start_y: float = 0):
        """ initiate values """
        self.x = start_x
        self.y = start_y


class Velocity:
    """ The Velocity Class, defines the speed and direction of an object's motion """

    def __init__(self, start_dx: float = 0, start_dy: float = 0):
        """ initiate values """
        self.dx = start_dx
        self.dy = start_dy
