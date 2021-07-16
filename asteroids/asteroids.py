"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

Completed by: N Johnston, Millwr1ght

This program implements the asteroids game.
"""
import arcade
from math import radians, sin, cos
from random import uniform, randint
from resources.ship import Ship
from resources.meteor import BigMeteor
from resources.laser import Laser
from resources.music_player import MusicPlayer
""" 
Ideas of what to add:
 -- Explosion death animation
 -- Pause/Game Over screens
 -- Lives system (maybe a 3-5 lives then death/game over sort of thing)
 -- Save highscore in an external text/JSON file
"""

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Asteroids'

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30
SHIP_TEXTURE = './resources/images/playerShip1_orange.png'

INITIAL_ROCK_COUNT = 5

# sound fx
LASER_FIRE = './resources/sounds/laser-fire.wav'
ASTEROID_CRUNCH = './resources/sounds/asteroid-crunch.wav'

# background music
MUSIC_VOLUME = 0.75
SONG_LIST = [
    "./resources/sounds/No Place to Hide.mp3",
    "./resources/sounds/Everpresence.mp3",
    "./resources/sounds/Genesis of the End.mp3"
]


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height, title):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # game variables and counters
        self.score = 0
        self.highscore = 0
        self.firing_delay = 10  # Machine gun bullet frame delay counter
        self.debug = False

        # game objects
        self.ship = Ship(start_x=SCREEN_WIDTH//2,
                         start_y=SCREEN_HEIGHT//2,
                         radius=SHIP_RADIUS,
                         turn_amount=SHIP_TURN_AMOUNT,
                         thrust=SHIP_THRUST_AMOUNT,
                         file=SHIP_TEXTURE)
        self.lasers = []
        self.asteroids = []

        # game starts with five(5) Big Rocks
        self.spawn_asteroids(INITIAL_ROCK_COUNT)

        # music
        self.music_player = MusicPlayer(MUSIC_VOLUME, SONG_LIST)
        self.music_player.setup()

        # sound effects
        self.laser_sound = arcade.load_sound(LASER_FIRE)
        self.asteroid_sound = arcade.load_sound(ASTEROID_CRUNCH)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # the player
        self.score = 0
        self.ship = Ship(start_x=SCREEN_WIDTH//2,
                         start_y=SCREEN_HEIGHT//2,
                         radius=SHIP_RADIUS,
                         turn_amount=SHIP_TURN_AMOUNT,
                         thrust=SHIP_THRUST_AMOUNT,
                         file=SHIP_TEXTURE)

        # the lasers and asteroids
        self.lasers = []
        self.asteroids = []

        # game starts with five(5) Big Rocks
        self.spawn_asteroids(INITIAL_ROCK_COUNT)

    def spawn_asteroids(self, count: int = 1):
        """ create asteroids to play with """
        # define where asteroids can't spawn, i.e. within the ship's hitbox
        too_close = self.ship.radius + BigMeteor.radius

        # Big Meteors
        for _ in range(count):
            # reset start values
            spawn_x = self.ship.center.x
            spawn_y = self.ship.center.y

            # find new ones far away
            while (abs(self.ship.center.x - spawn_x) < too_close and
                   abs(self.ship.center.y - spawn_y) < too_close):
                spawn_x = uniform(SCREEN_WIDTH // 8, (SCREEN_WIDTH * 7) // 8)
                spawn_y = uniform(SCREEN_HEIGHT // 8, (SCREEN_HEIGHT * 7) // 8)
            # get a new angle
            angle = uniform(-180, 180)

            # spawn the new meteor
            self.asteroids.append(BigMeteor(spawn_x, spawn_y, angle))

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        if self.debug:
            # Just hitboxes
            self.ship.draw(True)

            for laser in self.lasers:
                laser.draw(True)

            for rock in self.asteroids:
                rock.draw(True)

            self.draw_score()

            self.draw_debug()
        else:
            self.ship.draw()

            for laser in self.lasers:
                laser.draw()

            for rock in self.asteroids:
                rock.draw()

            self.draw_score()

    def draw_debug(self):
        """ display debug information on the screen """
        debug_text = self.ship.ship_debug()
        start_x = SCREEN_WIDTH - 180
        start_y = SCREEN_HEIGHT - 55
        arcade.draw_text(debug_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.WHITE)

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = f"Score: {self.score}\nHigh score: {self.highscore}"
        start_x = 10
        start_y = SCREEN_HEIGHT - 35
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.WHITE)

    def update_highscore(self):
        """ if the score is bigger, it is the new highscore """
        if self.score > self.highscore:
            self.highscore = self.score

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        for laser in self.lasers:
            laser.advance()

        for asteroid in self.asteroids:
            asteroid.advance()

        self.ship.advance()
        self.check_collisions()
        self.check_off_screen()
        self.update_highscore()

        if len(self.asteroids) < 3:
            # make more
            self.spawn_asteroids(randint(0, 2))

        # once you finish the first batch of asteroids, there is an 8% chance per second (.1% * 80 frames/sec) of spawning more
        if self.score > 160 and not randint(0, 999):
            self.spawn_asteroids()

    def on_update(self, delta_time):
        """ update the music player 
        the arcade documentation says music updates go in on_update() instead of in update() 
        """
        self.music_player.update()

    def machine_gun(self):
        """ rata-tata-tat rata-tata-tat """
        self.firing_delay -= 1
        # every 5 frames, shoot once, cycle counter
        if self.firing_delay == 0:
            self.fire_laser()
            self.firing_delay = 10

    def fire_laser(self):
        """ how to shoot lasers """
        spawn_x, spawn_y = self.ship.get_laser_spawn_x_y()
        laser = Laser(spawn_x, spawn_y)
        laser.fire(self.ship.velocity, self.ship.angle)

        # make laser sound here
        arcade.play_sound(self.laser_sound)

        self.lasers.append(laser)

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
                        asteroid.not_alive()
                        score, new_meteors = asteroid.hit()

                        # make asteroid crunch sound here
                        arcade.play_sound(self.asteroid_sound)

                        # add to the score
                        self.score += score

                        # add to the asteroid list
                        for meteor in new_meteors:
                            self.asteroids.append(meteor)

        # check if ship is touching any asteroid
        for asteroid in self.asteroids:
            if asteroid.alive and self.ship.alive:
                too_close = asteroid.radius + self.ship.radius

                if abs(asteroid.center.x - self.ship.center.x) < too_close and abs(asteroid.center.y - self.ship.center.y) < too_close:
                    # dead ship
                    self.ship.not_alive()

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

        if not self.ship.alive:
            # TODO: Explosion of ship?
            self.setup()

    def check_off_screen(self):
        """
        Checks to see if lasers or asteroids have left the screen
        and if so, moves them to the other side of the screen.
        :return:
        """
        for laser in self.lasers:
            if laser.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                laser.wrap_around(SCREEN_WIDTH, SCREEN_HEIGHT)

        for asteroid in self.asteroids:
            if asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                asteroid.wrap_around(SCREEN_WIDTH, SCREEN_HEIGHT)

        if self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
            self.ship.wrap_around(SCREEN_WIDTH, SCREEN_HEIGHT)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys or arcade.key.A in self.held_keys:
            # rotate ship counterclockwise
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys or arcade.key.D in self.held_keys:
            # rotate ship clockwise
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys or arcade.key.W in self.held_keys:
            # move ship forward
            self.ship.move_forward()

        if arcade.key.DOWN in self.held_keys or arcade.key.S in self.held_keys:
            # slow down ship
            self.ship.slow_down()

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            self.machine_gun()

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the laser.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # Fire the laser here!
                self.fire_laser()

            if key == arcade.key.RCTRL:
                self.debug = not self.debug

            if key == arcade.key.PERIOD:  # . or >
                self.music_player.advance_song()
                self.music_player.play_song()

            if key == arcade.key.COMMA:  # , or <
                self.music_player.go_back()
                self.music_player.play_song()

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
        angle_radians = radians(angle)

        x = length * cos(angle_radians)
        y = length * sin(angle_radians)

        return x, y


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
