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

    def __init__(self, radius, turn_amount, thrust, file: str = PLAYER):
        """ class setup"""
        # get the movingObject stuff
        super().__init__(radius=radius)

        self.texture_file = file
        self.rotation_speed = turn_amount
        self.thrust = thrust
