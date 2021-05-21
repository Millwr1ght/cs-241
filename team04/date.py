"""
w04 team assignment : Date.py

day : int
month : int
year : int
__init__()
prompt()
display()
"""


class Date:
    """ the date class """

    def __init__(self, date_day=1, date_month=1, date_year=2000):
        # set up the class variables and assign default values
        self.day = date_day
        self.month = date_month
        self.year = date_year

    def prompt(self):
        """ ask for a day, month, and year value """
        self.day = int(input('Day: '))

        # reset month value, if the user doesn't give a vaild month, then ask again
        self.month = 0
        while self.month < 1 or self.month > 12:
            self.month = int(input('Month: '))

        # reset year value, if the user doesn't give a vaild year, assk again
        self.year = 1999
        while year < 2000:
            self.year = int(input('Year: '))

    def display(self):
        """ print out the date in mm/dd/yyyy format """
        # remove the :02d to remove leading zeroes, for example 05/09/2021 --> 5/9/2021
        print(f'{self.month:02d}/{self.day:02d}/{self.year}')
