"""
File: sorting.py
Assignment: check10a.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """

    # put the smallest number in the first slot
    for slot_to_fill in range(len(numbers)):
        slot_of_min = slot_to_fill

        # for each number in the unsorted part of the list
        for j in range(slot_to_fill + 1, len(numbers)):
            # if current index value is smaller than the min, replace
            if numbers[slot_of_min] > numbers[j]:
                slot_of_min = j

        numbers[slot_to_fill], numbers[slot_of_min] = numbers[slot_of_min], numbers[slot_to_fill]
        # the first number in the list is now sorted


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
