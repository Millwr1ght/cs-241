def prompt_filename():
    filename = input('Please enter the data file: ')
    return filename


def rate_look_up(file_to_open):
    # open file
    with open(file_to_open) as open_file:
        # skip first line
        next(open_file)
        for line in open_file:
            num_of_rates += 1

            # get the rate
            strip_line = line.split().rstrip()
            rate = strip_line[6]

            # add the rate to cumulative
            cumulative_rate_sum += rate

            # if the rate is higher than the previous high, then it is the new highest rate
            # if the rate is lower than the last one, then it is the new lowest rate

    # get the average rate
    avg = cumulative_rate_sum/num_of_rates

    # for now
    return avg


def main():
    file_to_use = prompt_filename()
    rate_data = rate_look_up(file_to_use)
    print(f'\nThe average commercial rate is: {rate_data:.2f}')


if __name__ == '__main__':
    main()
