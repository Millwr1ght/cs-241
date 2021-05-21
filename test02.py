def main():
    """
    testing to see how the assignment's datafile is organized:
    zip,eiaid,utility_name,state,service_type,ownership,comm_rate,ind_rate,res_rate
    zip = [0]
    name = [2]
    state = [3]
    comm_rate = [6]
    """
    cumulative_rate_sum = 0
    num_of_rates = 0
    file_to_use = '/home/cs241/assign02/rates.csv'
    with open(file_to_use) as open_file:
        
        first_line = open_file.readline().strip()
        next(open_file)
        for line in open_file:
            line = open_file.readline().strip()    
            data = line.split(',')
            rate = float(data[6])
            # zipcode = int(data[0])
            ult_name = data[2]

            num_of_rates += 1
            cumulative_rate_sum += rate
            # print(zipcode)
            print(ult_name)
            
        print(cumulative_rate_sum/num_of_rates)
    print(first_line)


if __name__ == '__main__':
    main()
