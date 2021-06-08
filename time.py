"""
File: time.py
Author: Team Tuesday Morning (Nate, Tode, etc)

Practice using getters and setters by creating a class to model a time of day.
"""


class Time:
    """ Models the time of day """

    def __init__(self, seconds=0):
        """ 
        seconds : int
        minutes : int
        hours : int
        """
        self.__seconds = seconds
        self.__hours_simple = 0
        self.__period = None

    @property
    def period(self):
        """ if hours < 12, return 'AM'
        else if hours >= 12, return 'PM'
        """
        if self.hours < 12:
            self.__period = 'AM'
        else:
            self.__period = 'PM'
        return self.__period

    @property
    def hours_simple(self):
        """ gets the simple, non military time 
        if hours == 0, then hours = 12
        else if hours >= 13, then hours %= 12
        """
        self.hours_simple = self.hours
        return self.__hours_simple

    @hours_simple.setter
    def hours_simple(self, value):
        """ set simple hours """
        if value == 0:
            self.__hours_simple = 12
        elif value >= 13:
            self.__hours_simple = value - 12
        else:
            self.__hours_simple = value

    @property
    def hours(self):
        """ 
        gets the hours private attribute of Time
        """
        return self.__seconds // 3600

    @hours.setter
    def hours(self, value):
        """ 
        sets the hours attribute to a value between 0 and 23
        """
        if value < 0:
            value = 0
        elif value > 23:
            value = 23

        self.__seconds = self.__seconds + (value * 3600)

    @property
    def minutes(self):
        """ 
        gets the minutes attribute of Time
        """
        return (self.__seconds - ((self.__seconds // 3600) * 3600)) // 60

    @minutes.setter
    def minutes(self, value):
        """
        sets the minutes attribute to a value between 0 and 59
        """
        if value < 0:
            value = 0
        elif value > 59:
            value = 59

        self.__seconds = self.__seconds + (value * 60)

    @property
    def seconds(self):
        """ 
        gets the seconds attribute of Time
        """
        return self.__seconds % 60

    @seconds.setter
    def seconds(self, value):
        """ 
        sets the seconds attribute to a value between 0 and 59
        """
        if value < 0:
            value = 0
        elif value > 59:
            value = 59

        self.__seconds = self.__seconds + value


def main():
    """ the main function """
    # create a new time object
    time = Time()

    # prompt the user for hours, minutes, and seconds
    hours = int(input('Hours: '))
    minutes = int(input('Minutes: '))
    seconds = int(input('Seconds: '))

    # use your setters to set each of these values
    time.hours = hours
    time.minutes = minutes
    time.seconds = seconds

    # then use your getters to display each one.
    print('Time of day:')
    print(f'Hour: {time.hours:02}')
    print(f'Minute: {time.minutes:02}')
    print(f'Second: {time.seconds:02}')

    # clock
    print('\nMilitary time:')
    print(f'({time.hours:02}{time.minutes:02}:{time.seconds:02})')
    print('\nSimple time:')
    print(f'({time.hours_simple:02}:{time.minutes:02}:{time.seconds:02} {time.period})')


if __name__ == '__main__':
    main()
