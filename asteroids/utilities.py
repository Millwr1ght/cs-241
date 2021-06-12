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
        self._x = start_x
        self._y = start_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


class Velocity:
    """ The Velocity Class, defines the speed and direction of an object's motion """

    def __init__(self, start_dx: float = 0, start_dy: float = 0):
        """ initiate values """
        self.dx = start_dx
        self.dy = start_dy

    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, value):
        self._dx = value

    @property
    def dy(self):
        return self._dy

    @dy.setter
    def dy(self, value):
        self._dy = value

    def increment_dx(self, value):
        """ increase horizontal vector magnitude, maintain semblance of direction """
        if self._dx > 0:
            self._dx += value
        else:
            self._dx -= value

    def increment_dy(self, value):
        """ increase vertical vector magnitude, maintain semblance of direction """
        if self._dy > 0:
            self._dy += value
        else:
            self._dy -= value
