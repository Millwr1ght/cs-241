class Stack:
    """ """

    def __init__(self):
        self.stack = []

    def push(self, char):
        self.stack.append(char)

    def is_empty(self):
        if len(self.stack) != 0:
            return False
        return True

    def check_closing(self, char):
        if self.is_empty():
            return False
        last_brace_added = self.stack.pop()
        if (last_brace_added == '(' and char == ')') or (last_brace_added == '[' and char == ']') or (last_brace_added == '{' and char == '}'):
            # print('they match!')
            return True
        else:
            # print(f'they don\'t match! end this now! {char} | {last_brace_added}')
            self.push(last_brace_added)
            return False


def prompt():
    return input('File: ')


def main():
    """ """
    braces = Stack()
    good = True

    with open(prompt()) as open_file:
        for line in open_file:
            if not good:
                break
            for word in line.split():
                if not good:
                    break
                for char in word:
                    if char == '(' or char == '[' or char == '{':
                        # print(char)
                        braces.push(char)
                    elif char == ')' or char == ']' or char == '}':
                        does_it_match_the_end_of_the_stack = braces.check_closing(char)
                        if not does_it_match_the_end_of_the_stack:       
                            # if bad, be done
                            good = False


    if len(braces.stack) == 0 and good:
        print('Balanced')
    else:
        print('Not balanced')
    
    # print(braces.stack)


if __name__ == '__main__':
    main()
