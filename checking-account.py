"""
File : checking-account.py
Authors: Team Tuesday Lunch

Practice raising and catching errors.
"""


class BalanceError(Exception):
    """ the balance error exception """

    def __init__(self, message, overage):
        """ pass on the error message """
        super().__init__(message)
        # the amount over the balance
        self.overage = overage


class OutOfChecksError(Exception):
    """ the out of checks exception """

    def __init__(self, message):
        """ pass on the error message """
        super().__init__(message)


class CheckingAccount:
    """ the checking account class
    balance : float
    check_count : int
    __init__(starting_balance, num_checks) : None
    deposit(amount) : None
    write_check(amount) : None
    display() : None
    apply_for_credit(amount) : None
    """

    def __init__(self, starting_balance, num_checks):
        """ setup """
        self.check_count = num_checks

        if starting_balance < 0:
            raise BalanceError(
                "You have negative money! You can't open an account", abs(starting_balance))
        else:
            self._balance = starting_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if self._balance + value > 0:
            self._balance += value
        else:
            raise BalanceError(
                'You cannot bring your balance below zero.', abs(self._balance + value))

    def deposit(self, amount):
        """ increase the balance by the amount passed in. """
        if amount < 0:
            raise ValueError('You cannot deposit a negative amount of money.')
        else:
            self.balance += amount

    def write_check(self, amount):
        """ decrease the balance by the amount given and decrease the number of checks by 1. """
        if amount < 0:
            raise ValueError('You cannot withdraw a negative amount of money.')
        if amount > self.balance:
            raise BalanceError(
                "You cannot use more money than you have.", abs(amount - self._balance))
        elif self.check_count <= 0:
            raise OutOfChecksError('You do not have any more checks!')
        else:
            self.check_count -= 1
            self.balance -= amount

    def display(self):
        """ display the current balance and the number of checks. """
        print(
            f'Balance: {self.balance}\nChecks remaining: {self.check_count}')

    def apply_for_credit(self, amount):
        """ leave blank for now """
        raise NotImplementedError(
            'This feature is not implemented in this edition of The Game. Try again later.')


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ''

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))
            try:
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as error:
                print(error)
            except ValueError as error:
                print(error)

        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            try:
                acc.deposit(amount)
            except ValueError as error:
                print(error)

        elif command == "check":
            amount = float(input("Amount: "))
            try:
                acc.write_check(amount)
            except ValueError as error:
                print(error)
            except BalanceError as error:
                print(error)
            except OutOfChecksError:
                # if out of checks ask if they want 25 more for 5$
                more_checks = input(
                    '\nYou are out of checks! Would you like to but more for $5? (y/n) ')
                if more_checks.lower() == 'y':
                    acc.balance -= 5
                    acc.check_count += 25

        elif command == "credit":
            amount = float(input("Amount: "))
            try:
                acc.apply_for_credit(amount)
            except NotImplementedError as error:
                print(error)


if __name__ == "__main__":
    main()
