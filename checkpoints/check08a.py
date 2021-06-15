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
        self._gpa = 0.0

    def _get_gpa(self):
        """ get the GPA value """
        return self._gpa

    def _set_gpa(self, value):
        """ set the GPA to a value between 0 and 4 
        If a GPA less that 0 is entered, 
            this should instead set it to 0. 
        if a value greater than 4 is entered, 
            this should instead set the value to 4.0.
        """
        if value < 0:
            self._gpa = 0
        elif value > 4.0:
            self._gpa = 4.0
        else:
            self._gpa = value

    @property
    def letter(self):
        """ get the associated letter value 
        'determine the correct letter for the stored gpa, and return it'
        """
        if self._gpa < 1.0:
            return 'F'
        elif self._gpa >= 1.0 and self._gpa < 2.0:
            return 'D'
        elif self._gpa >= 2.0 and self._gpa < 3.0:
            return 'C'
        elif self._gpa >= 3.0 and self._gpa < 4.0:
            return 'B'
        else:
            return 'A'

    @letter.setter
    def letter(self, letter):
        """ set the associated letter value for the GPA 
        'determine the appropriate gpa value and store that.'
        { F: 0.0; D: 1.0; C: 2.0; B: 3.0; A: 4.0 }
        """
        if letter.upper() == 'F':
            self._gpa = 0.0
        elif letter.upper() == 'D':
            self._gpa = 1.0
        elif letter.upper() == 'C':
            self._gpa = 2.0
        elif letter.upper() == 'B':
            self._gpa = 3.0
        elif letter.upper() == 'A':
            self._gpa = 4.0

    gpa = property(_get_gpa, _set_gpa)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))


if __name__ == "__main__":
    main()
