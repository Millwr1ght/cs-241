from moving_objects import MovingObject
import math

# globals
BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60


class Laser:
    """ the laser class
    these fire from the ship, and hit meteors/asteroids/rocks

    - lifespan:int = BULLET_LIFE
    - radius = BULLET_RADIUS
    - texture_file = LASER

    - __init__() : None
    + fire() : None
    """

    def __init__(self, x, y, angle: float):
        """ setup attributes """
        # get that moving object
        super().__init__(angle=angle)

        self.lifespan = BULLET_LIFE
        self.move_speed = BULLET_SPEED
        self.radius = BULLET_RADIUS

    def fire(self, angle: float):
        """ shoot the laser based on the given angle, in degrees
        """
        self.velocity.dx = math.cos(math.radians(
            angle)) * self.move_speed
        self.velocity.dy = math.sin(math.radians(
            angle)) * self.move_speed
