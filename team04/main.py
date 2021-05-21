"""
w04 team assignment : Main.py

"""

# get the Assignment class from assignment.py
from assignment import Assignment

def main():
    """  creates a new Assignment, prompts for its values and display them.  """
    new_assignment = Assignment()
    new_assignment.prompt()
    new_assignment.display()


if __name__ == '__main__':
    main()