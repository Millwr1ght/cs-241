"""
File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
from random import randint, uniform, seed

# These are Global constants to use throughout the game
SCREEN_TITLE = 'Pong | Nathan Johnston'
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

# Classes


class Point:
    """ The Point Class, defines a co-ordinate pair on the SCREEN """

    def __init__(self, start_x=0, start_y=0):
        """ initiate values """
        self.x = start_x
        self.y = start_y


class Velocity:
    """ The Velocity Class, defines the speed and direction of an object's motion """

    def __init__(self, start_dx=uniform(-4, 4), start_dy=uniform(-4, 4)):
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


class Ball:
    """ The Pong Ball class """

    def __init__(self):
        """ initate values, start in the middle """
        seed()
        self.center = Point(start_x=SCREEN_WIDTH // 2,
                            start_y=SCREEN_HEIGHT // 2)
        self.velocity = Velocity()

    def draw(self):
        """ drawing The Ball in the window """

        # draw The Ball
        arcade.draw_circle_filled(
            self.center.x, self.center.y, BALL_RADIUS, arcade.color.BLACK)

    def advance(self):
        """ advancing The Ball in the window """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        """ invert the x velocity """
        self.velocity.dx *= -1

    def bounce_vertical(self):
        """ invert the y velocity """
        self.velocity.dy *= -1

    def faster(self, increment):
        """ increase the velocity by increment """
        self.velocity.increment(increment)

    def restart(self):
        """ reset ball values, re-__init__() """

        # Re-seed!
        seed()

        # Reroll!
        self.center = Point(start_x=(SCREEN_WIDTH // 2) + randint(-30, 30),
                            start_y=(SCREEN_HEIGHT // 2) + randint(-30, 30))

        # Reset!
        self.velocity = Velocity()

        # RESTART!!!


class Paddle:
    """ The Pong Paddle class """

    def __init__(self):
        """ variable setup """
        self.center = Point(start_x=SCREEN_WIDTH -
                            PADDLE_WIDTH, start_y=SCREEN_HEIGHT // 2)

    def draw(self):
        """ drawing The Paddle on the window """

        # draw the Paddle
        arcade.draw_rectangle_filled(self.center.x, self.center.y,
                                     PADDLE_WIDTH, PADDLE_HEIGHT,
                                     arcade.color.BLACK)

    def move_up(self):
        """ move The Paddle up """
        self.center.y += MOVE_AMOUNT

        # If Out of Bounds, Don't
        if self.center.y > SCREEN_HEIGHT - (PADDLE_HEIGHT // 2 + 1):
            self.center.y = SCREEN_HEIGHT - (PADDLE_HEIGHT // 2 + 1)

    def move_down(self):
        """ move The Paddle down """
        self.center.y += -MOVE_AMOUNT

        # If Down Below, Stop that
        if self.center.y < PADDLE_HEIGHT // 2:
            self.center.y = PADDLE_HEIGHT // 2


class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height, title):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height, title)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # at multiples of this number, difficulty increases
        self.difficulty_threshold = 7

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Restarts the game """

        # Reset Ball, Paddle, Score
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0

        # Reset key Booleans
        self.holding_left = False
        self.holding_right = False

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = f'Score: {self.score}\nRestart: [R]'
        start_x = 10
        start_y = SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move The Ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_score(self):
        """ Every ten or so points, make the ball faster """
        if self.score > 0 and self.score % self.difficulty_threshold == 0:
            self.ball.faster(randint(1, 3))

    def check_hit(self):
        """
        Checks to see if The Ball has hit The Paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH // 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT // 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
            abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.score += SCORE_HIT

            # make difficulty incremental
            self.check_score()

    def check_miss(self):
        """
        Checks to see if The Ball went past The Paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if The Ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        # Hit the left side of the Screen
        if self.ball.center.x < BALL_RADIUS and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        # Hit the Bottom of the screen
        if self.ball.center.y > (SCREEN_HEIGHT - BALL_RADIUS) and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

        # Hit the Top of the Screen
        if self.ball.center.y < BALL_RADIUS and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """

        # LEFT, DOWN, A, S
        if key == arcade.key.LEFT or key == arcade.key.DOWN or key == arcade.key.S or key == arcade.key.A:
            self.holding_left = True

        # RIGHT, UP, W, D
        if key == arcade.key.RIGHT or key == arcade.key.UP or key == arcade.key.W or key == arcade.key.D:
            self.holding_right = True

        # R to Restart and Reset
        if key == arcade.key.R:
            # restart Game
            self.setup()

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        # LEFT, DOWN, A, S
        if key == arcade.key.LEFT or key == arcade.key.DOWN or key == arcade.key.S or key == arcade.key.A:
            self.holding_left = False

        # RIGHT, UP, W, D
        if key == arcade.key.RIGHT or key == arcade.key.UP or key == arcade.key.W or key == arcade.key.D:
            self.holding_right = False


def main():
    """ the main function """

    # Creates the game and starts it going
    window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == '__main__':
    main()
