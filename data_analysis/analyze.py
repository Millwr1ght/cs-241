"""
file: analyze.py
author: Nathan Johnston


incomplete

"""

"""
Part 1:
1.  Calculate the mean and median number of points scored. (In other words, each row
    is the amount of points a player scored during a particular season. Calculate the
    median of these values. The result of this is that we have the median number of
    points players score each season.)
2.  Determine the highest number of points recorded in a single season. Identify who
    scored those points and the year they did so.
3.  Produce a boxplot that shows the distribution of total points, total assists, and
    total rebounds (each of these three is a separate box plot, but they can be on the
    same scale and in the same graphic).
4.  Produce a plot that shows how the number of points scored has changed over time by
    showing the median of points scored per year, over time. The x-axis is the year and
    the y-axis is the median number of points among all players for that year.

Part 2:
1.  Some players score a lot of points because they attempt a lot of shots. Among
    players that have scored a lot of points, are there some that are much more
    efficient (points per attempt) than others?
         -- if you include --all players-- (that made attempts), Tyler Wheeler, who played all of three minutes in 1998 has the second highest ppa efficiency 1.3333  
2.  It seems like some players may excel in one statistical category, but produce very
    little in other areas. Are there any players that are exceptional across many
    categories?
3.  Much has been said about the rise of the three-point shot in recent years. It seems
    that players are shooting and making more three-point shots than ever. Recognizing
    that this dataset doesn't contain the very most recent data, do you see a trend of
    more three-point shots either across the league or among certain groups of players?
    Is there a point at which popularity increased dramatically?

Part 3:
1.  Many sports analysts argue about which player is the GOAT (the Greatest Of All Time).
    Based on this data, who would you say is the GOAT? Provide evidence to back up your
    decision.
2.  The biographical data in this dataset contains information about home towns, home
    states, and home countries for these players. Can you find anything interesting about
    players who came from a similar location?
3.  Find something else in this dataset that you consider interesting. Produce a graph to
    communicate your insight.

"""




import pandas as pd  # Our data manipulation library
import seaborn as sns  # Used for graphing/plotting
import matplotlib.pyplot as plt  # If we need any low level methods
import os  # Used to change the directory to the right place
def mmmm(data, column):
    max = data[column].max()
    mean = data[column].mean()
    median = data[column].median()
    min = data[column].min()

    return f'min: {min:.1f}, max: {max:.1f}, mean: {mean:.1f}, median: {median:.1f}'


def anything_else(nba):

    pass


def player_homes(nba):

    # sorted by high school state
    players_per_state = nba.groupby(
        'hsState')['playerID'].count().sort_values(ascending=False).head(50)
    print(players_per_state)
    # players_per_state.plot(kind="bar")

    # sorted by hs city
    players_per_state = nba.groupby(
        'hsCity')['playerID'].count().sort_values(ascending=False).head(20)
    print(players_per_state)
    players_per_state.plot(kind="bar")


def finding_the_GOAT(nba):

    pass


def three_point_shot_trends(nba):

    pass


def exceptional_players(nba):

    nba_players = nba[['playerID', 'year', 'points', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers',
                       'fgMade', 'ftMade', 'threeMade', 'useFirst', 'lastName']]
    nba_players['name'] = nba_players['useFirst'] + \
        ' ' + nba_players['lastName']

    aggregation_functions = {
        'year': 'last',
        'name': 'first',
        'points': 'sum',
        'rebounds': 'sum',
        'assists': 'sum',
        'steals': 'sum',
        'blocks': 'sum',
        'turnovers': 'sum',
        'threeMade': 'sum',
        "fgMade": 'sum',
        'ftMade': 'sum'
    }

    list_of_aggergated_stats = ['points', 'rebounds', 'assists',
                                'steals', 'blocks', 'turnovers', 'fgMade', 'ftMade', 'threeMade']

    nba_player_totals = nba_players.groupby(
        'playerID').agg(aggregation_functions)

    for stat in list_of_aggergated_stats:
        # for each stat, remove all players below the mean
        nba_best = nba_player_totals[nba_player_totals[stat]
                                     > nba_player_totals[stat].mean()]

    print(nba_best.name.count())  # 690 players above the mean of all stats

    for stat in list_of_aggergated_stats:
        # for each stat, remove all players below the mean
        nba_very_best = nba_best[nba_best[stat] > nba_best[stat].mean()]

    print(nba_very_best.name.count())  # 238 above the nba_best means

    for stat in list_of_aggergated_stats:
        # for each stat, remove all players below the mean
        nba_very_x2_best = nba_very_best[nba_very_best[stat]
                                         > nba_very_best[stat].mean()]

    print(nba_very_x2_best.name.count())  # 97 above the nba_very_best means

    for stat in list_of_aggergated_stats:
        # for each stat, remove all players below the mean
        nba_very_x3_best = nba_very_x2_best[nba_very_x2_best[stat]
                                            > nba_very_x2_best[stat].mean()]

    print(nba_very_x3_best.name.count())  # 40 above the nba_very_x2_best means

    for stat in list_of_aggergated_stats:
        # for each stat, remove all players below the mean
        nba_very_x4_best = nba_very_x3_best[nba_very_x3_best[stat]
                                            > nba_very_x3_best[stat].mean()]

    # the 18 above all the nba_very_x3_best means
    print(nba_very_x4_best.name.count())

    # print(nba_very_x4_best)

    for stat in list_of_aggergated_stats:
        print(stat)
        print(f'all players: {mmmm(nba_player_totals, stat)}')
        print(f'very(x4) best: {mmmm(nba_very_x4_best, stat)}\n')

    for stat in list_of_aggergated_stats:
        # for each stat, remove all players below the mean
        nba_very_x5_best = nba_very_x4_best[nba_very_x4_best[stat]
                                            > nba_very_x4_best[stat].mean()]

    # the 18 above all the nba_very_x4_best means
    print(nba_very_x5_best)

# completed


def point_efficiency(nba):

    # get the useful rows
    nba_points = nba[["playerID", "year", "useFirst", "lastName", "points", "fgAttempted",
                      "fgMade", "ftAttempted", "ftMade"]]
    nba_points['name'] = nba_points['useFirst'] + ' ' + nba_points['lastName']

    # aggregate the columns by playerID
    aggregation_functions = {
        'year': 'last', 'name': 'first', 'points': 'sum', 'fgAttempted': 'sum', "fgMade": 'sum', "ftAttempted": 'sum', 'ftMade': 'sum'
    }
    nba_eff = nba_points.groupby(
        nba_points['playerID']).agg(aggregation_functions)

    # make new columns
    nba_eff['totalMade'] = nba_eff.fgMade + nba_eff.ftMade
    nba_eff['totalAttempts'] = nba_eff.fgAttempted + nba_eff.ftAttempted
    nba_eff["pointsPerAttempt"] = nba_eff.points / nba_eff.totalAttempts

    # filter out players who don't shoot hoops and lived before these stats were measured
    nba_eff = nba_eff[(nba_eff.ftAttempted > 0) | (nba_eff.fgAttempted > 0)]
    nba_eff = nba_eff[nba_eff.year > 1952]
    # more than the mean amount a points
    nba_eff = nba_eff[nba_eff.points > 3200]

    print(nba_eff[["name", "year", "points", "fgAttempted", "fgMade", "ftAttempted", "ftMade", "totalAttempts",
          "totalMade", "pointsPerAttempt"]].sort_values("pointsPerAttempt", ascending=False).head(10))

    nba_f = nba_eff[["name", "pointsPerAttempt"]].sort_values(
        "pointsPerAttempt", ascending=False).head(10)

    nba_f.index = nba_f.name
    ax = nba_f.plot(kind="bar", rot=10)
    ax.set_ylabel("Points Per Attempt")

    mmmm(nba_eff, 'pointsPerAttempt')


def median_points_per_year():

    nba_ppy = nba.groupby('year')['points'].median()
    nba_ppy.plot()


def totals_boxplots():

    # nba_players_total_rebounds = nba.groupby("playerID")['rebounds']
    # nba_players_total_assists = nba.groupby("playerID")['assists']
    # nba.boxplot(column='points', return_type='axes')

    nba_totals = nba.filter(['points', 'rebounds', 'assists'], axis=1)
    nba_totals.boxplot(return_type='axes')
    plt.show()
    # sns.boxplot(nba_players_total_rebounds['rebounds'], orient='v')
    # plt.show()
    # sns.boxplot(nba_players_total_assists['assists'], orient='v')
    # plt.show()


def mean_median_max_points_scored():

    median = nba.points.median()
    mean = nba.points.mean()
    max = nba.loc[nba.points.idxmax()]

    print(f'The median points scored in a season is {median}.')
    print(f'The average points scored in a season: {mean}')
    print('The max points scored in a season was by:')
    print(f'{max.useFirst} {max.lastName} in {max.year} with {max.points}')


def top_10_rebounders():

    # rebounds per game
    nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]

    # remove those with no games
    nba = nba[nba.GP > 0]

    print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]
              ].sort_values("reboundsPerGame", ascending=False).head(10))
    # Get the top 10 rebounders per year
    nba_topRebounders_perYear = nba[["reboundsPerGame", "year"]].groupby("year")[
        "reboundsPerGame"].nlargest(10)

    # Get the median of these 10
    nba_topRebounders_median_perYear = nba_topRebounders_perYear.groupby(
        "year").median()

    # Put year back in as a column
    nba_topRebounders_median_perYear = nba_topRebounders_median_perYear.reset_index()

    # Again no zeros...
    nba_topRebounders_median_perYear_noZeros = nba_topRebounders_median_perYear[
        nba_topRebounders_median_perYear["reboundsPerGame"] > 0]

    # Now plot top 10 rebounders
    sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year",
                y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")


def setup():
    # change directory to the data pile
    os.chdir("data_analysis/nba_data/")

    # get players
    players = pd.read_csv("basketball_players.csv")
    sm_players = players.drop(['PostGP', 'PostGS',
                               'PostMinutes', 'PostPoints', 'PostoRebounds', 'PostdRebounds',
                               'PostRebounds', 'PostAssists', 'PostSteals', 'PostBlocks',
                               'PostTurnovers', 'PostPF', 'PostfgAttempted', 'PostfgMade',
                               'PostftAttempted', 'PostftMade', 'PostthreeAttempted', 'PostthreeMade'], axis=1)

    # The "master" data (basketball_master.csv) has names, biographical information, etc.
    master = pd.read_csv("basketball_master.csv")
    sm_master = master.drop(['firstName', 'middleName', 'nameGiven', 'fullGivenName',
                            'nameSuffix', 'nameNick', 'firstseason', 'lastseason'], axis=1)
    # We can do a left join to "merge" these two datasets together
    nba = pd.merge(sm_players, sm_master, how="left",
                   left_on="playerID", right_on="bioID")

    return nba


""""""
nba = setup()
""""""
print(nba.columns)
""""""

# mean_median_max_points_scored()
# totals_boxplots()
# median_points_per_year()
# point_efficiency(nba)
# exceptional_players(nba=nba)
three_point_shot_trends(nba)
finding_the_GOAT(nba)
player_homes(nba)
anything_else(nba)


# Show the current plot
plt.show()
