def prompt_number():
    num = input('Enter a number (0 to quit): ')
    return num

def main():
    odd_list = []
    even_list = []
    sorting = True
    while sorting:
        try:
            num_to_sort = int(prompt_number())
            if num_to_sort == 0:
                sorting = False
            elif num_to_sort % 2 == 0:
                even_list.append(num_to_sort)
            elif num_to_sort % 2 == 1:
                odd_list.append(num_to_sort)
        except:
            print('A number please.')
            
    print('\nEven numbers:')
    for even in even_list:
        print(even)
    
    print('\nOdd numbers:')
    for odd in odd_list:
        print(odd)
    
if __name__ == '__main__':
    main()