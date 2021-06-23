"""
File: sorting.py
Assignment: check10b.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    # insertion sort
    # begin by assuming that a list with one item (position 0) is already sorted
    # On each pass, one for each item 1 through n−1
    for i in range(1, len(numbers)):
        # the current item is checked against those in the already sorted sublist.
        current = numbers[i]
        index = i
        # shift those items that are greater to the right.
        while index > 0 and numbers[index-1] > current:
            numbers[index] = numbers[index-1]
            index -= 1
        # When we reach a smaller item or the end of the sublist, the current item can be inserted.
        numbers[index] = current


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()
