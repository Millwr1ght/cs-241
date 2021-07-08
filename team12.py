"""
team activity #12
team tuesday lunch

pandas
"""
from datetime import datetime
import matplotlib.pyplot as plt
import pandas

weather_file = "./weather_year.csv"

data = pandas.read_csv(weather_file)

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]


data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))

data.index = data.date

data = data.drop(["date"], axis=1)

# empty = data.apply(lambda col: pandas.isnull(col))

data.events = data.events.fillna("")

""" num_rain = 0
for idx, row in data.iterrows():
    if "Rain" in row["events"]:
        num_rain += 1

print(f"Days with rain: {num_rain}")
 """

""" freezing_days = data[(data.max_temp <= 32) & (data.min_temp >= 20)]
print(freezing_days) """

cover_temps = {}
for cover, cover_data in data.groupby("cloud_cover"):
    cover_temps[cover] = cover_data.mean_temp.mean()  # The mean mean temp!

for event_kind in ["Rain", "Thunderstorm", "Fog", "Snow"]:
    col_name = event_kind.lower()  # Turn "Rain" into "rain", etc.
    data[col_name] = data.events.apply(lambda e: event_kind in e)


# data.max_temp.plot()
# data.max_temp.tail().plot(kind="bar", rot=10)
ax = data.max_temp.plot(title="Min and Max Temperatures")
data.min_temp.plot(style="red", ax=ax)
ax.set_ylabel("Temperature (F)")

plt.show()

data.to_csv("data/weather-mod.csv")
