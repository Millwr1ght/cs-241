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

print(
    f"Rebounds per season: Min: {min}, Max: {max}, Mean: {mean:.2f}, Median: {median}")
