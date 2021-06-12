import utilities  # Point, Velocity classes
from abc import ABC, abstractmethod


class MovingObject(ABC):
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
    is_off_screen(screen_width, screen_height) : Boolean
    wrap_around() : None
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
        texture = arcade.load_texture(self._texture_file)

        width = texture.width
        height = texture.height
        alpha = 255  # For transparency, 255 means not transparent

        arcade.draw_texture_rectangle(
            self.center.x, self.center.y, width, height, self.texture, self.angle, alpha)

    def rotate(self):
        """ increment angle by rotation speed """
        self.angle += self.rotation_speed

    def is_off_screen(self):
        """ checks if the object has left the premises 
        returns : Boolean
        """
        return self.center.x > SCREEN_WIDTH or self.center.y > SCREEN_HEIGHT or self.center.x < 0 or self.center.y < 0

    def wrap_around(self):
        """ checks what bounds the object has crossed and fixes it"""
        # horizontal
        if self.center.x > SCREEN_WIDTH:
            self.center.x = self.radius
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH - self.radius

        # vertical
        if self.center.x > SCREEN_WIDTH:
            self.center.x = self.radius
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH - self.radius

    def not_alive(self):
        """ commit alt+F4 """
        self.alive = False
