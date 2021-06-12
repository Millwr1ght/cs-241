from moving_objects import MovingObject


class Ship(MovingObject):
    """ class for the player's ship 

    - rotation_speed = SHIP_TURN_AMOUNT
    - radius = SHIP_RADIUS
    - texture_file = PLAYER
    - thrust = SHIP_THRUST_AMOUNT

    - __init__() : None
    + rotate() : None
    """

    def __init__(self, start_x, start_y, radius: int, turn_amount: int, thrust: int, file: str):
        """ class setup"""
        # get the movingObject stuff
        super().__init__(x=start_x, y=start_y, radius=radius)

        self._texture_file = file
        self.rotation_speed = turn_amount
        self.thrust = thrust

    def increase_velocity(self, dx: float, dy: float):
        """ increment velocity by a given speed """
        self.velocity.increment_dx(dx)
        self.velocity.increment_dy(dy)

    def get_laser_spawn_x_y(self):
        """ get the laser spawn location based on current ship orientation 
        :return: tuple(x:float, y:float)
        """
        return self._get_coords_from_angle(self.angle, self.radius)
