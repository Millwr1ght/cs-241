import pandas as pd  # Our data manipulation library
import seaborn as sns  # Used for graphing/plotting
import matplotlib.pyplot as plt  # If we need any low level methods
import os  # Used to change the directory to the right place

# change directory to the data pile
os.chdir("data_analysis/nba_data/")

# get players
players = pd.read_csv("basketball_players.csv")

# print(players)
min = players["rebounds"].min()
max = players["rebounds"].max()
mean = players["rebounds"].mean()
median = players["rebounds"].median()

#print(f"Rebounds per season: Min: {min}, Max: {max}, Mean: {mean:.2f}, Median: {median}")

# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")

# We can do a left join to "merge" these two datasets together
nba = pd.merge(players, master, how="left",
               left_on="playerID", right_on="bioID")

# rebounds per game
nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]

# remove those with no games
nba = nba[nba.GP > 0]

print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]
          ].sort_values("reboundsPerGame", ascending=False).head(10))
# plot it
# sns.boxplot(data=nba.reboundsPerGame)

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

# Now plot
sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year",
            y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")

# Show the current plot
plt.show()
