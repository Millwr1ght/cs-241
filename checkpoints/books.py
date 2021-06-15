"""
W04 : Checkpoint A
Objective : Demonstrate composition in Python (a class that contains another).
Author : Nathan Johnston
"""

class Person:
    def __init__(self, name='anonymous', year='unknown'):
        self.name = name
        self.birth_year = year

    def display(self):
        print(f'{self.name} (b. {self.birth_year})')


class Book:
    def __init__(self, book_title = 'untitled', book_author = Person(), book_publisher = 'unpublished'):
        self.title = book_title
        self.author = book_author
        self.publisher = book_publisher

    def display(self):
        print(f'{self.title}\nPublisher:\n{self.publisher}\nAuthor:')
        self.author.display()


def main():
    """ Create a new book; Call that book's display function; Prompts the user for each 
    of the following: author name and birth year, and the books title and publisher; 
    Sets these values for the current book and it's author. Calls the book's display 
    function again. """
    # new book
    new_book = Book()
    new_book.display()

    # prompt for info
    print('\nPlease enter the following:')
    new_book.author.name = input('Name: ')
    new_book.author.birth_year = input('Year: ')
    new_book.title = input('Title: ')
    new_book.publisher = input('Publisher: ')
    print()

    # display completed book info
    new_book.display()


if __name__ == '__main__':
    main()
