"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import math
from abc import ABC, abstractmethod

# class imports
import utilities  # Point, Velocity classes


# .\images\
player = './images/playerShip1_orange.png'
meteor_big = './images/meteorGrey_big1.png'
meteor_med = './images/meteorGrey_med1.png'
meteor_small = './images/meteorGrey_small1.png'
laser = './images/laserBlue01.png'

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Asteroids | Nathan Johnston'

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


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
    is_off_screen(screen_width, screen_height) : Boolean
    wrap_around() : None
    """

    def __init__(self, x: int = 0, y: int = 0, dx: float = 0, dy: float = 0, radius: int = 10, angle: float = 0):
        """ initialize object values """
        self.center = Point(start_x=x, start_y=y)
        self.velocity = Velocity(dx, dy)
        self.alive = True
        self.radius = radius
        self.angle = angle
        self.texture_file = None  # reassign this in subclasses

    def advance(self):
        """ Move the object across the field """
        # move dx, dy units
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):
        """ Draw self on field """
        texture = arcade.load_texture(self.texture_file)

        width = texture.width
        height = texture.height
        alpha = 255  # For transparency, 255 means not transparent

        arcade.draw_texture_rectangle(
            self.center.x, self.center.y, width, height, self.texture, self.angle, alpha)

    def rotate(self, value):
        """ rotate the moving object """
        self.angle += value

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


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.player = None

        self.lasers = []

        self.asteroids = []

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object

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
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            pass

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
