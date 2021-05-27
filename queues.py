"""
CS241 : Data structures - Queue
Author: Nathan Johnston

"""
from collections import deque


class Student:
    """ the Student class
    name : string
    course : string
    __init__()
    prompt()
    display()
    """

    def __init__(self):
        """ """
        self.name = ''
        self.course = ''

    def prompt(self):
        """ """
        self.name = input('\nName: ')
        self.course = input('Course: ')

    def display(self):
        """ """
        print(f'{self.name}{self.course}')


class HelpSystem:
    """ the Help System class
    waiting_list : deque
    __init__()
    is_student_waiting() : boolean
    add_to_waiting_list(Student)
    help_next_student()
    """

    def __init__(self):
        """ """
        self. waiting_list = deque()

    def is_student_waiting(self):
        """ if sutudent at end of list, then no """
        return len(self.waiting_list) > 0

    def add_to_waiting_list(self, student):
        """ add a Student to the wait deque """
        self.waiting_list.append(student)

    def help_next_student(self):
        """ 
        if there is not a student waiting, display "No one to help". 
        If there is a student waiting then remove them from the 
        waiting_list and display, "Now helping John with CS 241" 
        assuming that John is the name of the student, and CS 241 is the course.

        """

        if self.is_student_waiting():
            helped_student = self.waiting_list.popleft()
            print(
                f'Now helping {helped_student.name} with {helped_student.course}')

        else:
            print('No one to help')


def main():
    """ """
    h = HelpSystem()

    choice = ''
    while choice != '3':
        print('\nOptions:\n1. Add a new student\n2. Help next student\n3. Quit')
        choice = input('Enter: ')

        if choice == '1':
            s = Student()
            s.prompt()
            h.add_to_waiting_list(s)
        elif choice == '2':
            h.help_next_student()
        elif choice != '3':
            print('Invalid selection')

    print('\nThank you!')


if __name__ == '__main__':
    main()
