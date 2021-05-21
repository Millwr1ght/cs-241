def prompt_number():
    """asks for a number, returns it"""
    number = -1
    while number < 0:
        number = int(input('Enter a positive number: '))
        if number < 0:
            print('Invalid entry. The number must be positive.')
    print()
    return number


def compute_sum(*nums):
    """adds up all the numbers passed to the function"""
    sum = 0
    for num in nums:
        sum += num
    return sum


def main():
    num1 = prompt_number()
    num2 = prompt_number()
    num3 = prompt_number()
    sum_all = compute_sum(num1, num2, num3)
    print(f'The sum is: {sum_all}')


if __name__ == "__main__":
    main()
