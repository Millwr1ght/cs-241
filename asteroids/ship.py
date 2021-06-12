import moving_objects


class Ship(MovingObject):
    """ class for the player's ship 

    - rotation_speed = SHIP_TURN_AMOUNT
    - radius = SHIP_RADIUS
    - texture_file = PLAYER
    - thrust = SHIP_THRUST_AMOUNT

    - __init__() : None
    + rotate() : None
    """

    def __init__(self, start_x, start_y, radius: int = SHIP_RADIUS, turn_amount: int = SHIP_TURN_AMOUNT, thrust: int = SHIP_THRUST_AMOUNT, file: str = PLAYER):
        """ class setup"""
        # get the movingObject stuff
        super().__init__(start_x=start_x, start_y=start_y, radius=radius)

        self._texture_file = file
        self.rotation_speed = turn_amount
        self.thrust = thrust

    def increase_velocity(self, dx: float, dy: float):
        """ increment velocity by a given speed """
        self.velocity.increment_dx(dx)
        self.velocity.increment_dy(dy)
