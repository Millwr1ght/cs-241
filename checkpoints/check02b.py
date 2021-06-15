def prompt_filename():
    """ asks for a file path, returns the input"""
    filename = input('Enter file: ')
    return filename

def lines_and_words(filepath):
    """counts all lines and words in a file, returns the values as a tuple"""
    words = 0
    lines = 0
    with open(filepath) as open_file:
        for line in open_file:
            lines += 1
            for word in line.split():
                words += 1
    
    return lines, words

def main():
    file_to_read = prompt_filename()
    num_of_lines, num_of_words = lines_and_words(file_to_read)
    print(f'The file contains {num_of_lines} lines and {num_of_words} words.')

if __name__ == "__main__":
    main()