""" 
File: check08a.py
Author: Nathan Johnston
"""


class GPA:
    """ 
    the Class for GPA   

    ____GPA____
    gpa : float
    __init__()
    get_gpa() : float
    set_gpa(value) : None
    get_letter() : str
    set_letter(letter) : None
    """

    def __init__(self):
        """"""
        self.gpa = 0.0

    def get_gpa(self):
        """ get the GPA value """
        return self.gpa

    def set_gpa(self, value):
        """ set the GPA to a value between 0 and 4 
        If a GPA less that 0 is entered, 
            this should instead set it to 0. 
        if a value greater than 4 is entered, 
            this should instead set the value to 4.0.
        """
        if value < 0:
            self.gpa = 0
        elif value > 4.0:
            self.gpa = 4.0
        else:
            self.gpa = value

    def get_letter(self):
        """ get the associated letter value 
        'determine the correct letter for the stored gpa, and return it'
        """
        if self.gpa < 1.0:
            return 'F'
        elif self.gpa >= 1.0 and self.gpa < 2.0:
            return 'D'
        elif self.gpa >= 2.0 and self.gpa < 3.0:
            return 'C'
        elif self.gpa >= 3.0 and self.gpa < 4.0:
            return 'B'
        else:
            return 'A'

    def set_letter(self, letter):
        """ set the associated letter value for the GPA 
        'determine the appropriate gpa value and store that.'
        { F: 0.0; D: 1.0; C: 2.0; B: 3.0; A: 4.0 }
        """
        if letter.upper() == 'F':
            self.gpa = 0.0
        elif letter.upper() == 'D':
            self.gpa = 1.0
        elif letter.upper() == 'C':
            self.gpa = 2.0
        elif letter.upper() == 'B':
            self.gpa = 3.0
        elif letter.upper() == 'A':
            self.gpa = 4.0


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))


if __name__ == "__main__":
    main()
