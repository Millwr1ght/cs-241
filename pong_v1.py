"""
w05 Prove : Pong
Author: Nathan Johnston

One player Pong, using the Python Arcade
"""
import arcade
from random import seed, randint

# Global Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
SCREEN_TITLE = 'Pong'

BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
PADDLE_SPEED = 5


# Classes
class Ball:
    """ The Pong ball class """

    def __init__(self, start_x=SCREEN_WIDTH // 4, start_y=SCREEN_HEIGHT // 2):
        """ set up variables """
        seed()
        self.x = start_x
        self.y = start_y
        self.dx = randint(-4, 4)
        self.dy = randint(-4, 4)

    def draw(self):
        """ drawing the ball in the window """

        # draw the Ball
        arcade.draw_circle_filled(self.x, self.y,
                                  BALL_RADIUS, arcade.color.BLACK)

    def move(self):
        """ advancing the ball in the window """

        # Move the Ball
        self.x += self.dx
        self.y += self.dy

        # Did the ball hit:
        # the right side of the screen while moving right?
        if self.x > SCREEN_WIDTH - BALL_RADIUS and self.dx > 0:
            # Stop the ball, you lose
            self.dx *= 0
            self.dy *= 0

        # the left side of the screen while moving left?
        if self.x < BALL_RADIUS and self.dx < 0:
            self.dx *= -1

        # the bottom side of the screen while moving down?
        if self.y > SCREEN_HEIGHT - BALL_RADIUS and self.dy > 0:
            self.dy *= -1

        # the top side of the screen while moving up?
        if self.y < BALL_RADIUS and self.dy < 0:
            self.dy *= -1


class Paddle:
    """ the Pong paddle class """

    def __init__(self):
        """ variable setup """
        self.x = SCREEN_WIDTH - (PADDLE_WIDTH * 1.5)
        self.y = SCREEN_HEIGHT // 2
        self.dy = 0

    def draw(self):
        """ drawing the paddle on the window """

        # draw the Paddle
        arcade.draw_rectangle_filled(self.x, self.y,
                                     PADDLE_WIDTH, PADDLE_HEIGHT,
                                     arcade.color.BLACK)

    def move(self, up, down):
        """ advancing the paddle on the window """

        # Reset speed
        self.dy = 0

        # Is the move key pressed?
        if up and not down:
            self.dy = PADDLE_SPEED
        elif down and not up:
            self.dy = -PADDLE_SPEED

        # Move the Paddle
        self.y += self.dy

        # Check if out of bounds
        if self.y < PADDLE_HEIGHT // 2:
            self.y = PADDLE_HEIGHT // 2
        elif self.y > SCREEN_HEIGHT - (PADDLE_HEIGHT // 2 + 1):
            self.y = SCREEN_HEIGHT - (PADDLE_HEIGHT // 2 + 1)


class Game(arcade.Window):
    """ The Pong Game Class """

    def __init__(self, width, height, title):
        """ Game initial setup """
        super().__init__(width, height, title)

        # Track keypresses
        self.up_pressed = False
        self.down_pressed = False

        # Create the idea of Game Objects
        self.ball = Ball()
        self.paddle = Paddle()

        # Track if Game Over
        self.game_over = False

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ call to restart game """

        # New Game Objects
        self.ball = Ball()
        self.paddle = Paddle()

        # Reset Game Over
        self.game_over = False

    def on_draw(self):
        """ Render the window """

        # clear the screen to the background color
        arcade.start_render()

        # Draw the Paddle
        self.paddle.draw()

        # Draw the Ball
        self.ball.draw()

        # Game Over Text
        if self.game_over:
            arcade.draw_text("GAME OVER\nPress [r]",
                             SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.BLACK, 14, width=200,
                             align="center", anchor_x="center", anchor_y="center")

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here """

        # Move the Paddle
        self.paddle.move(self.up_pressed, self.down_pressed)

        # Move the ball
        self.ball.move()

        # Did the ball start with 0 velocity?
        if self.ball.dy == 0 and self.ball.x < SCREEN_WIDTH - BALL_RADIUS:
            self.ball.dy += 1
        if self.ball.dx == 0 and self.ball.x < SCREEN_WIDTH - BALL_RADIUS:
            self.ball.dx += 1

        # Check for Object Collision
        if self.ball.x + BALL_RADIUS >= self.paddle.x \
           and self.ball.x + BALL_RADIUS <= self.paddle.x + 5 \
           and self.ball.y >= (self.paddle.y - PADDLE_HEIGHT // 2) \
           and self.ball.y <= (self.paddle.y + PADDLE_HEIGHT // 2) \
           and self.ball.dx > 0:
            self.ball.dx *= -1

        # If Ball out of bounds?
        if self.ball.x > SCREEN_WIDTH - BALL_RADIUS:
            self.game_over = True

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.R:
            # restart Game
            self.setup()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False


def main():
    """ running The Game """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == '__main__':
    main()
