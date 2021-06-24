"""
File: liszt.py 
Author: N Johnston
(lists pun)
Use list manipulation in Python to solve problems
"""

numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]


def print_n():
    print(numbers)


print_n()
# - Insert the number 5 to the beginning of the list.
numbers.insert(0, 5)

# - Remove the number 2348 based on its value (as opposed to a hard-coded index of 4) from the list.
numbers.remove(2348)

# - Create a second list of 5 different numbers and add them to the end of the list in one step.
#       (Make sure it adds the numbers to the list such as: [1, 2, 3, 4, 5] not
#       as a sub list, such as [1, 2, 3, [4, 5]] ).
sublist = [1, 2, 3, 4, 5]
numbers += sublist

print_n()
# - Sort the list using the built in sorting algorithm.
numbers.sort()
print_n()

# - Sort the list backwards using the built in sorting algorithm.
numbers.sort(reverse=True)
print_n()

# - Use a built-in function to count the number of 12's in the list.
twelves = numbers.count(12)
print(f'Number of 12\'s: {twelves}')

# - Use a built-in function to find the index of the number 96.
index96 = numbers.index(96)
print(index96)

# - Use slicing to get the first half of the list, then get the second half of the list and make sure that nothing was left out or duplicated in the middle.
middle = len(numbers) // 2
left_slice = numbers[:middle]
right_slice = numbers[middle:]

print(f'Left slice: {left_slice}')
print(f'Right slice: {right_slice}')

# - Use slicing to create a new list that has every other item from the original list (i.e., skip elements, using the step functionality).
skipped = numbers[::2]
print(skipped)

# - Use slicing to get the last 5 items of the list. For this, please use negative number indexing.
last5 = numbers[-1:-6:-1]
print(last5)
