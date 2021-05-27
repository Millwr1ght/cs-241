"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others

Others being: N. Johnston

This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


class Point:
    """ The Point Class, defines a co-ordinate pair on the SCREEN """

    def __init__(self, start_x=0, start_y=0):
        """ initiate values """
        self.x = start_x
        self.y = start_y


class Velocity:
    """ The Velocity Class, defines the speed and direction of an object's motion """

    def __init__(self, start_dx=uniform(0.01, 4), start_dy=uniform(-2, 2)):
        """ initiate values """
        self.dx = start_dx
        self.dy = start_dy

    def increment(self, value):
        """ increase vector magnitude, maintain semblance of direction """
        if self.dx > 0:
            self.dx += value
        else:
            self.dx += -value
        if self.dy > 0:
            self.dy += value
        else:
            self.dy += -value


class FlyingObject:
    """ These 'fly' across the playing field, and die when they reach The Other Side 

    center : Point
    velocity : Velocity
    radius : float
    __init__()
    advance() : None
    draw() : None
    is_off_screen(screen_width, screen_height) : Boolean
    """

    def __init__(self):
        """ initialize object values """
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 10

    def advance(self, value):
        """ Move the object across the field """
        self.velocity.increment(value)

    def draw(self):
        """ Draw self on field """
        arcade.draw_circle_outline(
            self.center.x, self.center.y, self.radius, TARGET_COLOR)

# class Bullet:
# class Target:
# class StrongTarget(Target):
# class StandardTarget(Target):
# class SafeTarget(Target):


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """

    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360-self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        spawn_type = random.uniform(-2, 7)

        # low type == low points
        if spawn_type < 0:
            target = SafeTarget()
        # high grade == many points
        elif spawn_type > 5:
            target = StrongTarget()
        else:
            target = StandardTarget()

        # TODO: add trajectory

        # TODO: add target to the queue

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ stuff done when the mouse moves """

        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ clickety clickety clickety """

        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    @staticmethod
    def _get_angle_degrees(x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This is a static method.
        We haven't discussed them yet.
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()