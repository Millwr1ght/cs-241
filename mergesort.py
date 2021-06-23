"""
File: ta10-solution.py // mergesort.py
Author: Br. Burton
This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    # check to see if list is already sorted
    if len(items) > 1:
        # split the list in half at the midpoint
        middle = len(items) // 2

        left_half = items[:middle]
        right_half = items[middle:]

        # sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # compare and merge each half into the list
        i = 0  # index of left_half
        j = 0  # index of right_half
        k = 0  # sorted list index

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1


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
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
