class Student:
    """ Student class, used to store and handle student information """

    def __init__(self):
        """ Initialize a Student with the given user data """
        self.first_name = ''
        self.last_name = ''
        self.id = 0


def prompt_student():
    """ Creates a new Student, Asks user for student information, applies info to new Student"""
    s = Student()
    
    s.first_name = input('Please enter your first name: ')
    s.last_name = input('Please enter your last name: ')
    s.id = input('Please enter your id number: ')

    return s


def display_student(student):
    """ Take Student information and display it """
    print('\nYour information:')
    print(f'{student.id} - {student.first_name} {student.last_name}')


def main():
    """
    Checkpoint 3a: Student info 
    prompt the user for their personal information, store it, and display it
    """
    user = prompt_student()
    display_student(user)

if __name__ == '__main__':
    main()