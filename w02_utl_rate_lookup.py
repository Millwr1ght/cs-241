def prompt_filename():
    """
    asks for a file path, returns the input
    """
    filename = input('Please enter the data file: ')
    return filename


def rate_look_up(file_to_open):
    """
    skip the first line of the file, and reiterate line by line
    find the commercial rate (line[6] given the .csv structure)
    calculate average, lowest and highest rates
    """
    # variables to find
    num_of_rates = 0
    cumulative_rate_sum = 0
    high_rate = {
        'company': 'Name',
        'zip': '',
        'state': '',
        'rate': 0.0
    }
    low_rate = {
        'company': 'Name',
        'zip': '',
        'state': '',
        'rate': 1.0
    }

    # open file
    with open(file_to_open) as open_file:
        # skip first line
        next(open_file)
        for line in open_file:
            num_of_rates += 1

            # get the rate
            strip_line = line.strip()
            data = strip_line.split(',')
            rate = float(data[6])

            # add the rate to cumulative
            cumulative_rate_sum += rate

            # if the rate is higher than the previous high, then it is the new highest rate
            if rate > high_rate["rate"]:
                high_rate["rate"] = rate
                high_rate["zip"] = data[0]
                high_rate["company"] = data[2]
                high_rate["state"] = data[3]
            # if the rate is lower than the last one, then it is the new lowest rate
            if rate < low_rate["rate"]:
                low_rate["rate"] = rate
                low_rate["zip"] = data[0]
                low_rate["company"] = data[2]
                low_rate["state"] = data[3]

    # get the average rate
    avg_rate = cumulative_rate_sum/num_of_rates

    return avg_rate, high_rate, low_rate


def main():
    """
    gets filename of commercial utility rates, then look up those rates on the file
    displays average rate, as well as highest and lowest rates
    """
    file_to_use = prompt_filename()
    rate_avg, rate_high, rate_low = rate_look_up(file_to_use)
    print(f'\nThe average commercial rate is: {rate_avg}')
    print(f'\nThe highest rate is:\n{rate_high["company"]} ({rate_high["zip"]}, {rate_high["state"]}) - ${rate_high["rate"]:.12f}')
    print(f'\nThe lowest rate is:\n{rate_low["company"]} ({rate_low["zip"]}, {rate_low["state"]}) - ${rate_low["rate"]:.1f}')


if __name__ == '__main__':
    main()
