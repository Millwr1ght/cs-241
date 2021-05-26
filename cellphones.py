"""
CS241 : Check06b
Cellphone tracking .py
Author : Nathan Johnston
"""


class Phone:
    """ 
    area_code : int
    prefix : int
    suffix : int
    prompt_number() : void
    display() : void
    """

    def __init__(self, area_code: int = 123, prefix: int = 456, suffix: int = 7890):
        """ initialize """
        self.area_code = area_code
        self.prefix = prefix
        self.suffix = suffix

    def prompt_number(self):
        """ get a phone number from the user
        :return:
        """
        self.area_code = int(input('Area Code: '))
        self.prefix = int(input('Prefix: '))
        self.suffix = int(input('Suffix: '))

    def display(self):
        """ output the phone's info
        :return:
        """
        print(f'\nPhone info:\n({self.area_code}){self.prefix}-{self.suffix}')


class SmartPhone(Phone):
    """ 
    email : string
    prompt() : void
    display() : void
    """

    def __init__(self, email: str = '', area_code: int = 123, prefix: int = 456, suffix: int = 7890):
        """ setup """

        # setup Phone part first
        super().__init__()

        # setup Smart part
        self.email = email

    def prompt(self):
        """ get a smartphone info block from the user
        :return:
        """
        self.prompt_number()
        self.email = input('Email: ')

    def display(self):
        """ output the cell's info
        :return:
        """
        super().display()

        print(self.email)


def main():
    """ main """

    p = Phone()
    print('Phone:')
    p.prompt_number()
    p.display()

    print('\nSmart phone:')
    c = SmartPhone()
    c.prompt()
    c.display()


if __name__ == '__main__':
    main()
