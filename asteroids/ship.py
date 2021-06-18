from moving_objects import MovingObject


class Ship(MovingObject):
    """ class for the player's ship 

    - radius = SHIP_RADIUS
    - texture_file = PLAYER
    - thrust = SHIP_THRUST_AMOUNT

    - __init__() : None
    + rotate() : None
    + move_forward() : None
    """

    def __init__(self, start_x, start_y, radius: int, thrust: int, file: str):
        """ class setup"""
        # get the movingObject stuff
        super().__init__(x=start_x, y=start_y, radius=radius)

        self._texture_file = file
        self.thrust = thrust

    def rotate(self, turn_amount):
        """ rotate the ship a given amount """
        self.angle += turn_amount

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
        x, y = self._get_x_y_from_angle(self.angle, self.radius)
        return self.center.x + x, self.center.y + y
