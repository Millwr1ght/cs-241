"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import ship
import arcade
import math
from abc import ABC, abstractmethod

# .\images\
PLAYER = './images/playerShip1_orange.png'
ROCK_BIG = './images/meteorGrey_big1.png'
ROCK_MED = './images/meteorGrey_med1.png'
ROCK_SMALL = './images/meteorGrey_small1.png'
LASER = './images/laserBlue01.png'

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
        self.score = 0
        self.player = Ship(radius=SHIP_RADIUS)

        self.lasers = []

        self.asteroids = []  # starts with five(5) Big Rocks

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        self.player.draw()

        for laser in self.lasers:
            laser.draw()

        for rock in self.asteroids:
            rock.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = f"Score: {self.score}"
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.WHITE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Check for collisions
        self.check_collisions()
        self.check_off_screen()

        # TODO: Tell everything to advance or move forward one step in time

    def check_collisions(self):
        """
        Checks to see if lasers have hit asteroids.
        Updates scores and removes dead items.
        :return:
        """

        for laser in self.lasers:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if laser.alive and asteroid.alive:
                    too_close = laser.radius + asteroid.radius

                    if (abs(laser.center.x - asteroid.center.x) < too_close and
                            abs(laser.center.y - asteroid.center.y) < too_close):
                        # its a hit!

                        laser.not_alive()
                        self.score += asteroid.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_debris()

    def cleanup_debris(self):
        """
        Removes any dead lasers or asteroids from the list.
        :return:
        """
        for laser in self.lasers:
            if not laser.alive:
                self.lasers.remove(laser)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def check_off_screen(self):
        """
        Checks to see if lasers or asteroids have left the screen
        and if so, moves them to the other side of the screen.
        :return:
        """
        for laser in self.lasers:
            if laser.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                laser.wrap_around()

        for asteroid in self.asteroids:
            if asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                asteroid.wrap_around()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            # rotate ship counterclockwise
            pass

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            # rotate ship clockwise
            pass

        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            # move ship forward
            pass

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            # slow down ship
            pass

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the laser.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the laser here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    @staticmethod
    def _get_coords_from_angle(angle, length):
        """ 
        get the x and y co-ordinates from a length and an angle
        particularly from the angle and a length 
        so we can spawn lasers at the end of the ship
        """
        angle_radians = math.radians(angle)

        x = length * math.cos(angle_radians)
        y = length * math.sin(angle_radians)

        return x, y


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
