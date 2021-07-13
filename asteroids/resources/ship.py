from resources.moving_objects import MovingObject


class Ship(MovingObject):
    """ class for the player's ship 

    - radius = SHIP_RADIUS
    - texture_file = PLAYER
    - thrust = SHIP_THRUST_AMOUNT

    - __init__() : None
    + turn_left(turn_amount) : None
    + turn_right(turn_amount) : None
    + move_forward() : None
    + slow_down(): None
    + ship_debug(): str
    + get_laser_spawn_x_y(): None
    """

    def __init__(self, start_x, start_y, radius: int, turn_amount: int, thrust: int, file: str):
        """ class setup"""
        # get the movingObject stuff
        super().__init__(x=start_x, y=start_y, radius=radius)

        self._texture_file = file
        self.thrust = thrust
        self.turn = turn_amount

    def ship_debug(self):
        """
        outputs debug information
        :return: string
        """
        x, y = self.get_laser_spawn_x_y()
        return f'\nShip center: {self.center.x:.2f}, {self.center.y:.2f}\nShip angle: {self.angle:.2f}\nLasers spawn at: {x:.2f}, {y:.2f}'

    def turn_left(self):
        """ rotate the ship counter-clockwise a given amount """
        self.angle += self.turn

    def turn_right(self):
        """ rotate the ship clockwise a given amount """
        self.angle -= self.turn

    def move_forward(self):
        """ increment velocity by a given speed """
        dx, dy = self._get_x_y_from_angle(self.angle + 90, self.thrust)
        self.velocity.dx += dx
        self.velocity.dy += dy

    def slow_down(self):
        """ decrease velocity """
        self.velocity.dx *= 0.95
        self.velocity.dy *= 0.95

    def get_laser_spawn_x_y(self):
        """ get the laser spawn location based on current ship orientation 
        :return: tuple(x:float, y:float)
        """
        x, y = self._get_x_y_from_angle(self.angle + 90, self.radius)
        return self.center.x + x, self.center.y + y
