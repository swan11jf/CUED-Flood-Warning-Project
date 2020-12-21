# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        self.flood_risk_factor = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   latest level:  {}\n".format(self.latest_level)
        d += "   relative level:{}\n".format(self.relative_water_level())
        d += "   risk_factor:   {}\n".format(self.flood_risk_factor)
        d += "   risk_level:    {}".format(self.readable_risk())
        return d

    def typical_range_consistent(self):
        """
        Determines if the typical range exists and is valid data

        :return: if the typical range is valid data
        """
        return self.typical_range is not None and self.typical_range[0] is not None and self.typical_range[1] is not None and self.typical_range[0] <= self.typical_range[1]

    def relative_water_level(self):
        """
        Determines the current relative water level according to the typical levels.
        At the lowest level, relative water level is 0.0 and at the highest relative level is 1.0

        :return: Current relative water level
        """
        if not self.typical_range_consistent() or self.latest_level is None:
            return None
        return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])

    def readable_risk(self):
        """
        Changes numerical flood risk into human readable form. Values for each are determined by the median, third quartile, and 7th octile of a given set of data
        :return: String containing flood risk level
        """
        #0.25 is value of normal risk level at all normal relative water levels
        #I would have imported it from analysis however that introduces circular dependencies that cause the program to fail
        if self.flood_risk_factor is None:
            return "Unknown"
        elif self.flood_risk_factor <= 0.25:
            return "Low"
        elif self.flood_risk_factor <= 0.25 * 2.5:
            return "Moderate"
        elif self.flood_risk_factor <= 0.25 * 4:
            return "High"
        else:
            return "Severe"


def inconsistent_typical_range_stations(stations):
    """
    Creates a list of stations that have inconsistent typical range data or have no data for

    :param stations: A list of stations to be evaulated
    :return: A list of stations with inconsistent typical range
    """
    inconsistent_stations = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_stations.append(station)
    return inconsistent_stations

