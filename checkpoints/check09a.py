"""
File: check09a.py : exceptions
Author: Nathan Johnston

intended to help you practice the syntax of exceptions
"""


def int_input(prompt):
    """ asks for a integer value, returns that value """
    replied = False
    while not replied:
        try:
            number = int(input(prompt))
            replied = True
        except:
            print("The value entered is not valid")
    return number


def main():
    """ """

    user_answer = int_input('Enter a number: ')
    print(f'The result is: {2*user_answer}')


if __name__ == '__main__':
    main()
