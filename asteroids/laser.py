from moving_objects import MovingObject
import math

# globals
BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

# texture
LASER = './resouces/images/laserBlue01.png'


class Laser(MovingObject):
    """ the laser class
    these fire from the ship, and hit meteors/asteroids/rocks

    - lifespan:int = BULLET_LIFE
    - radius = BULLET_RADIUS
    - texture_file = LASER

    - __init__() : None
    + fire() : None
    """

    def __init__(self, x, y, file: str = LASER):
        """ setup attributes """
        # get that moving object
        super().__init__(x, y)

        self._texture_file = file
        self.lifespan = BULLET_LIFE
        self.move_speed = BULLET_SPEED
        self.radius = BULLET_RADIUS

    def advance(self):
        """ Move the object across the field """
        # move dx, dy units
        super().advance()

        self.lifespan -= 1
        if self.lifespan <= 0:
            self.not_alive()

    def fire(self, ship_velocity, angle: float):
        """
        shoot the laser based on the given angle, in degrees
        """
        angle = angle + 90
        self.velocity.dx = ship_velocity.dx + math.cos(math.radians(
            angle)) * self.move_speed
        self.velocity.dy = ship_velocity.dy + math.sin(math.radians(
            angle)) * self.move_speed
        self.angle = angle
