""" 
File: moving_objects.py
Author: Nathan Johnston

base class for moving objects for the asteroids.py arcade game
"""

# class and method imports
from utilities import Point, Velocity
from arcade import load_texture, draw_texture_rectangle
import math


class MovingObject:
    """ These objects move across the playing field
    When they reach The Other Side, they: wrap

    ___MovingObject()___
    center : Point()
    velocity : Velocity()
    radius : int
    alive : Boolean
    texture_file : str
    angle : float

    __init__()
    advance() : None
    draw() : None
    rotate() : None
    is_off_screen(width, height) : Boolean
    wrap_around(width, height) : None
    not_alive() : None
    """

    def __init__(self, x: int = 0, y: int = 0, dx: float = 0, dy: float = 0, radius: int = 10, angle: float = 0):
        """ initialize object values """
        self.center = Point(start_x=x, start_y=y)
        self.velocity = Velocity(dx, dy)
        self.alive = True
        self.radius = radius
        self.angle = angle
        self.rotation_speed = 0
        self._texture_file = None  # reassign this in subclasses

    def advance(self):
        """ Move the object across the field """
        # move dx, dy units
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):
        """ Draw self on field """
        texture = load_texture(self._texture_file)

        width = texture.width
        height = texture.height
        alpha = 255  # For transparency, 255 means not transparent

        draw_texture_rectangle(
            self.center.x, self.center.y, width, height, texture, self.angle, alpha)

    def rotate(self):
        """ increment angle by rotation speed """
        pass

    def is_off_screen(self, width, height):
        """ checks if the object has left the premises 
        returns : Boolean
        """
        return self.center.x > width or self.center.y > height or self.center.x < 0 or self.center.y < 0

    def wrap_around(self, width, height):
        """ checks what bounds the object has crossed and fixes it"""
        # horizontal
        if self.center.x > width:
            self.center.x = self.radius
        elif self.center.x < 0:
            self.center.x = width - self.radius

        # vertical
        if self.center.y > height:
            self.center.y = self.radius
        elif self.center.y < 0:
            self.center.y = height - self.radius

    def not_alive(self):
        """ commit alt+F4 """
        self.alive = False

    @staticmethod
    def _get_x_y_from_angle(angle, length):
        """ 
        get the x and y co-ordinates from a length and an angle
        particularly from the angle and a length 
        so we can spawn lasers at the end of the ship
        """
        angle_radians = math.radians(angle)

        x = length * math.cos(angle_radians)
        y = length * math.sin(angle_radians)

        return x, y
