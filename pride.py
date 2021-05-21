def prompt_filename():
    name_of_file = input('Which file shall we open today? ')
    return name_of_file


def prompt_word():
    word_to_find = input('Which word shall we find? ')
    return word_to_find


def parse_file(filename, word_to_find):
    # open file
    count = 0
    with open(filename) as open_file:
        print(open_file)
        for line in open_file:
            # read through word by word
            for word in line.split():
                # debug: print each word
                print(word)
                if word_to_find.lower() in word:
                    count += 1
    # close file
    return count


def main():
    print('Welcome to the file opener!')
    the_file = prompt_filename()
    the_word = prompt_word()
    print(f'Opening file \'{the_file}\'')
    word_count = parse_file(the_file, the_word)
    print(f'The word \'{the_word}\' occurs {word_count} times.')


if __name__ == "__main__":
    main()
