import numpy as np
import matplotlib
from floodsystem.station import *
import matplotlib.dates as dates
from floodsystem.geo import *

#Define each weight
initial_water_level_weight = 0.5
river_level_weight = 1

#Define constants
normal_water_level = 0.5
effective_radius = 20

def polyfit(dates, levels, p):
    """Fits a polynomial to the graph in Task 2E"""

    x = matplotlib.dates.date2num(dates)
    d0 = x[0]
    x -= d0
    y = levels

    # find coefficients of best-fit polynomial
    p_coeff = np.polyfit(x, y, p)
    # coefficient subbed into general polynomial
    poly = np.poly1d(p_coeff)

    return poly, d0

def determine_numerical_risk(stations):
    """
    Determines the flood risk of each individual station based on weighted sum of risks due to location, nearest river, and surrounding stations (excludes stations with inconsistent data)
    :param stations: Stations to be analyzed
    :return: None
    """

    #Filter out stations with inconsistent data
    good_stations = []
    bad_stations = inconsistent_typical_range_stations(stations)
    for station in stations:
        if station.latest_level is None:
            bad_stations.append(station)
        elif station not in bad_stations:
            good_stations.append(station)

    #Get dictionary with all rivers and stations
    rivers_stations = stations_by_river(good_stations)

    #Process each station and assign an initial risk level based on relative level
    for station in good_stations:
        station.flood_risk_factor = station.relative_water_level() * initial_water_level_weight

    #Get average water level of each river and modify risk factor based on river level
    for key in rivers_stations.keys():
        avg_water_level = sum(station.relative_water_level() for station in rivers_stations[key]) / len(rivers_stations[key])
        for station in rivers_stations[key]:
            station.flood_risk_factor += (avg_water_level - normal_water_level) * river_level_weight

    # Use surrounding risk to predict risk of stations with bad data
    for station in bad_stations:
        stations_in_radius = stations_within_radius(good_stations, station.coord, effective_radius)
        avg_risk_level = sum(station.flood_risk_factor for station in stations_in_radius) / len(stations_in_radius)
        station.flood_risk_factor = avg_risk_level

def stations_by_risk_level(stations):
    determine_numerical_risk(stations)
    #Remove stations with unknown risk levels
    good_stations = [x for x in stations if x.flood_risk_factor is not None]
    risk_stations = sorted(good_stations,key=lambda x: x.flood_risk_factor, reverse=True)
    return risk_stations