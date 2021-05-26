""" 
CS241 : Check06A
Bookshelf.py
Author : Nathan Johnston

"""


class Book:
    """ the generic Book class """

    def __init__(self, title='', author='', year=1970):
        """ setup variables """
        self.author = author
        self.title = title
        self.publication_year = year

    def prompt_book_info(self):
        """ GET user input on book's info """
        self.title = input('Title: ')
        self.author = input('Author: ')
        self.publication_year = int(input('Publication Year: '))

    def display_book_info(self):
        """ Output book's info """
        print(f'\n{self.title} ({self.publication_year}) by {self.author}')


class TextBook(Book):
    """ the Textbook subclass of Book """

    def __init__(self, title='', author='', year=1970, subject=''):
        """ setup variables """
        # GET Book chassis
        super().__init__(title, author, year)

        # setup own values
        self.subject = subject

    def prompt_subject(self):
        """ GET subject info """
        self.subject = input('Subject: ')

    def display_subject(self):
        """ ouput subject """
        print(f'Subject: {self.subject}')


class PictureBook(Book):
    """ the Illustrated subclass of Book """

    def __init__(self, title='', author='', year=1970, illustrator=''):
        """ setup variables """
        # GET Book chassis
        super().__init__(title, author, year)

        # setup own values
        self.illustrator = illustrator

    def prompt_illustrator(self):
        """ GET illustrator info """
        self.illustrator = input('Illustrator: ')

    def display_illustrator(self):
        """ ouput illustrator """
        print(f'Illustrated by {self.illustrator}')


def main():
    """ the main meat of this shindig """

    # Book
    book1 = Book()
    book1.prompt_book_info()
    book1.display_book_info()
    print()
    # TextBook
    book2 = TextBook()
    book2.prompt_book_info()
    book2.prompt_subject()
    book2.display_book_info()
    book2.display_subject()
    print()
    # PictureBook
    book3 = PictureBook()
    book3.prompt_book_info()
    book3.prompt_illustrator()
    book3.display_book_info()
    book3.display_illustrator()


if __name__ == '__main__':
    main()
