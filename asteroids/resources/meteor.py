from moving_objects import MovingObject
from abc import ABC, abstractmethod

# global constants
BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

# textures
ROCK_BIG = './resources/images/meteorGrey_big1.png'
ROCK_MEDIUM = './resources/images/meteorGrey_med1.png'
ROCK_SMALL = './resources/images/meteorGrey_small1.png'


class Meteor(MovingObject, ABC):
    """ the abstract class for moving space rocks 

    rotation_speed : int
    move_speed : int

    - __init__() : None
    + hit() : int
    - rotate() : None
    """

    def __init__(self, start_x, start_y, radius: int, turn_amount: int, thrust: int = BIG_ROCK_SPEED):
        """ setup class attributes """
        # get the fancy moving object stuff
        super().__init__(x=start_x, y=start_y, radius=radius)

        self.rotation_speed = turn_amount
        self.move_speed = thrust

    def advance(self):
        """ Move the object across the field """
        # move dx, dy units
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

        self.rotate()

    def rotate(self):
        """ increment angle by rotation speed """
        self.angle += self.rotation_speed

    @abstractmethod
    def hit(self):
        """ what happens when the meteor gets hit """
        pass


class BigMeteor(Meteor):
    """ the class of large rocks

    - rotation_speed = BIG_ROCK_SPIN
    - radius = BIG_ROCK_RADIUS
    - texture_file = ROCK_BIG

    - __init__() : None
    + hit() : int
    """

    # for spawning in rocks
    radius = BIG_ROCK_RADIUS

    def __init__(self, start_x, start_y, angle: float, radius: int = BIG_ROCK_RADIUS, turn_amount: int = BIG_ROCK_SPIN, file: str = ROCK_BIG):
        """ setup attributes """
        super().__init__(start_x, start_y, radius, turn_amount)

        self._texture_file = file
        self.angle = angle
        start_dx, start_dy = self._get_x_y_from_angle(
            self.angle, self.move_speed)
        self.velocity.dx = start_dx
        self.velocity.dy = start_dy

    def hit(self):
        """ what happens when you shoot a large asteroid?
        it breaks apart and becomes two medium asteroids and one small one.
        The first medium asteroid has the same velocity as the original large one 
            plus 2 pixel/frame in the up direction.
        The second medium asteroid has the same velocity as the original large one
            plus 2 pixel/frame in the down direction.
        The small asteroid has the original velocity plus 5 pixels/frame to the right.

        :returns: int (score for hit), list
        """
        new_meteors = []

        # first broken piece
        medium_1 = MedMeteor(self.center.x, self.center.y)
        medium_1.velocity.dy = self.velocity.dy + 2
        new_meteors.append(medium_1)

        # second broken piece
        medium_2 = MedMeteor(self.center.x, self.center.y)
        medium_2.velocity.dy = self.velocity.dy - 2
        new_meteors.append(medium_2)

        # third broken piece
        small = SmallMeteor(self.center.x, self.center.y)
        small.velocity.dx = self.velocity.dx + 5
        new_meteors.append(small)

        return 1, new_meteors


class MedMeteor(Meteor):
    """ the class of less large rocks

    - rotation_speed = MEDIUM_ROCK_SPIN
    - radius = MEDIUM_ROCK_RADIUS
    - texture_file = ROCK_MEDIUM

    - __init__() : None
    + hit() : int
    """

    def __init__(self, start_x, start_y, radius: int = MEDIUM_ROCK_RADIUS, turn_amount: int = MEDIUM_ROCK_SPIN, file: str = ROCK_MEDIUM):
        """ setup attributes """
        super().__init__(start_x, start_y, radius, turn_amount)

        self._texture_file = file

    def hit(self):
        """ what happens when you shoot a medium asteroid?
        it breaks apart and becomes two small asteroids.
        The small asteroid has the same velocity as the original medium one 
            plus 1.5 pixels/frame up and 1.5 pixels/frame to the right.
        The second, 1.5 pixels/frame down and 1.5 to the left.

        :returns: int, list
        """
        new_meteors = []

        # small debris chunk #1
        small_1 = SmallMeteor(self.center.x, self.center.y)
        small_1.velocity.dx = self.velocity.dx + 1.5  # to the right
        small_1.velocity.dy = self.velocity.dy + 1.5  # to the up
        new_meteors.append(small_1)

        # small debris chunk #2
        small_2 = SmallMeteor(self.center.x, self.center.y)
        small_2.velocity.dx = self.velocity.dx - 1.5  # to the left
        small_2.velocity.dy = self.velocity.dy - 1.5  # to the down
        new_meteors.append(small_2)

        return 3, new_meteors


class SmallMeteor(Meteor):
    """ the class of the smallest "large" rocks

    - rotation_speed = SMALL_ROCK_SPIN
    - radius = SMALL_ROCK_RADIUS
    - texture_file = ROCK_SMALL

    - __init__() : None
    + hit() : int, list
    """

    def __init__(self, start_x, start_y, radius: int = SMALL_ROCK_RADIUS, turn_amount: int = SMALL_ROCK_SPIN, file: str = ROCK_SMALL):
        """ setup attributes """
        super().__init__(start_x, start_y, radius, turn_amount)

        self._texture_file = file

    def hit(self):
        """ what happens when you shoot a small asteroid?
        it is destroyed and removed from the game.

        :returns: int (score for hit), list of new_meteors
        """
        self.not_alive()
        return 5, []
