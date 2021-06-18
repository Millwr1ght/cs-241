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
from abc import ABC, abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
SCREEN_TITLE = 'Awesome-er Version of Skeet | N. Johnston'

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_STRONG_COLOR = arcade.color.CINNABAR
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

    def __init__(self, start_dx: float = random.uniform(-1, 4), start_dy: float = random.uniform(-2, 2)):
        """ initiate values """
        self.dx = start_dx
        self.dy = start_dy


class FlyingObject:
    """ These 'fly' across the playing field, and die when they reach The Other Side 

    center : Point --> all start at (0,0) unless otherwise specified
    velocity : Velocity --> all have no speed, ---^
    radius : float --> all 10 unless ---------^
    __init__()
    advance() : None
    draw() : None
    is_off_screen(screen_width, screen_height) : Boolean
    """

    def __init__(self, x: int = 0, y: int = 0, dx: float = 0, dy: float = 0, radius: int = TARGET_RADIUS, color=TARGET_COLOR):
        """ initialize object values """
        self.center = Point(start_x=x, start_y=y)
        self.velocity = Velocity(dx, dy)
        self.radius = radius
        self.color = color
        self.alive = True

    def advance(self):
        """ Move the object across the field """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self):
        """ Draw self on field """
        arcade.draw_circle_filled(
            self.center.x, self.center.y,
            self.radius, self.color)

    def is_off_screen(self, width, height):
        """ checks if the object has left the premises 
        returns : Boolean
        """
        return self.center.x > width or self.center.y > height or height > 0


class Bullet(FlyingObject):
    """ the shoot shoot missile class 
    fire(angle:float) : None
    """

    def __init__(self, spawn_x, spawn_y):
        """ setup variables """
        # initialize center, velocity, radius, color
        super().__init__(x=spawn_x, y=spawn_y)

        self.color = BULLET_COLOR
        self.radius = BULLET_RADIUS

    def not_alive(self):
        """ commit alt+F4 """
        self.alive = False

    def fire(self, angle: float):
        """ shoot the bullet based on the given angle, in degrees 
        if necessary, increase radius and decrease speed by relevant multipliers
        """
        self.velocity.dx = math.cos(math.radians(
            angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(
            angle)) * BULLET_SPEED


class ChargedBullet(Bullet):
    """ the Charged shot bullet class
    delay from left mouse hold to release is proportionate to bullet size and speed
    """

    def __init__(self, x, y, multiplier):
        """ setup variables """
        # initialize center, velocity, radius, color
        super().__init__(spawn_x=x, spawn_y=y)

        self.multiplier = 1 + multiplier
        self.hit_points = 0.5 * multiplier

    def not_alive(self):
        """ commit scooter ankle """
        self.hit_points -= 1
        if self.hit_points <= 0:
            self.alive = False

    def fire(self, angle: float):
        """ shoot the bullet based on the given angle, in degrees 
        increases radius and decreases speed by multiplier
        """
        self.radius *= self.multiplier

        self.velocity.dx = math.cos(math.radians(
            angle)) * BULLET_SPEED / self.multiplier
        self.velocity.dy = math.sin(math.radians(
            angle)) * BULLET_SPEED / self.multiplier


class Target(FlyingObject, ABC):
    """ the get shot missile-ish class
    there are three types/subclasses: strong, safe, standard

    alive : Boolean
    hit() : int
    launch() : None
    """

    def __init__(self, t_color=TARGET_COLOR, t_radius=TARGET_RADIUS, t_spawn=SCREEN_HEIGHT//2):
        """ setup variables """
        # initialize center, velocity, radius, color
        super().__init__(color=t_color, radius=t_radius, y=t_spawn)

    def launch(self):
        """ Target's version of Bullet's fire()
        sets the projectile's velocity
        safe and standard go fast, strong ones go slow
        """
        # standard speed
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 5)

    @abstractmethod  # Decorator to define an abstract method
    def hit(self):
        """ represents the target being hit
        should either kill the target 
        (or decrement the number of hits remaining for the strong target) 
        and return an integer representing the points scored for that hit.
        """
        pass


class StandardTarget(Target):
    """ Standard Target Class
    Rendered as a circle with a 20px diameter.
    Destroyed with one hit.
    1 point is awarded for hitting it.
    """

    def __init__(self, height):
        """ setup variables """
        super().__init__(t_spawn=height)

    def hit(self):
        """ target got shot
        Target dies. 
        Returns 1 point
        """
        self.alive = False
        return 1


class StrongTarget(Target):
    """ the STRONG target
    has 3 hp
    hp is drawn on self
    """

    def __init__(self, height):
        """ setup variables """
        super().__init__(t_color=TARGET_STRONG_COLOR,
                         t_spawn=height)

        self.hit_points = 2

    def draw(self):
        """ a Target, but with a number """
        super().draw()  # base target image
        text_x = self.center.x
        text_y = self.center.y
        arcade.draw_text(repr(self.hit_points+1), text_x, text_y,
                         arcade.color.CLARET, font_size=20,
                         align="center", anchor_x="center", anchor_y="center")

    def launch(self):
        """ the STRONG launcher 
        sets velocity to a slower speed
        """
        # slow down speed
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 3)

    def hit(self):
        """ Strong target was hit! Not very effective...
        decrements the number of hits remaining
        Returns the points scored for that hit: 1 if not dead, 5 if so
        """
        if self.hit_points < 1:
            self.alive = False
            return 5
        else:
            self.hit_points -= 1
            return 1


class SafeTarget(Target):
    """ the 'safe' target class
    is not remotely safe to hit
    do not touch with bullet
    1 hit kill, -5 points awarded
    """

    def __init__(self, height):
        """ setup variables """
        super().__init__(t_color=TARGET_SAFE_COLOR,
                         t_radius=TARGET_SAFE_RADIUS,
                         t_spawn=height)

    def draw(self):
        """ draw the safe blue square """
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, self.radius, self.radius, self.color)

    def hit(self):
        """ represents the target being hit
        kills the target and returns an integer representing the points scored for that hit
        that integer is -10
        """
        self.alive = False
        return -10


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
        arcade.draw_rectangle_filled(self.center.x, self.center.y,
                                     RIFLE_WIDTH, RIFLE_HEIGHT,
                                     RIFLE_COLOR, 360-self.angle)


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

    def __init__(self, width, height, title):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height, title)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        self.targets = []

        self.weapon_list = ['Single Fire', 'Rapid Fire', 'Charge Fire']
        self.weapon = 0

        self.rapid_fire = False
        self.rapid_delay = 0

        self.charging = False
        self.charge_delay = 0  # charge bullet size and speed are proportional to delay length

        self.debug = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object

        for bullet in self.bullets:
            bullet.draw()

        for target in self.targets:
            target.draw()

        self.rifle.draw()

        self.draw_score()

        self.draw_weapon_name()

        if self.debug:
            self.draw_debug()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def draw_weapon_name(self):
        """
        Puts the current weapon type on the screen
        """
        weapon_text = f'Weapon type: {self.weapon_list[self.weapon]}\nRight click to cycle weapon'
        start_x = SCREEN_WIDTH - 170
        start_y = SCREEN_HEIGHT - 35
        arcade.draw_text(weapon_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def draw_debug(self):
        """
        draw debug information on screen
        """
        debug_text = f'debug: Charging: {self.charging}, {self.charge_delay}'
        start_x = SCREEN_WIDTH - 170
        start_y = SCREEN_HEIGHT - 55
        arcade.draw_text(debug_text, start_x=start_x, start_y=start_y,
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

        # non-standard firing logic
        if self.rapid_fire:
            self.rapid_delay += 1
            # every 4 frames, shoot once, cycle counter
            if self.rapid_delay % 5 == 0:
                self.make_bullet(self.rifle.angle)
                self.rapid_delay = 0

        elif self.charging and self.charge_delay < 12:
            # increase delay counter for every frame of charging
            self.charge_delay += 0.1

        for bullet in self.bullets:
            bullet.advance()

        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # Decide what type of target to create and append it to the list
        spawn_type = random.uniform(-2, 7)
        spawn_height = random.uniform(SCREEN_HEIGHT//2, SCREEN_HEIGHT)

        # low type == high points, slower
        if spawn_type < 0:
            target = StrongTarget(spawn_height)

        # high grade == lower points, faster
        elif spawn_type > 5:
            target = SafeTarget(spawn_height)
        # else: meh == 1 point
        else:
            target = StandardTarget(spawn_height)

        # PULL!
        target.launch()

        # target is in the air
        self.targets.append(target)

    def make_bullet(self, angle):
        """ 
        make a bullet! make many bullet!
        :return:
        """
        # find the spawn point
        x, y = self._get_coords_from_angle(angle, RIFLE_WIDTH//2)

        bullet = Bullet(x, y)
        bullet.fire(angle)

        self.bullets.append(bullet)

    def make_charged_bullet(self, angle):
        """ 
        make a big bullet
        :return:
        """
        # find the spawn point
        x, y = self._get_coords_from_angle(angle, RIFLE_WIDTH//2)

        bullet = ChargedBullet(x, y, self.charge_delay)
        bullet.fire(angle)

        self.bullets.append(bullet)

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

                        bullet.not_alive()
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

        # right click switches weapon between single fire, rapid fire and charge fire
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.weapon = (self.weapon + 1) % 3

        # Left click fire!
        elif button == arcade.MOUSE_BUTTON_LEFT:

            # get the mouse angle
            angle = self._get_angle_degrees(x, y)

            # Rapid fire mechanics
            if self.weapon == 1:
                # while mouse down, bullet hell spam and/or auto-fire?
                self.rapid_fire = True

            # charge fire mechanics
            elif self.weapon == 2:
                # while mouse down, charge the bullet
                self.charging = True

            # standard rate of fire
            elif self.weapon == 0:
                # Fire!
                self.make_bullet(angle)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ release the clickety """

        if self.weapon == 1:
            # end rapid fire
            self.rapid_fire = False

        elif self.weapon == 2:
            # get the mouse angle
            angle = self._get_angle_degrees(x, y)

            # Fire!
            self.make_charged_bullet(angle)

            # and release
            self.charging = False
            self.charge_delay = 0

    def on_key_press(self, symbol: int, modifiers: int):
        """
        keyboard operations
        """
        # press D to for Charged Bullet debugging information
        if not self.debug and symbol == arcade.key.D:
            self.debug = True
        elif symbol == arcade.key.D:
            self.debug = False

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

    @staticmethod
    def _get_coords_from_angle(angle, length):
        """ 
        get the x and y co-ordinates from a length and an angle
        particularly from the angle and length of the rifle 
        so we can spawn bullets at the end of the barrel
        """
        angle_radians = math.radians(angle)

        x = length * math.cos(angle_radians)
        y = length * math.sin(angle_radians)

        return x, y


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
