""" 
CS 241 : Team07.py
Employee Wages

Author : Team Tuesday Morning (Nathan Johnston)
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    """ the Employee base class 
    name : string 
    __init__()
    display() : string
    """

    def __init__(self, name):
        """ set up variable """
        self.name = name

    @abstractmethod
    def display(self):
        """ outputs name information """
        raise AttributeError('class needs to overide display method')

    @abstractmethod
    def get_paycheck(self):
        """ paycheck calculator """
        raise AttributeError('class needs to overide paycheck method')


class HourlyEmployee(Employee):
    """ the hourly worker class 
    hourly_wage : int
     __init__()
    display() : string
    """

    def __init__(self, name: str = 'Unnamed', wage: int = 0, hours: int = 20):
        """ setup variable """
        super().__init__(name)

        self.hours = hours
        self.hourly_wage = wage

    def get_paycheck(self):
        """ calculate paycheck """
        print(f'Paycheck: ${self.hours * self.hourly_wage}')

    def display(self):
        """ display the name and wage in the format: "John - $8/hour" """
        print(f'{self.name} - ${self.hourly_wage}/hour')


class SalaryEmployee(Employee):
    """ the salary worker class 
    salary : int
     __init__()
    display() : string
    """

    def __init__(self, name: str = 'Unnamed', wage: int = 0):
        """ setup variable """
        super().__init__(name)

        self.salary = wage

    def get_paycheck(self):
        """ calculate paycheck """
        print(f'Paycheck: ${self.salary / 24}')

    def display(self):
        """ display the name and salary in the format: "John - $50000/year" """
        print(f'{self.name} - ${self.salary}/year')


def display_employee_data(e):
    """ accepts an employee and calls its display function as well as its get_paycheck() function and displays the value """
    e.display()
    e.get_paycheck()


def main():
    """ the main function """

    # Declares a list for employees.
    employees = []

    # Loops until the user enters "q" and prompts the user for an "h" (hourly employee)
    # or an "s" (salary employee) or a "q" to quit.
    # Then prompts for the name and the hourlyRate/salary
    # For each employee entered, creates a new employee of the correct type and adds it to the list.

    while (choice := input('[h]ourly, [s]alary, or [q]uit: ')) != 'q':
        if choice.lower() == 'h':
            name = input('Name: ')
            hourly = int(input('Hourly wages: '))
            hours = int(input('Hours per week: '))
            h = HourlyEmployee(name, hourly, hours)
            employees.append(h)

        elif choice.lower() == 's':
            name = input('Name: ')
            salary = int(input('Salary wages: '))
            s = SalaryEmployee(name, salary)
            employees.append(s)

        else:
            print('Invalid response!')

    # After the user enters "q", have main loop through the list and call the display method for each employee.

    for employee in employees:
        display_employee_data(employee)


# run program
if __name__ == '__main__':
    main()
