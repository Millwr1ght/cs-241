"""
w04 team assignment : Assignment.py

name : string
start_date : Date
due_date : Date
end_date : Date
__init__()
prompt()
display()
"""
#get the Date class from date.py
from date import Date


class Assignment:
    """ the assignment class """

    def __init__(self, name = 'Untitled', start = Date(), due = Date(), end = Date()):
        # set up the class variables and assign default values
        self.name = name
        self.start_date = start
        self.due_date = due
        self.end_date = end
    
    def prompt(self):
        """ ask for a name, then each of the three dates in turn """
        self.name = input('Name: ')
        
        print('\nStart Date:')
        self.start_date.prompt()
        
        print('\nDue Date:')
        self.due_date.prompt()

        print('\nEnd Date:')
        self.end_date.prompt()
        print()

    def display(self):
        """ display the name and each of the dates """
        print(f'Assignment: {self.name}')
        print('Start Date:')
        self.start_date.display()
        print('Due Date:')
        self.due_date.display()
        print('End Date:')
        self.end_date.display()
