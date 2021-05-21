"""
Robot Simulator

Author: Nathan Johnston
Purpose: Drive the robot, fire the laser, conserve fuel
"""

class Robot:
    """ the robot class, moves up/right/down/left, fires a laser, and outputs status"""

    def __init__(self, x_coord, y_coord, fuel_tank):
        self.x = x_coord
        self.y = y_coord
        self.fuel_level = fuel_tank

    def check_fuel(self, amount):
        if self.fuel_level >= amount:
            self.fuel_level -= amount
            return True
        else:
            print("Insufficient fuel to perform action")
            return False

    def move_up(self):
        """ Moves up 1 unit, but subtracts one? hey teach, this doesn't make sense but if you say so """
        if self.check_fuel(5):
            self.y -= 1

    def move_left(self):
        """ Moves left 1 unit """
        if self.check_fuel(5):
            self.x -= 1

    def move_down(self):
        """ Moves down 1 unit """
        if self.check_fuel(5):
            self.y += 1

    def move_right(self):
        """ Moves right 1 unit """
        if self.check_fuel(5):
            self.x += 1

    def status(self):
        """ displays current status """
        print(f'({self.x}, {self.y}) - Fuel: {self.fuel_level}')

    def fire(self):
        """ fires the robot laser """
        if self.check_fuel(15):
            print('Pew! Pew!')


def user_prompt():
    """ user interface, choices are up, down, left, right, fire, status, and quit """
    user_choice = False
    while user_choice != 'up' and user_choice != 'left' and user_choice != 'right' and user_choice != 'down' and user_choice != 'fire' and user_choice != 'status' and user_choice != 'quit':
        user_choice = input('Enter command: ').lower()
    return user_choice


def main():
    """ gameplay """
    game_on = True
    Player = Robot(10, 10, 100)
    while game_on:
        command = user_prompt()
        if command == 'up':
            Player.move_up()
        elif command == 'left':
            Player.move_left()
        elif command == 'right':
            Player.move_right()
        elif command == 'down':
            Player.move_down()
        elif command == 'fire':
            Player.fire()
        elif command == 'status':
            Player.status()
        elif command == 'quit':
            print('Goodbye.')
            game_on = False


if __name__ == "__main__":
    main()
