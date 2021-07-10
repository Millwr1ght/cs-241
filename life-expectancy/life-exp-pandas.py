"""
File: life-exp-pandas.py
Author: Nathan Johnston

Objective: Analysis of a census data

"""
import pandas
import matplotlib.pyplot as plt


def get_stats(year, data):
    """ """
    # all years and countries
    if year == 'all':
        return get_min_max_mean_age(data)

    # data for one year
    elif type(year) == int:
        data_year = data[data.year == year]
        return get_min_max_mean_age(data_year)

    # data for one country
    elif type(year) == str and year != 'all':
        # year may actually be country
        data_country = data[data.country == year]

        # get max, min, etc
        max, min, mean = get_min_max_mean_age(data_country)

        # make the year the row label
        data_country.index = data_country.year

        # drop the year column
        data_country = data_country.drop(["year"], axis=1)

        return data_country, max, min, mean


def get_min_max_mean_age(data):
    max = data.loc[data.age.idxmax()]
    min = data.loc[data.age.idxmin()]
    mean = data.age.mean()
    return max, min, mean


def print_line_plot(data):
    """ makes a line graph of a countries life expectancy through time """
    data.age.plot()
    plt.show()


def print_year_graph(data, year):
    """ make a bar graph of all countries life expectancies in a given year """
    # prepare data
    data_year = data[data.year == year]  # get the year
    data_year.index = data_year.code  # the code index, the codex if you will
    # don't need this column anymore
    data_year = data_year.drop(["code"], axis=1)
    # plot
    ax = data_year.age.plot(kind="bar", rot=10)
    ax.set_ylabel("Life Expectancy (years)")
    plt.show()


def prompt_year():
    """ get the user's input as to a specific year to analyze """
    return int(input('Enter the year of interest: '))


def prompt_country():
    """ get the user's input as to a specific country to analyze """
    return input('Enter a country of interest (for example: Canada): ')


def see_graph():
    """ would the user like to see a graph? """
    choice = input('Would you like to see a graph of this information? (y/n) ')
    return choice.lower() == 'y' or choice.lower() == 'yes'


def main():
    """ main funct. """
    # census file name
    census_file = "life-expectancy\\life-expectancy.csv"

    # read file
    census = pandas.read_csv(census_file)

    # rename columns
    census.columns = ["country", "code", "year", "age"]

    # get the max and min from the data
    max_country, min_country, avg_age = get_stats('all', census)
    print(
        f'The overall max life expectancy is: {max_country.age:.3f} from {max_country.country} in {max_country.year}')
    print(
        f'The overall min life expectancy is: {min_country.age:.3f} from {min_country.country} in {min_country.year}')

    choice = -1
    while choice != 3:
        print('\nWhat part of the census do you want to look at?\n 1: Specific year\n 2: Specific country\n 3: Quit')
        choice = int(input('(1, 2, or 3): '))
        if choice == 1:
            # now for the year
            year = prompt_year()
            max_country, min_country, avg_age = get_stats(year, census)

            print(f'\nIn the year {year}:')
            print(
                f'The average life expectancy across the world was {avg_age:.3f}')
            print(
                f'The max life expectancy was in {max_country.country} with {max_country.age}')
            print(
                f'The min life expectancy was in {min_country.country} with {min_country.age}')

            if see_graph():
                # plot it!
                print_year_graph(census, year)

        elif choice == 2:
            # specific country data
            country = prompt_country()
            country_data, max_year, min_year, trash = get_stats(
                country, census)

            print(
                f'The max life expectancy was in {max_year.year} with {max_year.age}')
            print(
                f'The min life expectancy was in {min_year.year} with {min_year.age}')

            if see_graph():
                # plot it!
                print_line_plot(country_data)

        elif choice == 3:
            print('\nThank you for using our Census Data Lookup Service!')

        else:
            print('Please make a valid selection: 1, 2, or 3')


if __name__ == '__main__':
    main()
