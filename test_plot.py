from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import random

def test_plot_water_levels():

    stations = build_station_list()
    update_water_levels(stations)

    dt = 10
    x = random.randrange(0, len(stations)-1, 1)
    y = random.randrange(0, len(stations)-1, 1)

    #check whether function actually plots anyting or not
    for i in [x, y]:
        station = stations[i]
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

def test_plot_water_level_with_fit():
    stations = build_station_list()
    update_water_levels(stations)

    p = 4
    dt = 10
    x = random.randrange(0, len(stations)-1, 1)
    y = random.randrange(0, len(stations)-1, 1)

    for i in [x, y]:
        station = stations[i]
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)