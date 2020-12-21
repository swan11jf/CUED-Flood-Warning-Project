# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from haversine import haversine, Unit
from .utils import *

def stations_by_distance(stations, p):
    """
    Returns a list of stations sorted by distance to p

    :param stations: A list of all stations to be tested
    :param p: The centre point of testing
    :return: A list of tuples (station, distance to p) that is sorted in order of increasing distance to p
    """
    stations_distance = [(x, haversine(x.coord,p,unit=Unit.KILOMETERS)) for x in stations]
    return sorted_by_key(stations_distance,1)

def stations_within_radius(stations, centre, r):
    """
    Returns a list of stations that are within a radius r of the centre point

    :param stations: A list of all stations
    :param centre: Center point of region
    :param r: Radius of testing
    :return: A list of all stations with radius r
    """
    stations_sorted = stations_by_distance(stations,centre)
    stations_within = []
    for x in stations_sorted:
        if x[1] <= r:
            stations_within.append(x[0])
        else:
            break
    return stations_within

def rivers_with_station(stations):
    """Given a station object returns names of the rivers with a monitoring station."""
    rivers = set()
    for x in stations:
        rivers.add(x.river)
    return rivers

def stations_by_river(stations):
    """Maps river names to a list of station objects on a given river"""
    dict = {}
    rivers = rivers_with_station(stations)

    for river in rivers:
        dict[river] = []

    for station in stations:
        dict[station.river].append(station)

    return dict

def rivers_by_station_number(stations, N):
    """Determines N rivers with the greatest number of monitoring stations"""
    dict = stations_by_river(stations)
    list_rivers = []

    for k, v in dict.items():
        num = len(v)
        list_rivers.append((k, num))

    list_rivers_sort = sorted_by_key(list_rivers, 1, True)

    list_output = []
    i = 0
    for river in list_rivers_sort:
        list_output.append(river)
        i+=1
        if i < len(list_rivers_sort) and list_rivers_sort[i][1] == list_output[-1][1]:
            continue
        elif i >= N:
            break
    return list_output