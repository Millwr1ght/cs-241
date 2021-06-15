"""
File: check09b.py : exceptions
Author: Nathan Johnston

intended to help you practice the syntax of exceptions
"""


class NegativeNumberError(Exception):
    """ new exception type """
    pass


def get_inverse(n):
    """ """
    # if n is not a number, exception
    if type(float(n)) != float or type(int(n)) != int:
        raise ValueError
    # if n is 0, exception
    else:
        f = float(n)
        if f == 0:
            raise ZeroDivisionError
        # in n < 0, exception
        elif f < 0:
            raise NegativeNumberError
        else:
            return 1/f


def main():
    """ """
    number = input('Enter a number: ')

    try:
        result = get_inverse(number)
    except ValueError:
        print('Error: The value must be a number')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    except NegativeNumberError:
        print('Error: The value cannot be negative')
    else:
        print(f'The result is: {result}')


if __name__ == '__main__':
    main()
