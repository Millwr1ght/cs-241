"""
File: ta10-solution.py // quicksort.py
Author: Br. Burton
This file demonstrates the quick sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def quick_sort(items, first, last):
    """ 
    quick sort the items List 
    """
    # check to see if list is already sorted (only one index)
    if first < last:
        # find the middle
        middle = middle_finder(items, first, last)

        # split and sort either half
        quick_sort(items, first, middle - 1)  # left_half
        quick_sort(items, middle + 1, last)  # right_half


def middle_finder(items, first, last):
    """
    find the middle of the list (approx)
    """
    pivot = items[first]
    left = first + 1
    right = last

    # march to the middle
    working = True
    while working:

        # march left
        while left <= right and items[left] <= pivot:
            left += 1

        # march right
        while right >= left and items[right] >= pivot:
            right -= 1

        if right < left:
            working = False
        else:
            items[left], items[right] = items[right], items[left]

    # you have reached the middle
    items[first], items[right] = items[right], items[first]

    return right


def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests thequick sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    quick_sort(items, 0, len(items) - 1)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
