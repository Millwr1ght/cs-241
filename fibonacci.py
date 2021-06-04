"""
Fibonacci.py

Author: Nathan Johnston
"""


# Write a function, def fib(n), that computes the Fibonacci number at index n.

def fib(n):
    """ 
    computes the Fibonacci number at index n
    """
    if n <= 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    """ the main function """
    num = int(input('Pick the nth fibonacci number: (0 -> n) '))
    print(fib(num))


if __name__ == '__main__':
    main()
